import click
from flask import Blueprint

users_bp = Blueprint('users', __name__)


@users_bp.cli.command('create')
@click.argument('login_name', required=True)
def create(login_name):
    """ Creates a user """
    print("Create user: {}".format(login_name))


