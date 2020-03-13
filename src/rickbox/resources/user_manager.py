"""
Wrapper for user management logic (just viewing right now)

Code-centric usage is all handled automatically by Flask-Session.

CLI Usage (with app running on info3103:1503):
    View user with ID=1:
        curl -i -H "Content-Type: application/json" -X GET -b cookie-jar http://info3103.cs.unb.ca:1503/users/1
"""

from flask import Response
from flask_restful import Resource

from database.models.user import User
from util.decorators import conceal_error_message, require_session
from util.responses import ERROR_400, ERROR_404


class UserManager(Resource):

    @conceal_error_message
    @require_session
    def get(self, user_identifier):
        try:
            user = User.get(user_identifier)
        except ValueError:
            return ERROR_400
        except LookupError:
            return ERROR_404

        # user.json is already json, so json_response is not applicable
        return Response(user.json, 200)
