import pymysql

#database connection
connection = pymysql.connect(host="localhost", user="root", passwd="", database="test")
cursor = connection.cursor()




Drop_tbl = "Drop table IF EXISTS Artists "
cursor.execute(Drop_tbl )



#commiting the connection then closing it.
connection.commit()
connection.close()
print("end");
    
        
    