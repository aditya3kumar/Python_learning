import pymysql
import pymysql.cursors

#database connection
def db_connect():

    db = pymysql.connect(host="localhost", user="root", passwd="", database="test")

    return db






