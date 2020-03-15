"""
Wrapper for file collection management (upload file, view collection)

Code-centric usage is all handled automatically by Flask-Session.

CLI Usage (with app running on info3103:1503):
    Upload a file:
        Pay special attention to "LOCAL_FILE_NAME_HERE", port number, and user identifier in the URL
        curl -i -H "Content-Type: multipart/form-data" -X POST -F "file=@LOCAL_FILE_NAME_HERE" -b cookie-jar https://info3103.cs.unb.ca:1503/users/1/files -v -k

    View all files for user:
        Pay special attention to port number and user identifier in the URL
        curl -i -H "Content-Type: application/json" -X GET -b cookie-jar https://info3103.cs.unb.ca:1503/users/1/files -v -k
 """
import os

from flask import request
from flask_restful import Resource
from werkzeug.utils import secure_filename

from app_config import UPLOAD_FOLDER
from database.models.file import File
from database.models.user import User
from util.decorators import conceal_error_message, require_session
from util.responses import resource_created, resource_list, ERROR_400, ERROR_404, ERROR_409


class FileCollectionManager(Resource):

    @conceal_error_message
    @require_session
    def post(self, user_identifier):
        """
        Upload a new file.
        """
        if 'file' not in request.files:
            return ERROR_400

        file = request.files['file']

        # User did not select a file, so HTTP sends empty filename
        if file.filename == '':
            return ERROR_400

        owner = User.get(user_identifier)

        # Build the filesystem path
        sanitized_filename = secure_filename(file.filename)
        path = os.path.join(UPLOAD_FOLDER, owner.username, sanitized_filename)
        if os.path.exists(path):  # file already exists in filesystem
            return ERROR_409

        file.save(path)
        file_size = os.stat(path).st_size
        file_id = File(owner_id=owner.id, name=file.filename, path=path, size=file_size).save()
        return resource_created(file_id)

    @conceal_error_message
    @require_session
    def get(self, user_identifier):
        """
        List all files owned by the given user.
        """
        try:
            owned_files = File.get_by_owner(user_identifier, json=True)
        except LookupError:
            return ERROR_404

        return resource_list(owned_files)
