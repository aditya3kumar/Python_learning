import pymysql

#database connection
connection = pymysql.connect(host="localhost", user="root", passwd="", database="test")
cursor = connection.cursor()
create_tbl= "create table artists "
cursor.execute(create_tbl)



#commiting the connection then closing it.
connection.commit()
connection.close()
print("end");
print("hello")
    
        
    