from flask import Flask
from flask_restful import Api
from flask_session import Session

import app_config
from resources.file_manager import FileManager
from resources.file_collection_manager import FileCollectionManager
from resources.user_manager import UserManager
from resources.session_manager import SessionManager
from util.responses import json_response

app = Flask(__name__)

# required for sessions. unrelated to https
app.secret_key = app_config.APP_SECRET_KEY
app.config['SESSION_TYPE'] = app_config.SESSION_TYPE
app.config['SESSION_COOKIE_NAME'] = app_config.SESSION_COOKIE_NAME
app.config['SESSION_COOKIE_DOMAIN'] = app_config.SESSION_COOKIE_DOMAIN
Session(app)
api = Api(app)

api.add_resource(SessionManager, '/login')
api.add_resource(UserManager, '/users/<user_identifier>')
api.add_resource(FileCollectionManager, '/users/<user_identifier>/files')
api.add_resource(FileManager, '/users/<user_identifier>/files/<file_id>')


@app.route('/users', strict_slashes=False)
def users_list():
    response_body = {'message': 'Listing users is not enabled.'}
    return json_response(response_body, 200)


if __name__ == '__main__':
    app.run(
        host=app_config.APP_HOST,
        port=app_config.APP_PORT,
        debug=app_config.APP_DEBUG
    )
