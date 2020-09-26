from logging import exception

import pymysql
import pymysql.cursors


# database connection
def db_connect():
    try:
        db = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="", database="test")

    except pymysql.err.OperationalError as err:
        print('operational error :',err)
        exit(0)
    except Exception as error:
        print(error,'this error occurring')
        exit(0)
    return db

