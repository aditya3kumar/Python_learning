import pymysql
from database.connection import db_connect

def db_delete(db):
    cursor=db.cursor()
    delete_tbl='''drop table tbl_employee1'''
    delete_val= cursor.execute(delete_tbl)
    if delete_val >0:
        print("Record deleted")
    else:
        print("Record not deleted")

    print("-------drop table end---")








