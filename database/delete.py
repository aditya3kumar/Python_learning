import logging
from logging import exception

import pymysql
from database.connection import db_connect

def db_delete(db):
    try:
        cursor=db.cursor()
        delete_tbl="delete from tbl_employee1 where Status= 'Inactive';"
        delete_val= cursor.execute(delete_tbl)
        db.commit()
        print('delete_val')
        return delete_val


    except Exception as error:
        logging.warning('DB exception: %s' % error)

def db_delete_validate(delete_val):
    if delete_val >0 :
       print("Total Record deleted:",delete_val)
    else:
        print("Record not deleted")












