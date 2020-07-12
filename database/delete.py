import pymysql
from database.connection import db_connect

def db_delete(db):
    cursor=db.cursor()
    delete_tbl="delete from tbl_employee1 where Status= 'Inactive';"
    delete_val= cursor.execute(delete_tbl)
    db.commit()
    return delete_val


def db_delete_validate(delete_val):
    if delete_val >0:
        print("Total Record deleted:",delete_val)
    else:
        print("Record not deleted")












