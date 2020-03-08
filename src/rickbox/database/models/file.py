"""
Object representation for the files table / file entities.
Acts as the interface between the database and the application.

Usage:

The constructor takes in three required params – username – and two optional
params – name, and email. Returns a File object with the given properties.
"""

import json

from database.database_helper import DatabaseHelper
from database.models.user import User
from util.validators import validate_id


class File:
    id = None
    owner_id = None
    name = None
    path = None
    size = None
    last_modified = None

    def __init__(self, id=None, owner_id=None, name=None, path=None, size=None, last_modified=None):
        self.id = id
        self.owner_id = owner_id
        self.name = name
        self.path = path
        self.size = size
        self.last_modified = last_modified

    def save(self):
        """
        Commits a File record to the database.

        :return If the commit was successful, return the ID of the newly-created File

        Raises:
            ValueError:
                - file.id is set (`put` operation is NYI)
                - file.owner_id is blank (None or '')
                - file.name is blank (None or '')
                - file.path is blank (None or '')
            LookupError:
                - User record with id corresponding to `file.user_id` could not be found
                - File record could not be found after saving
            NameError:
                - file.name exists in database already for given owner_id
        """
        if self.id is not None:
            # currently only supports saving new records, not updating existing ones
            raise ValueError('The `File.id` attribute must be None to save a File object.')

        if self.owner_id in (None, ''):
            raise ValueError('The `File.owner_id` attribute must not be empty to save a File object.')

        # further validate the owner_id – this will blow up if it is invalid
        User.get(self.owner_id)

        if self.name in (None, ''):
            raise ValueError('The `File.name` attribute must not be empty to save a File object.')

        if self.path in (None, ''):
            raise ValueError('The `File.path` attribute must not be empty to save a File object.')

        with DatabaseHelper() as db:
            result = db.callproc('add_file', [self.owner_id, self.name, self.path, self.size])
            return result.fetchone()[0]

    @classmethod
    def get_by_id(cls, file_id):
        """
        Query the database for a single File record based on primary key.

        :param file_id: the unique ID of the File record to find

        :return If a File record exists with the given id, return that record

        Raises:
            ValueError:
                - file_id is None or negative
            LookupError:
                - no File record with the given id exists
        """
        file_id = validate_id(file_id)

        with DatabaseHelper() as db:
            record = db.callproc('get_file_by_id', [file_id]).fetchone()
            if record is None:
                raise LookupError('No file with the given id exists in the database.')

        return File.from_record(record)

    @classmethod
    def get_by_owner(cls, owner_identifier, json=False):
        """
        Query the database for all files owned by the user with the given user ID or username.

        :param owner_identifier: the user ID or username of the user whose files to return
        :param json: whether to process the File records into JSON objects

        :return
            - If File records exists with the given owner, return that collection. Else, return an empty List
            - If json=True, process the collection into JSON before returning
        """

        # This validates that the user exists, and allows us to guarantee we are using a user ID.
        owner_id = User.get(owner_identifier).id

        with DatabaseHelper() as db:
            records = db.callproc('get_file_by_owner_id', [owner_id]).fetchall()

        records = [File.from_record(record) for record in records]

        if json:
            records = [record.json for record in records]

        return records

    @classmethod
    def from_record(cls, record):
        """
        Convert a raw database record into a File object.

        :param record: the File record to convert into an object.

        :return a File object
        """
        return File(
            id=record[0],
            owner_id=record[1],
            name=record[2],
            path=record[3],
            size=record[4],
            last_modified=record[5]
        )

    @property
    def json(self):
        """
        Convert the File object into a JSON string representation.

        :return a JSONified File
        """
        return json.dumps({
            "id": self.id,
            "owner_id": self.owner_id,
            "name": self.name,
            "path": self.path,
            "size": self.size,
            "last_modified": self.last_modified.ctime()
        })
