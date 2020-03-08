"""
Wrapper for user session logic (log in, log out, check-if-logged-in)

Code-centric usage is all handled automatically by Flask-Session.

CLI Usage (with app running on info3103:1503):
    Log in:
        curl -i -H "Content-Type: application/json" -X POST -d '{"username": "jsmith123", "password": "secret"}' -c cookie-jar http://info3103.cs.unb.ca:1503/login

    Log out:
        curl -i -H "Content-Type: application/json" -X DELETE -b cookie-jar http://info3103.cs.unb.ca:1503/login

    Check if logged in:
        curl -i -H "Content-Type: application/json" -X GET -b cookie-jar http://info3103.cs.unb.ca:1503/login
"""

from flask import request, session
from flask_restful import Resource

from database.models.user import User
from ldap.ldap_helper import LdapHelper
from util.decorators import conceal_error_message, require_session
from util.responses import ERROR_400, json_response


class UserSession(Resource):

    @conceal_error_message
    def post(self):
        # Log in handler
        if not request.json \
                or 'username' not in request.json \
                or 'password' not in request.json:
            return ERROR_400

        username = request.json['username']
        with LdapHelper() as ldap:
            result = ldap.authenticate(username, request.json['password'])

        status_code = result[0]
        response_body = {'message': result[1]}

        if status_code == 201:
            # auto-generate User records for first-time logins
            if User.username_available(username):
                User(username=username).save()
            user_record = User.get_by_username(username)
            session['username'] = username
            session['user_id'] = user_record.id

        return json_response(response_body, status_code)

    @conceal_error_message
    @require_session
    def get(self):
        response_body = {'message': 'OK', 'username': session.get('username')}
        return json_response(response_body, 200)

    @conceal_error_message
    def delete(self):
        try:
            session.pop('username')
        except KeyError:
            pass
        return json_response({'message': 'OK'}, 204)
