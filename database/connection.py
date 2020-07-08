import pymysql
import pymysql.cursors
import cx_Oracle

#database connection
def db_connect():

    db = pymysql.connect(host="127.0.0.1", port=3306,user="root",password="",database="test")
    #db =cx_Oracle.connect('scott/tiger@localhost')
    if (db):
        print("Connection established:",db)
        print(db.host)
    else:
        print ("Connection not estblished")

    print("----connection-------")
    return db






