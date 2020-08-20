import logging

import pymysql
from database.connection import db_connect

def db_insert(db):
    try:
        cursor=db.cursor()
        insert_tbl='''INSERT INTO `tbl_employee1` (`NAME`, `DEPT`, `STATUS`) VALUES ('test2', 'IT', 'INACTIVE')'''
        insert_val=cursor.execute(insert_tbl)
        db.commit()

        return insert_val
    except pymysql.err.OperationalError as err:
        print('operational error :',err)
        exit(0)
    except Exception as error:
        logging.warning('DB exception: %s' % error)

def db_insert_validate(insert_val):
    if insert_val > 0:
        print("total no. of Record inserted:",insert_val)
    elif insert_val==None:
        print("None query executed")

    else:
        print("There are no results for this query")







