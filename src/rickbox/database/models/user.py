import pymysql
from database import RecordNotFoundError, get_columns, ColumnNotSearchableError
from database.database_helper import DatabaseHelper
from database.models.base import BaseModel


class User(BaseModel):

    def __init__(self, username=None, root_folder_id=None, login_name=None, display_name=None):
        super()
        return

    @property
    def table_name(self):
        return 'users'

