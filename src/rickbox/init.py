#!/Users/aj/work/unb/info3103/project_backend/venv/bin/python
from database.database_helper import DatabaseHelper

if __name__ == '__main__':
    with DatabaseHelper() as database:
        database.execute('DROP DATABASE IF EXISTS `skydrive`')
