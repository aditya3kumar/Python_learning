from database.connection import db_connect
from database.create_tbl import db_createtbl,db_create_validate
from database.delete import db_delete,db_delete_validate
from database.insert import db_insert,db_insert_validate
from database.select import db_select
from database.update import db_update,db_update_validate


print('--result--')

connection=db_connect()

# # creating table and validate creation of table
validate_create=db_createtbl(connection)
db_create_validate(validate_create)
#
 # inserting records and validate insertion of records
#
insert_val = db_insert(connection)
db_insert_validate(insert_val)
#
# # update records and validate update of records
#
update_val=db_update(connection)
db_update_validate(update_val)
#
# # Select records
db_select(connection)
# # delete records and validate it
#
# delete_val=db_delete(connection)
# db_delete_validate(delete_val)

# drop table and validate it

# connection close
connection.close()
print('--end--')
