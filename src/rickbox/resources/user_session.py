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

import json
from flask import Response, request, session
from flask_restful import Resource

from util.decorators import conceal_error_message, require_session
from ldap.ldap_helper import LdapHelper
from database.models.user import User


class UserSession(Resource):

    @conceal_error_message
    def post(self):
        # Log in handler
        if not request.json \
                or 'username' not in request.json \
                or 'password' not in request.json:
            return Response(json.dumps({'message': 'Bad request'}), 400)

        username = request.json['username']
        with LdapHelper() as ldap:
            result = ldap.authenticate(username, request.json['password'])

        status_code = result[0]
        response_body = {'message': result[1]}

        if status_code == 201:
            session['username'] = username

        # auto-generate User records for first-time logins
        if User.username_available(username):
            User(username=username).save()
        return Response(json.dumps(response_body),
                        status=status_code,
                        mimetype='application/json')

    @conceal_error_message
    @require_session
    def get(self):
        response_body = {'message': 'OK', 'username': session.get('username')}
        return Response(json.dumps(response_body), 200)

    @conceal_error_message
    def delete(self):
        try:
            session.pop('username')
        except KeyError:
            pass
        return Response(json.dumps({'message': 'OK'}), 204)
