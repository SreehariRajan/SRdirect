import mysql.connector
from mysql.connector import Error
connection = mysql.connector.connect(host='localhost',user='admin',password='root',database='studentdirectory')
cursor=connection.cursor()
cursor.execute("SHOW TABLES")
global tables
tables=cursor.fetchall()
print(tables)
for i in tables:
    print(i)
connection.commit()
connection.close()
def add(admissionnumber,r,n,dob,c,d,cteacher,po,pe,e,a):
    
    def convertToBinaryData(filename):
    # Convert digital data to binary format
        with open(filename, 'rb') as file:
            binaryData = file.read()
        return binaryData


    def insertBLOB(admissionnumber,r,n,dob,c,d,cteacher,po,pe,e,a):#blob stmt
        try:
            connection = mysql.connector.connect(host='localhost',user='admin',password='root',database='studentdirectory')
            cursor=connection.cursor()
            Picture=convertToBinaryData(po)
            query= "INSERT INTO students(admissionnumber,roll,name,dateob,std,division,classteacher,photo,phone,email,address) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                
            insert_blob_tuple=(admissionnumber,r,n,dob,c,d,cteacher,Picture,pe,e,a)
                # Convert data into tuple format

            result = cursor.execute(query, insert_blob_tuple)
                            
            connection.commit()
            print("Image and file inserted successfully as a BLOB into students")
        except mysql.connector.Error as error:
                
                
            print("Failed inserting BLOB data into MySQL table {}".format(error))
            print("------------------")
                
        finally:
            if (connection.is_connected()):
                cursor.close()
                connection.close()
                print("MySQL connection is closed")
    xyz=['students']
    xyz=tuple(xyz)
    if xyz in tables:
        print("hiiiiii")
        insertBLOB(admissionnumber,r,n,dob,c,d,cteacher,po,pe,e,a)
    elif xyz not in tables:
        print("nama")
        try:
            connection = mysql.connector.connect(host='localhost',user='admin',password='root',database='studentdirectory')
            cursor=connection.cursor()
            query="CREATE TABLE students(admissionnumber char(4) primary key not null,roll int not null,name varchar(100) not null,dateob varchar(10) not null,std int not null,division char(1) not null,classteacher varchar(100) not null,photo longblob,phone varchar(12) not null,email varchar(1000),address varchar(1000) not null)"
            cursor.execute(query)
            connection.commit()
            insertBLOB(admissionnumber,r,n,dob,c,d,cteacher,po,pe,e,a)
        except mysql.connector.Error as error:
                
                
            print("Failed inserting BLOB data into MySQL table {}".format(error))
            print("------------------")
def deletedetails(cwd,ROLLNO):
    try:
        connection = mysql.connector.connect(host='localhost',user='admin',password='root',database='studentdirectory')
        cursor=connection.cursor()
        cursor.execute("SELECT * FROM "+cwd+" where roll={}".format(ROLLNO))
        result2=cursor.fetchall()
            
        query= "DELETE FROM "+cwd+" WHERE roll={}".format(ROLLNO)
        # Convert data into tuple format
        result = cursor.execute(query)
        connection.commit()
            
            
        print(" deleted successfully")
    except mysql.connector.Error as error:
        print("Failed inserting BLOB data into MySQL table {}".format(error))
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
