import pymysql
from database.select import db_select
from database.connection import db_connect
from database.update import db_update
from database.create_tbl import db_createtbl
from database.insert import db_insert
from database.delete import db_delete

#CHANGE MASTER TO MASTER_HOST='127.0.0.1', MASTER_PORT=3306,MASTER_USER='aditya', MASTER_PASSWORD='aditya'

print('result')
# a=db_select()
# print(a)
# b=db_update()
# print(b)
# connection and validate
db=db_connect()
# db_createtbl() and validate creation of table
db_createtbl(db)
# insert recrods and validate insertion of records

db_insert(db)
# updated records and validate update of records
db_update(db)
# delete records and validate it

# drop table and validate it
db_delete(db)


print('test')
