from flask import Flask

from blueprints.register import register_all_blueprints
from database import RecordNotFoundError
from database.models.user import User

app = Flask(__name__)
register_all_blueprints(app)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/get_user_by_id')
def get_user_by_id():
    try:
        return User().columns
    except RecordNotFoundError as err:
        return str(err)


if __name__ == '__main__':
    app.run()
