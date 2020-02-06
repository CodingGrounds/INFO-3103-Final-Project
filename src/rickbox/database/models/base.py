from abc import ABC

import pymysql

from database import get_columns, DatabaseHelper, RecordNotFoundError, ColumnNotSearchableError


class BaseModel(ABC):

    @staticmethod
    def get_row_by_id(self, find_id):
        response = None
        if find_id is None:
            raise ValueError('`id` is a required parameter.')

        if isinstance(find_id, int):
            find_id = [find_id]

        try:
            with DatabaseHelper() as database:
                response = database.cursor.callproc('get_row_by_id', find_id)
        except pymysql.err.InternalError as err:
            if err[0] == 1305:  # procedure does not exist
                response = 'Procedure does not exist'

        if response is None:
            raise RecordNotFoundError(f'No #{self.__class__.__name} with that ID has been found.')
        return response

    def __get_by_column_value__(self, column, value):
        if column not in self.columns:
            raise ColumnNotSearchableError(
                f'The column `{column}` is not unique and therefore not valid for finding users.')

    @property
    def columns(self):
        response = None
        try:
            with DatabaseHelper() as database:
                response = database.cursor.callproc('get_columns_for_table', self.table_name)
        except pymysql.err.InternalError as err:
            print()
            if type(err).__name__ == 1305:  # procedure does not exist
                response = 'Procedure does not exist'
            else:
                raise err
        return response

    @property
    def table_name(self):
        raise NotImplementedError('Must be implemented by child classes')
