import os
import mysql.connector
from mysql.connector import Error


        
    
def readBlobData(admissionnumber):
    try:
        connection = mysql.connector.connect(host='localhost',user='admin',password='root',database='studentdirectory')
        cursor = connection.cursor()
        print("Connected")
        
        sql_fetch_blob_query = ("SELECT * from students where admissionnumber='{}'".format(admissionnumber))
        cursor.execute(sql_fetch_blob_query)
        record = cursor.fetchall()
        for row in record:
            global admis
            global r
            global n
            global c
            global d
            global cteach
            global po
            global pe
            global e
            global a
            global dob
            
            admis=row[0]
            r=row[1]
            n=row[2]
            dob=row[3]
            c=row[4]
            d=row[5]
            cteach=row[6]
            po=row[7]
            pe=row[8]
            e=row[9]
            a=row[10]
            resumeFile = row[7]
            h=os.getcwd()
            print("Storing employee image and resume on disk \n")
            global photoPath
            photoPath = h+"\\output\\" +str(r)+ ".jpg"
            writeTofile(po, photoPath)
            resize(photoPath)
        cursor.close()
        

    except Error as error:
        print("Failed to read blob data from sqlite table", error)
    
    finally:
        if (connection):
             connection.close()
             print(" connection is closed")
        return t

def rtest():
    connection = mysql.connector.connect(host='localhost',user='admin',password='root',database='studentdirectory')
    cursor=connection.cursor()
    query="""select admissionnumber from students"""
    cursor.execute(query)
    x=cursor.fetchall()
    global t
    t=[]
    for i in x:
            f=i[0]
            t.append(f)
    return t
