import pymysql
from database.connection import db_connect


def db_update(db):
    cursor=db.cursor()
    update_tbl="Update tbl_employee1 set NAME ='test21' where ID = 1"
    update_val=cursor.execute(update_tbl)
    db.commit()
    return update_val


def db_update_validate(update_val):
    if update_val>0:
        print("Record updated:",update_val)
    else:
        print("Record not updated")



