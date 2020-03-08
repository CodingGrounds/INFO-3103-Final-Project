import json

from flask import Flask, request, Response, session
from flask_restful import Api
from flask_session import Session

import app_config
from database.models.user import User
from resources.user_session import UserSession
from resources.user_manager import UserManager

app = Flask(__name__)

# required for sessions. unrelated to https
app.secret_key = app_config.APP_SECRET_KEY
app.config['SESSION_TYPE'] = app_config.SESSION_TYPE
app.config['SESSION_COOKIE_NAME'] = app_config.SESSION_COOKIE_NAME
app.config['SESSION_COOKIE_DOMAIN'] = app_config.SESSION_COOKIE_DOMAIN
Session(app)
api = Api(app)

api.add_resource(UserSession, '/login')
api.add_resource(UserManager, '/users/<user_identifier>')


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/users', strict_slashes=False)
def users_list():
    response_body = {'message': 'Listing users is not enabled.'}
    return Response(json.dumps(response_body), 200)


if __name__ == '__main__':
    app.run(
        host=app_config.APP_HOST,
        port=app_config.APP_PORT,
        debug=app_config.APP_DEBUG
    )
