import glob
import os

from database.database_helper import DatabaseHelper


if __name__ == '__main__':
    sql = "DROP DATABASE IF EXISTS skydrive;"
    sql += "CREATE DATABASE skydrive;"

    print(sql)
