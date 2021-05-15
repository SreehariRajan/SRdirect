import os
import mysql.connector
from mysql.connector import Error
def namesorting1(c):
    connection = mysql.connector.connect(host='localhost',user='admin',password='root',database='studentdirectory')
    cursor = connection.cursor()
    query=("select * from students where std='{}' and division='{}' and name like "+str(c)+" order by roll").format(xx,yy)
    cursor.execute(query)
    global result1
    result1=cursor.fetchall()
    connection.commit()
    connection.close()
    cursor.close()
def namesorting11(c):
    connection = mysql.connector.connect(host='localhost',user='admin',password='root',database='studentdirectory')
    cursor = connection.cursor()
    query='select * from studentsdeleted where name like '+str(c)+' order by admissionnumber'
    cursor.execute(query)
    global result1500
    result1500=cursor.fetchall()
    connection.commit()
    connection.close()
    cursor.close()
def namesorting1school(c):
    connection = mysql.connector.connect(host='localhost',user='admin',password='root',database='studentdirectory')
    cursor = connection.cursor()
    query=("select * from students where name like "+str(c)+" order by admissionnumber")
    cursor.execute(query)
    global result1school
    result1school=cursor.fetchall()
    connection.commit()
    connection.close()
    cursor.close()
def view03school():
    connection = mysql.connector.connect(host='localhost',user='admin',password='root',database='studentdirectory')
    cursor = connection.cursor() 
    sql_fetch_blob_query = "SELECT * from students order by admissionnumber"
    cursor.execute(sql_fetch_blob_query)
    global resultschool
    resultschool=cursor.fetchall()
    cursor.close()
    connection.close()
def view033(x,y):
    global xx,yy
    xx=x
    yy=y
    connection = mysql.connector.connect(host='localhost',user='admin',password='root',database='studentdirectory')
    cursor = connection.cursor() 
    sql_fetch_blob_query = ("SELECT * from students where std='{}' and division='{}' order by roll".format(x,y))
    cursor.execute(sql_fetch_blob_query)
    global result
    result=cursor.fetchall()
    cursor.close()
    connection.close()
def view0333():
    connection = mysql.connector.connect(host='localhost',user='admin',password='root',database='studentdirectory')
    cursor = connection.cursor() 
    sql_fetch_blob_query = ("SELECT * from studentsdeleted order by admissionnumber")
    cursor.execute(sql_fetch_blob_query)
    global result500
    result500=cursor.fetchall()
    cursor.close()
    connection.close()
def readBlobData(admissionnumber):
    try:
        connection = mysql.connector.connect(host='localhost',user='admin',password='root',database='studentdirectory')
        cursor = connection.cursor()
        sql_fetch_blob_query = ("SELECT * from students where admissionnumber='{}'".format(admissionnumber))
        cursor.execute(sql_fetch_blob_query)
        record = cursor.fetchall()
        for row in record:
            global admis
            global r
            global n
            global dob
            global c
            global d
            global cteach
            global po
            global pe
            global e
            global a            
            admis=row[0]
            po=row[1]
            n=row[2]
            dob=row[3]
            c=row[4]
            cteach=row[5]
            d=row[6]
            r=row[7]
            pe=row[8]
            e=row[9]
            a=row[10]
        cursor.close()
    except Error as error:
        pass
    finally:
        if (connection):
             connection.close()
def disabletest234():
    connection = mysql.connector.connect(host='localhost',user='admin',password='root')
    cursor=connection.cursor()
    query="""show databases"""
    cursor.execute(query)
    x2=cursor.fetchall()
    cursor.close()
    connection.close()
    if ('studentdirectory',) in x2:
        connection = mysql.connector.connect(host='localhost',user='admin',password='root',database='studentdirectory')
        cursor=connection.cursor()
        query="""show tables"""
        cursor.execute(query)
        x=cursor.fetchall()
        connection.commit()
        t=[]
        for i in x:
                f=i[0]
                t.append(f)
        if len(t)>2:
            query="select * from studentsdeleted"
            cursor.execute(query)
            x1=cursor.fetchall()
            if len(x1)==0:
                return True
            else:
                return False
        else:
            return True
        cursor.close()
        connection.close()
    else:
        return True
def disabletest():
    connection = mysql.connector.connect(host='localhost',user='admin',password='root')
    cursor=connection.cursor()
    query="""show databases"""
    cursor.execute(query)
    x2=cursor.fetchall()
    cursor.close()
    connection.close()
    if ('studentdirectory',) in x2:
        connection = mysql.connector.connect(host='localhost',user='admin',password='root',database='studentdirectory')
        cursor=connection.cursor()
        query="""show tables"""
        cursor.execute(query)
        x=cursor.fetchall()
        connection.commit()
        t=[]
        for i in x:
                f=i[0]
                t.append(f)
        if len(t)>1:
            query="select * from students"
            cursor.execute(query)
            x1=cursor.fetchall()
            if len(x1)==0:
                return True
            else:
                return False
        else:
            return True
        cursor.close()
        connection.close()
    else:
        return True

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
    cursor.close()
    connection.close()
def classtest(c):
    connection = mysql.connector.connect(host='localhost',user='admin',password='root',database='studentdirectory')
    cursor=connection.cursor()
    query="""select std from students"""
    cursor.execute(query)
    record=cursor.fetchall()
    global l11
    l11=[]
    for row in record:
         l11.append(row)    
    tu=(c,)
    if tu in l11:
        cursor.close()
        connection.close()
        return True        
    else:
        cursor.close()
        connection.close()
        return False    
def classdivtest(c,d):
    connection = mysql.connector.connect(host='localhost',user='admin',password='root',database='studentdirectory')
    cursor=connection.cursor()
    query="""select std,division from students"""
    cursor.execute(query)
    record=cursor.fetchall()
    view033(c,d)
    global l1
    l1=[]
    for row in record:
         l1.append(row) 
    tu=(str(c),str(d))
    if tu in l1:
        
        return True
        cursor.close()
        connection.close()
    else:
        
        return False
        cursor.close()
        connection.close()
def adidtest(p):
    connection = mysql.connector.connect(host='localhost',user='admin',password='root',database='studentdirectory')
    cursor=connection.cursor()
    query="""select admissionnumber from students"""
    cursor.execute(query)
    record=cursor.fetchall()
    l2=[]
    for row in record:
      l2.append(row)
    x=(p,)
    cursor.close()
    connection.close()
    if x in l2:
        return True
    else:
        return False
    
def classstudent(stdd,divisionn,r):
    connection = mysql.connector.connect(host='localhost',user='admin',password='root',database='studentdirectory')
    cursor=connection.cursor()
    query="""select roll from students where std='{}' and division='{}'""".format(stdd,divisionn)
    cursor.execute(query)
    record=cursor.fetchall()
    l3=[]
    cursor.close()
    connection.close()
    connection = mysql.connector.connect(host='localhost',user='admin',password='root',database='studentdirectory')
    cursor=connection.cursor()
    query="""select admissionnumber from students where std='{}' and division='{}' and roll={}""".format(stdd,divisionn,r)
    cursor.execute(query)
    record1=cursor.fetchall()
    cursor.close()
    connection.close()
    for row1 in record1:
        for x in row1:
            global zzz
            zzz=x
    
    for row in record:
        l3.append(row)
    y=(r,)
    if y in l3:
        return True
    else:
        return False
def adidforpromote(c):
    connection = mysql.connector.connect(host='localhost',user='admin',password='root',database='studentdirectory')
    cursor = connection.cursor() 
    sql_fetch_blob_query = ("SELECT admissionnumber from students where std='{}'".format(c))
    cursor.execute(sql_fetch_blob_query)
    result111=cursor.fetchall()
    global result11
    result11=[]
    for i in result111:
            ff=i[0]
            result11.append(ff)
    cursor.close()
    connection.close()    
def forpromoting(c):
    connection = mysql.connector.connect(host='localhost',user='admin',password='root',database='studentdirectory')
    cursor = connection.cursor() 
    sql_fetch_blob_query ="SELECT admissionnumber,name,photo,std,division,roll from students where std='{}' order by division,roll".format(c)
    cursor.execute(sql_fetch_blob_query)
    global result10
    result10=cursor.fetchall()
    cursor.close()
    connection.close()
    adidforpromote(c)
def modtestt(c,d):
    global amod,bmod
    amod=c
    bmod=d
