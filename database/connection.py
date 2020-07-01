import pymysql
import pymysql.cursors

#database connection
def db_connect():

    db = pymysql.connect(host="localhost", user="root", passwd="", database="test")

    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    print('test')
    return cursor




a=db_connect()
print(a);

