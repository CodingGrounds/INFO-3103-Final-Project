"""
Object representation for the users table / user entities.
Acts as the interface between the database and the application.

Usage:

The constructor takes in one required param – username – and two optional
params – name, and email. Returns a User object with the given properties.
"""

import json

from database.database_helper import DatabaseHelper
from util.validators import validate_id


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
        """
        if self.id is not None:
            # currently only supports saving new records, not updating existing ones
            raise ValueError('The `User.id` attribute must be None to save a User object.')

        if self.username in (None, ''):
            raise ValueError('The `User.username` attribute must not be empty to save a User object.')

        if not User.username_available(self.username):
            # This should probably be some other exception
            # Maybe some custom ones should be made?
            raise NameError(f'The username {self.username} is already taken.')

        with DatabaseHelper() as db:
            db.callproc('add_user', [self.username, self.name, self.email])

        return User.get_by_identifier(self.username, is_username=True).id

    @classmethod
    def get_by_identifier(cls, identifier, is_username=None):
        """
        Query the database for a single User record based on identifier (ID/username).

        :param identifier: the identifier value of the User record to find
        :param is_username: whether the identifier value represents a username. False implies the identifier is an ID

        Returns:
            If a user record exists with the given identifier, return that record

        Raises:
            ValueError:
                - is_username is None
                - identifier is None or an empty string
            LookupError:
                - no User record with the given identifier exists
        """

        if is_username is None:
            raise ValueError('`is_username` must be explicitly set to True or False.')

        if identifier in (None, ''):
            raise ValueError('`identifier` is a required parameter.')

        if is_username:
            identifier_type = 'username'
        else:
            identifier_type = 'id'
            identifier = validate_id(identifier)

        stored_proc = f'get_user_by_{identifier_type}'

        # Convert to iterable for PyMySQL
        identifier = (identifier,)
        with DatabaseHelper() as db:
            record = db.callproc(stored_proc, identifier).fetchone()
            if record is None:
                raise LookupError(f'No user with the given {identifier_type} exists in the database.')

        return User(*record)

    @classmethod
    def username_available(cls, username):
        try:
            # Username is found, so it is unavailable
            User.get_by_identifier(username, is_username=True)
            return False
        except LookupError:
            # Username is not found, so it is available
            return True

    @property
    def json(self):
        return json.dumps({
            "id": self.id,
            "username": self.username,
            "name": self.name,
            "email": self.email
        })
