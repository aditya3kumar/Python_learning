import pymysql
from database.connection import db_connect


def db_update(db):
    cursor=db.cursor()
    update_tbl="Update tbl_employee1 set NAME ='test21' where ID = 1"
    update_val=cursor.execute(update_tbl)

    if update_val>1:
        print("Record updated")
    else:
        print("Record not updated")

    print("---update end----")

