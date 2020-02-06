from database.database_helper import DatabaseHelper


class RecordNotFoundError(Exception):
    pass


class ColumnNotFoundError(Exception):
    pass


class ColumnNotSearchableError(Exception):
    pass


def get_columns(table):
    if table is None:
        raise ValueError("table must be specified")

    with DatabaseHelper() as db:
        return db.cursor.callproc('get_columns_for_table', table)