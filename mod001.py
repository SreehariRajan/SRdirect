# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mod001.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import retrieve,mod01,mod0,head

class Ui_mod001(object):
    def inchange(self):
        self.invalid_3.setText("")
    def cancel1(self): 
        self.window = QtWidgets.QMainWindow()
        self.ui=mod0.Ui_mod0()
        self.ui.setupUi(self.window)
        self.window.show()
        self.mod001.hide()
    def ctrselect(self):
        retrieve.modtestt(self.class_2.text().lower(),self.division.text().lower())
        if len(self.class_2.text())!=0 and len(self.division.text())!=0:
            if self.class_2.text().isdigit()==True or self.class_2.text().lower() in ['lkg','ukg']:
                if self.division.text().isalpha()==True:
                    if retrieve.classdivtest(self.class_2.text().lower(),self.division.text().lower())==True:
                        head.cteacherautomation(self.class_2.text().lower(),self.division.text().lower())
                        self.window = QtWidgets.QMainWindow()
                        self.ui=mod01.Ui_mod01()
                        self.ui.setupUi(self.window)
                        self.window.show()
                        self.mod001.hide()
                    else:

                        self.invalid_3.setText("Class does not exist")
                else:
                    self.invalid_3.setText("Invalid Entry")
            else:
                self.invalid_3.setText("Invalid Entry")
        else:
            self.invalid_3.setText("All fields are mandatory")
    def setupUi(self, mod001):
        self.mod001=mod001
        mod001.setObjectName("mod001")
        mod001.resize(591, 332)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mod001.sizePolicy().hasHeightForWidth())
        mod001.setSizePolicy(sizePolicy)
        mod001.setMinimumSize(QtCore.QSize(591, 332))
        mod001.setMaximumSize(QtCore.QSize(591, 332))
        self.centralwidget = QtWidgets.QWidget(mod001)
        self.centralwidget.setObjectName("centralwidget")
        self.invalid = QtWidgets.QLabel(self.centralwidget)
        self.invalid.setGeometry(QtCore.QRect(150, 350, 251, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        self.invalid.setFont(font)
        self.invalid.setStyleSheet("color: rgb(255, 3, 3);")
        self.invalid.setText("")
        self.invalid.setObjectName("invalid")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(0, -20, 751, 541))
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/ttt.jpg"))
        self.label.setObjectName("label")
        self.add = QtWidgets.QPushButton(self.centralwidget)
        self.add.setGeometry(QtCore.QRect(10, 10, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPixelSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.add.setFont(font)
        self.add.setAcceptDrops(False)
        self.add.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.add.setCheckable(False)
        self.add.setDefault(True)
        self.add.setFlat(True)
        self.add.setObjectName("add")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(500, 10, 31, 31))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/newPrefix/icon.png"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(530, 20, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPixelSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(150, 160, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPixelSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(150, 120, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPixelSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.division = QtWidgets.QLineEdit(self.centralwidget)
        self.division.setGeometry(QtCore.QRect(220, 160, 231, 21))
        self.division.setStyleSheet("background:transparent")
        self.division.setObjectName("division")
        self.class_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.class_2.setGeometry(QtCore.QRect(220, 120, 231, 21))
        self.class_2.setStyleSheet("background:transparent")
        self.class_2.setObjectName("class_2")
        self.invalid_2 = QtWidgets.QLabel(self.centralwidget)
        self.invalid_2.setGeometry(QtCore.QRect(240, 280, 151, 16))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPixelSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.invalid_2.setFont(font)
        self.invalid_2.setStyleSheet("color:rgb(238, 0, 0)")
        self.invalid_2.setText("")
        self.invalid_2.setObjectName("invalid_2")
        self.cancel = QtWidgets.QPushButton(self.centralwidget)
        self.cancel.setGeometry(QtCore.QRect(370, 230, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPixelSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cancel.setFont(font)
        self.cancel.setAcceptDrops(False)
        self.cancel.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cancel.setCheckable(False)
        self.cancel.setDefault(True)
        self.cancel.setFlat(True)
        self.cancel.setObjectName("cancel")
        self.submit = QtWidgets.QPushButton(self.centralwidget)
        self.submit.setGeometry(QtCore.QRect(220, 230, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPixelSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.submit.setFont(font)
        self.submit.setAcceptDrops(False)
        self.submit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.submit.setCheckable(False)
        self.submit.setDefault(True)
        self.submit.setFlat(True)
        self.submit.setObjectName("submit")
        self.invalid_3 = QtWidgets.QLabel(self.centralwidget)
        self.invalid_3.setGeometry(QtCore.QRect(220, 180, 231, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPixelSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.invalid_3.setFont(font)
        self.invalid_3.setStyleSheet("color:rgb(238, 0, 0)\n"
"")
        self.invalid_3.setText("")
        self.invalid_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.invalid_3.setObjectName("invalid_3")
        mod001.setCentralWidget(self.centralwidget)
        self.add.setFocusPolicy(QtCore.Qt.NoFocus)
        self.menubar = QtWidgets.QMenuBar(mod001)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 591, 21))
        self.menubar.setObjectName("menubar")
        mod001.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mod001)
        self.statusbar.setObjectName("statusbar")
        mod001.setStatusBar(self.statusbar)
        self.submit.clicked.connect(self.ctrselect)
        self.cancel.clicked.connect(self.cancel1)
        self.retranslateUi(mod001)
        QtCore.QMetaObject.connectSlotsByName(mod001)
        mod001.setTabOrder(self.class_2, self.division)
        mod001.setTabOrder(self.division, self.submit)
        mod001.setTabOrder(self.submit, self.cancel)
        self.class_2.textChanged.connect(self.inchange)
        self.division.textChanged.connect(self.inchange)
    

    def retranslateUi(self, mod001):
        _translate = QtCore.QCoreApplication.translate
        mod001.setWindowTitle(_translate("mod001", "Update"))
        self.add.setText(_translate("mod001", "UPDATE"))
        self.label_3.setText(_translate("mod001", "admin"))
        self.label_12.setText(_translate("mod001", "DIVISION "))
        self.label_13.setText(_translate("mod001", "CLASS       "))
        self.cancel.setText(_translate("mod001", "Back"))
        self.submit.setText(_translate("mod001", "Submit"))
import pic


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mod001 = QtWidgets.QMainWindow()
    ui = Ui_mod001()
    ui.setupUi(mod001)
    mod001.show()
    sys.exit(app.exec_())














 







    