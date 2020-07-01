import pymysql
from database.select import db_select
from database.connection import db_connect

print('result')
a=db_select()
print(a)
