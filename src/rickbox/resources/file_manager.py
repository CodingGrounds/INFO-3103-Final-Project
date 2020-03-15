"""
Wrapper for individual file management (download, delete).

Code-centric usage is all handled automatically by Flask-Session.

CLI Usage (with app running on info3103:1503):
    Download a file:
        Pay special attention to "LOCAL_FILE_NAME_HERE", port number, user identifier in the URL, and OUTPUT_FILE_NAME
        curl -H "Content-Type: application/json" -X GET -b cookie-jar https://info3103.cs.unb.ca:1503/users/USER_IDENTIFIER/files/FILE_ID --output OUTPUT_FILE_NAME -k

    Delete a file:
        Pay special attention to port number, user identifier, and file id
        curl -H "Content-Type: application/json" -X DELETE -b cookie-jar https://info3103.cs.unb.ca:1503/users/USER_IDENTIFIER/files/FILE_ID -i -k

    Rename a file:
        Pay special attention to port number, user identifier, file id, and passed JSON
        curl -i -H "Content-Type: application/json" -X PUT -b cookie-jar https://info3103.cs.unb.ca:1503/users/USER_IDENTIFIER/files/FILE_ID -d '{"name": "fdsagsdf"}' -v -k
"""

from flask import send_file, request, Response
from flask_restful import Resource

from util.decorators import conceal_error_message, verify_file_access_authorization
from util.responses import ERROR_400, OK_204, ERROR_409


class FileManager(Resource):
    @conceal_error_message
    @verify_file_access_authorization
    def get(self, user_identifier=None, file_id=None, authorized_file=None):
        """
        Initiate a download for a given file.
        """

        return send_file(authorized_file.path, attachment_filename=authorized_file.name)

    @conceal_error_message
    @verify_file_access_authorization
    def delete(self, user_identifier=None, file_id=None, authorized_file=None):
        """
        Delete a given file.
        """

        authorized_file.delete()
        return OK_204

    @conceal_error_message
    @verify_file_access_authorization
    def put(self, user_identifier=None, file_id=None, authorized_file=None):
        """
        Rename a given file.
        """

        if not request.json or 'name' not in request.json:
            return ERROR_400

        try:
            authorized_file.name = request.json['name']
            authorized_file.save()
        except FileExistsError:
            return ERROR_409

        return Response(authorized_file.json, 200, mimetype='application/json')
