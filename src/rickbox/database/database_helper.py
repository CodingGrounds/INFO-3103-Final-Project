"""
Database wrapper for MySQL and MariaDB databases.

Usage:

The constructor for the database helper takes in a host, username, password,
and database name. These are optional and if not provided, the helper will use
the values stored in the database config file.

This database helper takes advantage of the `with` pattern.
Transactions will automatically commit when the with block is exited.

Example:
```
with DatabaseHelper() as database:
    database.execute('SELECT * FROM users')
    database.execute('INSERT into users(name, email) VALUES (%s, %s)', ('John Doe', 'john.doe@example.com'))
```

Select statements require two steps to complete.
The select query must be executed and then the results fetched.

Example:
```
with DatabaseHelper() as database:
    database.execute('SELECT * FROM users')
    results = database.fetchone();
    results = database.fetchall();
```

All queries should be properly parameterized.

Example:
```
with DatabaseHelper() as database:
    database.execute('INSERT INTO users (name, email) VALUES (%s, %s)', ('John Doe', 'john.doe@example.com'))
```
"""

import pymysql

from database_config import MYSQL_HOST, MYSQL_USER, MYSQL_PASS, MYSQL_DB


class DatabaseHelper:

    def __init__(self, host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASS, db=MYSQL_DB):
        """
        Create a connection to the database with the given attributes

        :param host: address of the database to connect to
        :param user: username to connect to the database with
        :param password: password to authenticate the user
        :param db: name of the database to use
        """
        self._connection = pymysql.connect(host=host, user=user, password=password, db=db)
        self._cursor = self._connection.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Commit all transactions and close the database connection"""
        self.commit()
        self._connection.close()

    @property
    def connection(self):
        return self._connection

    @property
    def cursor(self):
        return self._cursor

    def commit(self):
        """Commit any pending transactions to the database"""
        self._connection.commit()

    def execute(self, query, params=None):
        """
        Execute an sql query against the database with optional parameters.

        :param query: query to execute
        :param params: optional parameters to pass with the query
        """
        self._cursor.execute(query=query, args=params or ())
        return self

    def fetchall(self):
        return self._cursor.fetchall()

    def fetchone(self):
        return self._cursor.fetchone()


if __name__ == '__main__':
    with DatabaseHelper() as database:
        database.execute('create table if not exists test_table (name varchar(20), email varchar(50))')
        print(database.execute('show databases').fetchall())
        print(database.execute('show tables').fetchall())
        database.execute('insert into test_table (name, email) values ("test", "test@example.com")')
        print(database.execute('select * from test_table').fetchall())
