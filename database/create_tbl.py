from time import sleep

import pymysql
from database.connection import db_connect

EMPLOYEE_TABLE = []


def db_createtbl(db):
    cursor = db.cursor()

    EMPLOYEE_TABLE = """CREATE TABLE tbl_employee1(  
                   ID int AUTO_INCREMENT PRIMARY KEY,
                   NAME  VARCHAR(20) NOT NULL,  
                   Dept VARCHAR(50),  
                   status VARCHAR(10))"""

    validate_create = cursor.execute(EMPLOYEE_TABLE)
    db.commit()
    return validate_create

def db_create_validate(validate_create):
    if validate_create == 0 or validate_create == None:
        print("Table created")
    else:
        print("Table not created")
