import re
import warnings
import click
import pymysql
from flask import Blueprint
from database import DatabaseHelper
from database.sql.procs import get_all_procs
from database.sql.schema import get_all_schemas

db_bp = Blueprint('db', __name__)


@db_bp.cli.command('init')
def init():
    """ Initializes the database tables, stored procedures, associations, etc. """
    print('Loading schemas...')
    for query_set in [get_all_schemas(), get_all_procs()]:
        for key in query_set.keys():
            print(f'Creating {key}...')
            print(query_set[key])
            queries = str(query_set[key])
            queries = re.sub(r'(\n| )+', ' ', queries)
            queries = queries.split(';')
            queries = [query for query in list(map(str.strip, queries)) if len(query) > 0]
            for query in queries:
                print('lenquery:\t', len(query))
                def operation():
                    with DatabaseHelper() as db:
                        db.execute(query)

                handle_warnings(operation, key)
    print('Done!')


@db_bp.cli.command('drop')
@click.option('--force', is_flag=True, help='This is a safety mechanism')
@click.option('--db', required=True, help='The name of the database to drop')
def drop(force, db):
    """ Drops the database. Be careful. """
    if not force:
        print('The --force flag was not passed. No action taken')
        return
    make_or_drop(db, 'drop')


@db_bp.cli.command('make')
@click.option('--db', required=True, help='The name of the database to drop')
def make(db):
    """ Creates a new database. """
    make_or_drop(db, 'make')


def handle_warnings(fn, entity_name):
    warnings.filterwarnings('error')
    try:
        fn()
    except pymysql.err.Warning as err:
        if err.args[0] == 1008:  # can't drop database; database does not exist
            print(f'Unable to drop database {entity_name} because database does not exist')
        elif err.args[0] == 1007:  # can't create database; database already exists
            print(f'Unable to create database {entity_name} because database already exists')
    except pymysql.err.InternalError as err:
        if err.args[0] == 1050:  # can't create table; table already exists
            print(f'Unable to create table {entity_name} because table already exists')
        else:
            print(err)
    warnings.filterwarnings('default')


def make_or_drop(db, action):
    """ Common function to make or drop arrays. Used by make and drop """
    if len(db) == 0:
        print('Error: --db option requires an argument')
        return

    def operation():
        with DatabaseHelper(db=None) as helper:
            if action == 'make':
                helper.execute(f'CREATE DATABASE IF NOT EXISTS {db};')
                print(f'Database {db} created')
            elif action == 'drop':
                helper.execute(f'DROP DATABASE IF EXISTS {db};')
                print(f'Database {db} dropped')

    handle_warnings(operation, db)
