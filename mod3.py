# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mod3.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

import retrieve,modify2c,mod1
class Ui_mod3(object):
    def inchange(self):
        self.invalid_3.setText("")
    def back1(self):
        self.window = QtWidgets.QMainWindow()
        self.ui=mod1.Ui_mod1()
        self.ui.setupUi(self.window)
        self.window.show()
        self.mod3.hide()
    def forcrup(self):
        y=self.roll.text
        yyy=self.class_2.text
        yyyy=self.division.text
        rll=self.roll.text()
        cls2=self.class_2.text()
        divsn=self.division.text()
        if len(rll)!=0 and len(cls2)!=0 and len(divsn)!=0:
            if divsn.isalpha()==True and rll.isdigit()==True:
                if cls2.isdigit()==True or cls2.lower() in ['lkg','ukg']:
                    if retrieve.classstudent(cls2.lower(),divsn.lower(),int(rll))==True:
                        self.roll.setText("")
                        self.class_2.setText("")
                        self.division.setText("")
                        retrieve.readBlobData(retrieve.zzz)
                        self.invalid_3.setText("")
                        self.window=QtWidgets.QMainWindow()
                        self.ui=modify2c.Ui_modify2()
                        self.ui.setupUi(self.window)
                        self.window.show()
                        self.mod3.hide()
                    else:
                        self.invalid_3.setText("Student not found")
                else:
                    self.invalid_3.setText("Invalid Entry")
            else:
                self.invalid_3.setText("Invalid Entry")
        else:
            self.invalid_3.setText("All fields are mandatory")

    def setupUi(self, mod3):
        self.mod3=mod3
        mod3.setObjectName("mod3")
        mod3.resize(601, 354)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mod3.sizePolicy().hasHeightForWidth())
        mod3.setSizePolicy(sizePolicy)
        mod3.setMinimumSize(QtCore.QSize(601, 354))
        mod3.setMaximumSize(QtCore.QSize(601, 354))
        self.centralwidget = QtWidgets.QWidget(mod3)
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
        self.add.setFocusPolicy(QtCore.Qt.NoFocus)
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
        self.label_12.setGeometry(QtCore.QRect(150, 140, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPixelSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(150, 90, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPixelSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(150, 190, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPixelSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.division = QtWidgets.QLineEdit(self.centralwidget)
        self.division.setGeometry(QtCore.QRect(220, 140, 231, 21))
        self.division.setStyleSheet("background:transparent")
        self.division.setObjectName("division")
        self.class_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.class_2.setGeometry(QtCore.QRect(220, 90, 231, 21))
        self.class_2.setStyleSheet("background:transparent")
        self.class_2.setObjectName("class_2")
        self.roll = QtWidgets.QLineEdit(self.centralwidget)
        self.roll.setGeometry(QtCore.QRect(220, 190, 231, 21))
        self.roll.setStyleSheet("background:transparent")
        self.roll.setObjectName("roll")
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
        self.cancel.setGeometry(QtCore.QRect(370, 240, 81, 21))
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
        self.submit.setGeometry(QtCore.QRect(220, 240, 81, 21))
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
        self.invalid_3.setGeometry(QtCore.QRect(220, 210, 231, 31))
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
        mod3.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mod3)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 601, 21))
        self.menubar.setObjectName("menubar")
        mod3.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mod3)
        self.statusbar.setObjectName("statusbar")
        mod3.setStatusBar(self.statusbar)
        self.cancel.clicked.connect(self.back1)
        self.submit.clicked.connect(self.forcrup)
        self.retranslateUi(mod3)
        QtCore.QMetaObject.connectSlotsByName(mod3)
        mod3.setTabOrder(self.class_2, self.division)
        mod3.setTabOrder(self.division, self.roll)
        mod3.setTabOrder(self.roll, self.submit)
        mod3.setTabOrder(self.submit, self.cancel)
        self.class_2.textChanged.connect(self.inchange)
        self.division.textChanged.connect(self.inchange)
        self.roll.textChanged.connect(self.inchange)
    def retranslateUi(self, mod3):
        _translate = QtCore.QCoreApplication.translate
        mod3.setWindowTitle(_translate("mod3", "Update"))
        self.add.setText(_translate("mod3", "UPDATE"))
        self.label_3.setText(_translate("mod3", "admin"))
        self.label_12.setText(_translate("mod3", "DIVISION "))
        self.label_13.setText(_translate("mod3", "CLASS       "))
        self.label_14.setText(_translate("mod3", "ROLLNO  "))
        self.cancel.setText(_translate("mod3", "Back"))
        self.submit.setText(_translate("mod3", "Submit"))
import pic


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mod3 = QtWidgets.QMainWindow()
    ui = Ui_mod3()
    ui.setupUi(mod3)
    mod3.show()
    sys.exit(app.exec_())
