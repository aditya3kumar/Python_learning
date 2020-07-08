from time import sleep

import pymysql
import pymysql.cursors

from database.connection import db_connect

def db_select(db):
    cursor=db.cursor()


    PostgreSQL_select_Query = """select column_name from information_schema.columns where table_name = 'tbl_employee1' """
    cursor.execute(PostgreSQL_select_Query)
    column_name=list(cursor.fetchall())
    print(column_name)

    select_tbl = "select * from tbl_employee1"
    cursor.execute(select_tbl)
    name=cursor.execute(select_tbl)
    rows=cursor.fetchall()

    data=[]
    for eachRow in rows:

        data.append(eachRow)
    print(data)

