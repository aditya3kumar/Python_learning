from time import sleep

import pymysql
from database.connection import db_connect

def db_createtbl(db):
    cursor=db.cursor()


    studentRecord = """CREATE TABLE tbl_employee1(  
                   ID INT  NOT NULL,
                   NAME  VARCHAR(20) NOT NULL,  
                   Dept VARCHAR(50),  
                   login VARCHAR(50), 
                   status VARCHAR(5))"""


    validate_create=cursor.execute(studentRecord)
    db_connect().commit()

    print(validate_create)
    if validate_create==0 or validate_create==None :
        print("Table not created")
    else:
        print("Table created")

    print("----createtbl end---------")
    return
