import PIL
from PIL import Image
import mysql.connector
from mysql.connector import Error
import cv2
def exstucheck():
    if databasecheck()==True:
        connection = mysql.connector.connect(host='localhost',user='admin',password='root',database='studentdirectory')
        cursor=connection.cursor()
        query="show tables"
        cursor.execute(query)
        ex=cursor.fetchall()
        if ('studentsdeleted',) in ex:
            return True
        else:
            return False
    else:
        return False
def cp(cforchanging):
    global classabove
    if cforchanging=='lkg':
        classabove='ukg'
    elif cforchanging=='ukg':
        classabove='1'
    elif cforchanging=='12':
        classabove='Eligible for higher studies'
    elif cforchanging in ['1','2','3','4','5','6','7','8','9','10','11']:
        cl=int(cforchanging)
        classabove=str(cl+1)
    else:
        classabove=None
def removeacc():
    try:
        connection = mysql.connector.connect(host='localhost',user='admin',password='root',database='studentdirectory')
        cursor=connection.cursor()   
        query= "DROP TABLE ACCOUNTINFO"
        # Convert data into tuple format
        result = cursor.execute(query)
        connection.commit()   
    except mysql.connector.Error as error:
        pass
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
def changerr(aaa,bbb):
    connection = mysql.connector.connect(host='localhost',user='admin',password='root',database='studentdirectory')
    cursor=connection.cursor()
    query= "select * from accountinfo"
    cursor.execute(query)
    resuu=cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    passss=[]
    for i in resuu:
        passss.append(i[1])
    if aaa in passss:
        return True
    else:
        return False  
def changer(aaa,bbb):
    connection = mysql.connector.connect(host='localhost',user='admin',password='root',database='studentdirectory')
    cursor=connection.cursor()
    query= "select * from accountinfo"
    cursor.execute(query)
    resuu=cursor.fetchall()
    connection.commit()
    passss=[]
    for i in resuu:
        passss.append(i[1])
    if aaa in passss:
        connection = mysql.connector.connect(host='localhost',user='admin',password='root',database='studentdirectory')
        cursor=connection.cursor()
        query= "update accountinfo set password='{}' where password='{}'".format(bbb,aaa)
        pp=cursor.execute(query)
        connection.commit()
        cursor.close()
        connection.close()
    else:
        cursor.close()
        connection.close()
       
def forgett(a):
    global forgetpcheck
    forgetpcheck=a
def forgettt(oc):
    try:
        connection = mysql.connector.connect(host='localhost',user='admin',password='root',database='studentdirectory')
        cursor=connection.cursor()
        query= "select answer from accountinfo"
        cursor.execute(query)
        resuu=cursor.fetchall()
        connection.commit()
        ans=[]
        for i in resuu:
            ans.append(i[0])
        if oc in ans:
            return True
        else:
            return False
    except mysql.connector.Error as error: 
        pass                
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
def question():
    connection = mysql.connector.connect(host='localhost',user='admin',password='root',database='studentdirectory')
    cursor=connection.cursor()
    query= "select question from accountinfo"

    cursor.execute(query)
    resuu=cursor.fetchall()
    connection.commit()
    quest=[]
    for i in resuu:
        quest.append(i[0])
    return quest
def forget(a1,a2):
    try:
        
        connection = mysql.connector.connect(host='localhost',user='admin',password='root',database='studentdirectory')
        cursor=connection.cursor()
        query= "update accountinfo set password='{}' where answer='{}'".format(a1,a2)
        pp=cursor.execute(query)
        connection.commit()
    except mysql.connector.Error as error:
        pass                
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
def checkforfirst():
    try:
        connection = mysql.connector.connect(host='localhost',user='admin',password='root',database='studentdirectory')
        cursor=connection.cursor()
        query= "select * from accountinfo"
        cursor.execute(query)
        resu=cursor.fetchall()
        connection.commit()
        global forfirst,forfirstt
        forfirstt=[]
        forfirst=[]
        for i in resu:
            forfirst.append(i[0])
        for i in resu:
            forfirstt.append(i[1])
    except mysql.connector.Error as error:
        pass                
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
def below(u,n):
    global uu,nnn
    uu=u
    nnn=n
def createaccounting(user,password,question,answer):
    try:
        connection = mysql.connector.connect(host='localhost',user='admin',password='root',database='studentdirectory')
        cursor=connection.cursor()
        query= "insert into accountinfo(user,password,question,answer) values (%s,%s,%s,%s)"
        insert_blob_tuple=(user,password,question,answer)
        resultt=cursor.execute(query,insert_blob_tuple)
        connection.commit()
    except mysql.connector.Error as error:
        pass
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
def databasecheck():
    connection = mysql.connector.connect(host='localhost',user='admin',password='root')
    cursor=connection.cursor()
    query= "SHOW DATABASES"
    result = cursor.execute(query)
    r=cursor.fetchall()
    cursor.close()
    connection.close()
    if ('studentdirectory',) in r:
        return True
    else:
        return False
def databasecheckingforadd():
    try:
        connection = mysql.connector.connect(host='localhost',user='admin',password='root')
        cursor=connection.cursor()
        query= "SHOW DATABASES"
        result = cursor.execute(query)
        r=cursor.fetchall()
        cursor.close()
        connection.close()
        if ('studentdirectory',) in r:
            connection = mysql.connector.connect(host='localhost',user='admin',password='root',database='studentdirectory')
            cursor=connection.cursor()
            cursor.execute("SHOW TABLES")
            global tables
            tables=cursor.fetchall()
            connection.commit()
            cursor.close()
            connection.close()
            return True
        else:    
            try:
                connection = mysql.connector.connect(host='localhost',user='admin',password='root')
                cursor=connection.cursor()
                query= "CREATE DATABASE studentdirectory"
                result = cursor.execute(query)
            except mysql.connector.Error as error:
                pass
            finally:
                if (connection.is_connected()):
                    cursor.close()
                    connection.close()
                    databasecheckingforadd()            
    except mysql.connector.Error as error:
            pass            
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
def add(admissionnumber,po,n,dob,c,cteacher,d,r,pe,e,a):
    def rollsorting():
        connection = mysql.connector.connect(host='localhost',user='admin',password='root',database='studentdirectory')
        cursor=connection.cursor()
        query="select admissionnumber from students where std='{}' and division='{}' order by name".format(c,d)
        cursor.execute(query)
        rolling=cursor.fetchall()
        cursor.close()
        connection.close()
        forrolling=1
        for ring in range(len(rolling)):
            rrolling=rolling[ring]
            connection = mysql.connector.connect(host='localhost',user='admin',password='root',database='studentdirectory')
            cursor=connection.cursor()
            query="update students set roll={} where admissionnumber='{}'".format(forrolling,rrolling[0])
            cursor.execute(query)
            forrolling+=1
            connection.commit()
            cursor.close()
            connection.close()   
    def convertToBinaryData(filename):
        exten=filename.split('.')
        ex=exten[-1]
                             
        im = cv2.imread(filename)
        im_resize = cv2.resize(im, (161, 192))
            
        is_success, im_buf_arr = cv2.imencode("."+ex, im_resize)
        byte_im = im_buf_arr.tobytes()
        return byte_im
    def insertBLOB(admissionnumber,po,n,dob,c,cteacher,d,r,pe,e,a):#blob stmt
        try:
            connection = mysql.connector.connect(host='localhost',user='admin',password='root',database='studentdirectory')
            cursor=connection.cursor()
            if po!="PHOTO NOT AVAILABLE":
                Picture=convertToBinaryData(po)
                query= "INSERT INTO students(admissionnumber,photo,name,dateob,std,classteacher,division,roll,phone,email,address) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                
                insert_blob_tuple=(admissionnumber,Picture,n,dob,c,cteacher,d,r,pe,e,a)
                # Convert data into tuple format

                result = cursor.execute(query, insert_blob_tuple)
            else:
                 query= "INSERT INTO students(admissionnumber,photo,name,dateob,std,classteacher,division,roll,phone,email,address) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                
                 insert_blob_tuple=(admissionnumber,po,n,dob,c,cteacher,d,r,pe,e,a)
                # Convert data into tuple format

                 result = cursor.execute(query, insert_blob_tuple)                            
            connection.commit()
            cursor.close()
            connection.close()
            rollsorting()
        except mysql.connector.Error as error:
            cursor.close()
            connection.close()                   
        finally:
            if (connection.is_connected()):
                cursor.close()
                connection.close()
    xyz=('students',)
    if xyz in tables:
        insertBLOB(admissionnumber,po,n,dob,c,cteacher,d,r,pe,e,a)
    elif xyz not in tables:
        try:
            connection = mysql.connector.connect(host='localhost',user='admin',password='root',database='studentdirectory')
            cursor=connection.cursor()
            query="CREATE TABLE students(admissionnumber char(4) primary key not null,photo longblob,name varchar(100) not null,dateob varchar(10) not null,std varchar(4) not null,classteacher varchar(100) not null,division char(1) not null,roll int,phone varchar(12) not null,email varchar(1000),address varchar(1000) not null)"
            cursor.execute(query)
            connection.commit()
            insertBLOB(admissionnumber,po,n,dob,c,cteacher,d,r,pe,e,a)
        except mysql.connector.Error as error:
            pass
        finally:
            if (connection.is_connected()):
                cursor.close()
                connection.close()
def adddeleted(admissionnumber,po,n,dob,c,cteacher,d,r,pe,e,a):
    connection = mysql.connector.connect(host='localhost',user='admin',password='root',database='studentdirectory')
    cursor=connection.cursor()
    cursor.execute("SHOW TABLES")
    tables=cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    def insertBLOB(admissionnumber,po,n,dob,c,cteacher,d,r,pe,e,a):#blob stmt      
        try:
            connection = mysql.connector.connect(host='localhost',user='admin',password='root',database='studentdirectory')
            cursor=connection.cursor()
            query= "INSERT INTO studentsdeleted(admissionnumber,photo,name,dateob,std,classteacher,division,roll,phone,email,address) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                
            insert_blob_tuple=(admissionnumber,po,n,dob,c,cteacher,d,r,pe,e,a)
                # Convert data into tuple format

            result = cursor.execute(query, insert_blob_tuple)
                            
            connection.commit()
        except mysql.connector.Error as error:
            pass
        finally:
            if (connection.is_connected()):
                cursor.close()
                connection.close()    
    xyz=('studentsdeleted',)
    if xyz in tables:
        insertBLOB(admissionnumber,po,n,dob,c,cteacher,d,r,pe,e,a)
    elif xyz not in tables:
        try:
            connection = mysql.connector.connect(host='localhost',user='admin',password='root',database='studentdirectory')
            cursor=connection.cursor()
            query="CREATE TABLE studentsdeleted(admissionnumber char(4) not null,photo longblob,name varchar(100) not null,dateob varchar(10) not null,std varchar(4) not null,classteacher varchar(100) not null,division char(1) not null,roll int not null,phone varchar(12) not null,email varchar(1000),address varchar(1000) not null)"
            cursor.execute(query)
            connection.commit()
            insertBLOB(admissionnumber,po,n,dob,c,cteacher,d,r,pe,e,a)
        except mysql.connector.Error as error:
            pass
        finally:
            if (connection.is_connected()):
                cursor.close()
                connection.close()
def deletedetails(adid):
    connection = mysql.connector.connect(host='localhost',user='admin',password='root',database='studentdirectory')
    cursor=connection.cursor()
    query="select std,division from students where admissionnumber='{}'".format(adid)
    cursor.execute(query)
    rolling1=cursor.fetchall()
    cursor.close()
    connection.close()
    c1=rolling1[0]
    c=c1[0]
    d1=rolling1[0]
    d=d1[1]
    
    def rollsorting():
        connection = mysql.connector.connect(host='localhost',user='admin',password='root',database='studentdirectory')
        cursor=connection.cursor()
        query="select admissionnumber from students where std='{}' and division='{}' order by name".format(c,d)
        cursor.execute(query)
        rolling=cursor.fetchall()
        cursor.close()
        connection.close()
        forrolling=1
        for ring in range(len(rolling)):
            rrolling=rolling[ring]
            connection = mysql.connector.connect(host='localhost',user='admin',password='root',database='studentdirectory')
            cursor=connection.cursor()
            query="update students set roll={} where admissionnumber='{}'".format(forrolling,rrolling[0])
            cursor.execute(query)
            forrolling+=1
            connection.commit()
            cursor.close()
            connection.close()   
    try:
        connection = mysql.connector.connect(host='localhost',user='admin',password='root',database='studentdirectory')
        cursor=connection.cursor()            
        query= "DELETE FROM STUDENTS WHERE admissionnumber='{}'".format(adid)
        # Convert data into tuple format
        result = cursor.execute(query)
        connection.commit()
        cursor.close()
        connection.close()       
        rollsorting()
    except mysql.connector.Error as error:
        cursor.close()
        connection.close()
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close() 
def deletedetail(r,c,d):
    def rollsorting():
        connection = mysql.connector.connect(host='localhost',user='admin',password='root',database='studentdirectory')
        cursor=connection.cursor()
        query="select admissionnumber from students where std='{}' and division='{}' order by name".format(c,d)
        cursor.execute(query)
        rolling=cursor.fetchall()
        cursor.close()
        connection.close()
        forrolling=1
        for ring in range(len(rolling)):
            rrolling=rolling[ring]
            connection = mysql.connector.connect(host='localhost',user='admin',password='root',database='studentdirectory')
            cursor=connection.cursor()
            query="update students set roll={} where admissionnumber='{}'".format(forrolling,rrolling[0])
            cursor.execute(query)
            forrolling+=1
            connection.commit()
            cursor.close()
            connection.close()   
    try:
        connection = mysql.connector.connect(host='localhost',user='admin',password='root',database='studentdirectory')
        cursor=connection.cursor()

            
        query= "DELETE FROM STUDENTS WHERE roll={} and std='{}' and division='{}'".format(r,c,d)
        # Convert data into tuple format
        result = cursor.execute(query)
        connection.commit()
        cursor.close()
        connection.close()    
        rollsorting()  
    except mysql.connector.Error as error:
        cursor.close()
        connection.close() 
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
def updatee(n,r,dob,c,d,ct,photo,phoneno,email,address,adm):
    def rollsorting():
        connection = mysql.connector.connect(host='localhost',user='admin',password='root',database='studentdirectory')
        cursor=connection.cursor()
        query="select admissionnumber from students where std='{}' and division='{}' order by name".format(c,d)
        cursor.execute(query)
        rolling=cursor.fetchall()
        cursor.close()
        connection.close()
        forrolling=1
        for ring in range(len(rolling)):
            rrolling=rolling[ring]
            connection = mysql.connector.connect(host='localhost',user='admin',password='root',database='studentdirectory')
            cursor=connection.cursor()
            query="update students set roll={} where admissionnumber='{}'".format(forrolling,rrolling[0])
            cursor.execute(query)
            forrolling+=1
            connection.commit()
            cursor.close()
            connection.close()   
    def convertToBinaryData(filename):
        exten=filename.split('.')
        ex=exten[-1]
                             
        im = cv2.imread(filename)
        im_resize = cv2.resize(im, (161, 192))
            
        is_success, im_buf_arr = cv2.imencode("."+ex, im_resize)
        byte_im = im_buf_arr.tobytes()
        return byte_im


    def insertBLOB(n,r,dob,c,d,ct,photo,phoneno,email,address,adm):#blob stmt
        try:
            connection = mysql.connector.connect(host='localhost',user='admin',password='root',database='studentdirectory')
            cursor=connection.cursor()
            Picture=convertToBinaryData(photo)
            query= "update students set name=%s,roll=%s,dateob=%s,std=%s,division=%s,classteacher=%s,photo=%s,phone=%s,email=%s,address=%s where admissionnumber=%s".format(n,r,dob,c,d,ct,Picture,phoneno,email,address,adm)
            tupletoupdate=(n,r,dob,c,d,ct,Picture,phoneno,email,address,adm)
                

            result = cursor.execute(query, tupletoupdate)
                            
            connection.commit()
            cursor.close()
            connection.close()
            rollsorting()
        except mysql.connector.Error as error:                
            cursor.close()
            connection.close()                
        finally:
            if (connection.is_connected()):
                cursor.close()
                connection.close()
    insertBLOB(n,r,dob,c,d,ct,photo,phoneno,email,address,adm)
def updatee1(n,r,dob,c,d,ct,photo,phoneno,email,address,adm):
    def rollsorting():
        connection = mysql.connector.connect(host='localhost',user='admin',password='root',database='studentdirectory')
        cursor=connection.cursor()
        query="select admissionnumber from students where std='{}' and division='{}' order by name".format(c,d)
        cursor.execute(query)
        rolling=cursor.fetchall()
        cursor.close()
        connection.close()
        forrolling=1
        for ring in range(len(rolling)):
            rrolling=rolling[ring]
            connection = mysql.connector.connect(host='localhost',user='admin',password='root',database='studentdirectory')
            cursor=connection.cursor()
            query="update students set roll={} where admissionnumber='{}'".format(forrolling,rrolling[0])
            cursor.execute(query)
            forrolling+=1
            connection.commit()
            cursor.close()
            connection.close()   
    def insertBLOB(n,r,dob,c,d,ct,photo,phoneno,email,address,adm):#blob stmt
        try:
            connection = mysql.connector.connect(host='localhost',user='admin',password='root',database='studentdirectory')
            cursor=connection.cursor()
            query= "update students set name=%s,roll=%s,dateob=%s,std=%s,division=%s,classteacher=%s,photo=%s,phone=%s,email=%s,address=%s where admissionnumber=%s".format(n,r,dob,c,d,ct,photo,phoneno,email,address,adm)
            tupletoupdate=(n,r,dob,c,d,ct,photo,phoneno,email,address,adm)
            result = cursor.execute(query, tupletoupdate)                            
            connection.commit()
            cursor.close()
            connection.close()
            rollsorting()
        except mysql.connector.Error as error:                
            curosr.close()
            connection.close()                  
        finally:
            if (connection.is_connected()):
                cursor.close()
                connection.close()
    insertBLOB(n,r,dob,c,d,ct,photo,phoneno,email,address,adm)
def cteacherautomation(c,d):
            connection = mysql.connector.connect(host='localhost',user='admin',password='root',database='studentdirectory')
            cursor=connection.cursor()
            query="""select std,division from students"""
            cursor.execute(query)
            record=cursor.fetchall()
            cursor.close()
            connection.close()
            l1=[]
            for row in record:
                 l1.append(row) 
            tu=(str(c),str(d))
            if tu in l1:
                try:
                    connection = mysql.connector.connect(host='localhost',user='admin',password='root',database='studentdirectory')
                    cursor=connection.cursor()
                    query= "select classteacher from students where std=%s and division=%s".format(c,d)
                    tupletoupdate=(c,d)
                    cursor.execute(query, tupletoupdate)
                    result55=cursor.fetchall()
                    connection.commit()
                    global ctr
                    for i in result55:
                        for j in i:
                            ctr=j
                except mysql.connector.Error as error:
                    pass         
                finally:
                    if (connection.is_connected()):
                        cursor.close()
                        connection.close()           
                        return True
                        cursor.close()
                        connection.close()
            else:                        
                return False
                cursor.close()
                connection.close()
def cupdate(c,d,nct):
        try:
            connection = mysql.connector.connect(host='localhost',user='admin',password='root',database='studentdirectory')
            cursor=connection.cursor()
            query= "update students set classteacher=%s where std=%s and division=%s".format(nct,c,d)
            tupletoupdate=(nct,c,d)
            result = cursor.execute(query, tupletoupdate)               
            connection.commit()
        except mysql.connector.Error as error:
            pass
                
        finally:
            if (connection.is_connected()):
                cursor.close()
                connection.close()                

