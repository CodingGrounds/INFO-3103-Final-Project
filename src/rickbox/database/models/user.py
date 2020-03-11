"""
Object representation for the users table / user entities.
Acts as the interface between the database and the application.

Usage:

The constructor takes in one required param – username – and two optional
params – name, and email. Returns a User object with the given properties.
"""

import json

from database.database_helper import DatabaseHelper


class User:
    id = None
    username = None
    name = None
    email = None

    def __init__(self, id=None, username=None, name=None, email=None):
        self.id = id
        self.username = username
        self.name = name
        self.email = email

    def save(self):
        """
        Commits a User record to the database.

        Returns:
            If the commit was successful, return the ID of the newly-created User

        Raises:
            ValueError:
                - user.id is set (`put` operation is NYI)
                - user.username is blank (None or '')
            LookupError:
                - User record could not be found after saving
            NameError:
                - user.username exists in database already
            IndexError:
                - When adding the user was unsuccessful on the db side for some reason
        """
        if self.id is not None:
            # currently only supports saving new records, not updating existing ones
            raise ValueError('The `User.id` attribute must be None to save a User object.')

        if self.username in (None, ''):
            raise ValueError('The `User.username` attribute must not be empty to save a User object.')

        if not User.username_available(self.username):
            # This should probably be some other exception, not NameError
            # Maybe some custom ones should be made?
            raise NameError(f'The username {self.username} is already taken.')

        with DatabaseHelper() as db:
            new_user_id = db.callproc('add_user', [self.username, self.name, self.email]).fetchone()[0]
            return f'{new_user_id}'

    @classmethod
    def get(cls, identifier):
        """
        Query the database for a single User record based on identifier.

        :param identifier: the user ID or identifier of the User record to find

        Returns:
            If a user record exists with the given identifier, return that record

        Raises:
            ValueError:
                - identifier is None or an empty string
            LookupError:
                - no User record with the given identifier exists
        """

        if identifier in (None, ''):
            raise ValueError('`identifier` is a required parameter.')

        # Convert to iterable for PyMySQL
        identifier = (identifier,)

        with DatabaseHelper() as db:
            record = db.callproc('get_user', identifier).fetchone()
            if record is None:
                raise LookupError('No user with the given identifier exists in the database.')

        return User(*record)

    @classmethod
    def username_available(cls, username):
        # Username is found, so it is unavailable
        with DatabaseHelper() as db:
            record = db.callproc('get_user_by_username', username).fetchone()
            if record is None:
                # No user with given username has been found => Username is available
                return True
        return False

    @property
    def json(self):
        return json.dumps({
            "id": self.id,
            "username": self.username,
            "name": self.name,
            "email": self.email
        })
