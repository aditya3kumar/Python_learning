import pymysql
import pymysql.cursors

from database.connection import db_connect



def db_select():
    print(db_connect())
    print('tes')

    select_tbl= "select * from tbl_employee"
    db_connect().cursor.execute(select_tbl)
    result=db_connect().cursor.fetchall(select_tbl)
    for eachRow in result:
        print(eachRow)
    db_connect().connection.commit()

    return result

print(db_select())