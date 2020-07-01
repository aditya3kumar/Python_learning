from time import sleep

import pymysql
import pymysql.cursors

from database.connection import db_connect

def db_select():
    cursor=db_connect().cursor()

    select_tbl= "select * from tbl_employee"
    cursor.execute(select_tbl)
    rows=cursor.fetchall()

    data=[]
    for eachRow in rows:

        data.append(eachRow)

    return data
