import pymysql
from database.connection import db_connect

def db_insert(db):
    cursor=db.cursor()
    insert_tbl='''INSERT INTO `tbl_employee1` (`NAME`, `DEPT`, `STATUS`) VALUES ('test2', 'IT', 'INACTIVE')'''
    insert_val=cursor.execute(insert_tbl)
    db.commit()
    return insert_val


def db_insert_validate(insert_val):
    if insert_val > 0:
        print("total no. of Record inserted:",insert_val)
    elif insert_val==None:
        print("None query executed")

    else:
        print("There are no results for this query")







