import pymysql
from database.select import db_select
from database.connection import db_connect
from database.update import db_update
from database.create_tbl import db_createtbl
from database.insert import db_insert
from database.delete import db_delete

#CHANGE MASTER TO MASTER_HOST='127.0.0.1', MASTER_PORT=3306,MASTER_USER='aditya', MASTER_PASSWORD='aditya'

print('--result--')
# a=db_select()
# print(a)
# b=db_update()
# print(b)
# connection and validate
connection=db_connect()
# db_createtbl() and validate creation of table
db_createtbl(connection)

# insert records and validate insertion of records

db_insert(connection)
# Select records
db_select(connection)

# update records and validate update of records

db_update(connection)

# Select records
db_select(connection)
# delete records and validate it
db_delete(connection)
# drop table and validate it

# connection close
connection.close()
print('--end--')
