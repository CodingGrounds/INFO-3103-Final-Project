from flask import Flask

from blueprints.register import register_all_blueprints

app = Flask(__name__)
register_all_blueprints(app)


@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run()
