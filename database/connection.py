import pymysql
import pymysql.cursors


# database connection
def db_connect():
    db = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="", database="test")
    if (db):
        print("Connection established:", db)
    else:
        print("Connection not estblished")

    print("----connection-------")
    return db
