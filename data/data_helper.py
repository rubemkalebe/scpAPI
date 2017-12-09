DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = 'root'
DB_NAME = 'scp'
DB_CHARSET = 'utf8mb4'

import pymysql.cursors


def create_connection():
    return pymysql.connect(
        host = DB_HOST,
        user = DB_USER,
        password = DB_PASSWORD,
        db = DB_NAME,
        charset = DB_CHARSET,
        cursorclass = pymysql.cursors.DictCursor
    )

