from flask import Flask, request

from database.models.user import User

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/users/by_username/<username>')
def users_by_username(username):
    try:
        user = User.get_by_username(username)
        if user is None:
            return '500'
        return user.json
    except ValueError:
        return '400'
    except LookupError:
        return '404'


@app.route('/users/by_id/<user_id>')
def users_by_id(user_id):
    try:
        user = User.get_by_id(user_id)
        if user is None:
            return '500'

        return user.json
    except ValueError:
        return '400'
    except LookupError:
        return '404'


# Just for example and testing.
@app.route('/users/create/<user_id>')
def users_create(user_id):
    name = request.args.get('name')
    email = request.args.get('email')

    try:
        x = User(None, user_id, name, email)
        return str(x.save())
    except ValueError:
        return '400'
    except NameError:
        return '409'


if __name__ == '__main__':
    app.run()
