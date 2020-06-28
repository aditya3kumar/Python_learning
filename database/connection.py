import pymysql

#database connection
connection = pymysql.connect(host="localhost", user="root", passwd="", database="test")
cursor = connection.cursor()
select_tbl= "select * from tbl_employee "
cursor.execute(select_tbl)



#commiting the connection then closing it.
connection.commit()
connection.close()
print("end");
print("hello")
