import gevent
global forecho2,forechoo2
forecho2=1
forechoo2=1
from PyQt5 import QtWidgets
import mysql.connector
from mysql.connector import Error
import head,createaccount,sys,first
cc=head.databasecheck()
def doublecheck():
        app = QtWidgets.QApplication(sys.argv)
        connection = mysql.connector.connect(host='localhost',user='admin',password='root',database='studentdirectory')
        cursor=connection.cursor()
        cursor.execute("SHOW TABLES")
        tables=cursor.fetchall()
        cursor.close()
        connection.close()
        if ('accountinfo',) in tables:
                connection = mysql.connector.connect(host='localhost',user='admin',password='root',database='studentdirectory')
                cursor=connection.cursor()
                cursor.execute("select * from accountinfo")
                tables=cursor.fetchall()
                cursor.close()
                connection.close()
                if len(tables)!=0:
                            window=QtWidgets.QMainWindow()
                            ui=first.Ui_first()
                            ui.setupUi(window)
                            window.show()
                else:
                            window=QtWidgets.QMainWindow()
                            ui=createaccount.Ui_createaccount()
                            ui.setupUi(window)
                            window.show()
                app.exec_()
                                    
        elif ('accountinfo',) not in tables:
            try:
                connection = mysql.connector.connect(host='localhost',user='admin',password='root',database='studentdirectory')
                cursor=connection.cursor()
                query="CREATE TABLE accountinfo(user varchar(100),password varchar(100) primary key,question varchar(1000),answer varchar(1000))"
                cursor.execute(query)
                connection.commit()
                cursor.close()
                connection.close()
                window=QtWidgets.QMainWindow()
                ui=createaccount.Ui_createaccount()
                ui.setupUi(window)
                window.show()
                app.exec_()
            except mysql.connector.Error as error:
                pass
            finally:
                if (connection.is_connected()):
                    cursor.close()
                    connection.close()            
if cc==True:
    doublecheck()
        
elif cc==False:
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
                doublecheck()
