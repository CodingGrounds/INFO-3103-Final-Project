"""
Wrapper for user session logic (log in, log out, check-if-logged-in)

Code-centric usage is all handled automatically by Flask-Session.

CLI Usage (with app running on info3103:1503):
    Log in:
        Pay special attention to port number
        curl -i -H "Content-Type: application/json" -X POST -d '{"username": "jsmith123", "password": "secret"}' -c cookie-jar http://info3103.cs.unb.ca:1503/login

    Upload a file:
        Pay special attention to "LOCAL_FILE_NAME_HERE", port number, and user id
        curl -i -H "Content-Type: multipart/form-data" -X POST -F "file=@LOCAL_FILE_NAME_HERE" -b cookie-jar http://info3103.cs.unb.ca:1503/users/1/files  -v

    View all files for user:
        Pay special attention to port number and user id
        curl -i -H "Content-Type: application/json" -X GET -b cookie-jar http://info3103.cs.unb.ca:1503/users/1/files -v
 """
import os

from flask import request
from flask_restful import Resource
from werkzeug.utils import secure_filename

from app_config import UPLOAD_FOLDER
from database.models.file import File
from util.decorators import conceal_error_message, require_session
from util.responses import resource_created, resource_list, ERROR_400


class FileManager(Resource):

    @conceal_error_message
    @require_session
    def post(self, user_id):
        if 'file' not in request.files:
            return ERROR_400

        file = request.files['file']

        # User did not select a file, so HTTP sends empty filename
        if file.filename == '':
            return ERROR_400

        # prepend filenames with user IDs to avoid naming conflicts
        filename = f"USERID_{user_id}_" + file.filename
        filename = secure_filename(filename)
        path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(path)

        file_size = os.stat(path).st_size

        file_id = File(owner_id=user_id, name=filename, path=path, size=file_size).save()

        return resource_created(file_id)

    @conceal_error_message
    @require_session
    def get(self, user_identifier):
        owned_files = File.get_by_owner(user_identifier, json=True)
        return resource_list(owned_files)

    @conceal_error_message
    @require_session
    def delete(self):
        pass
