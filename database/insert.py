import pymysql
from database.connection import db_connect

def db_insert(db):
    cursor=db.cursor()
    insert_tbl='''INSERT INTO `tbl_employee1` (`ID`,`NAME`, `DEPT`, `STATUS`) VALUES ('3', 'test2', 'IT', 'INACTIVE')'''
    print(insert_tbl)
    b=cursor.execute(insert_tbl)
    db_connect().commit()
    print(b)
    if b > 0:
        rs = cursor.fetchall()
        print(rs)
        print("Record inserted")
    elif    b==None:
        print("None query executed")

    else:
        print("There are no results for this query")


    print("---insert end---")




