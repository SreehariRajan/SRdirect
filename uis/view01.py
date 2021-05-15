# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view01.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_view01(object):
    def setupUi(self, view01):
        view01.setObjectName("view01")
        view01.resize(510, 313)
        self.centralwidget = QtWidgets.QWidget(view01)
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
        self.add.setGeometry(QtCore.QRect(10, 10, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
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
        self.label_2.setGeometry(QtCore.QRect(410, 10, 31, 31))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/newPrefix/icon.png"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(440, 20, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.invalid_2 = QtWidgets.QLabel(self.centralwidget)
        self.invalid_2.setGeometry(QtCore.QRect(240, 280, 151, 16))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.invalid_2.setFont(font)
        self.invalid_2.setStyleSheet("color:rgb(238, 0, 0)")
        self.invalid_2.setText("")
        self.invalid_2.setObjectName("invalid_2")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(220, 230, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.back.setFont(font)
        self.back.setAcceptDrops(False)
        self.back.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.back.setCheckable(False)
        self.back.setDefault(True)
        self.back.setFlat(True)
        self.back.setObjectName("back")
        self.classwise = QtWidgets.QPushButton(self.centralwidget)
        self.classwise.setGeometry(QtCore.QRect(220, 190, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.classwise.setFont(font)
        self.classwise.setAcceptDrops(False)
        self.classwise.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.classwise.setCheckable(False)
        self.classwise.setDefault(True)
        self.classwise.setFlat(True)
        self.classwise.setObjectName("classwise")
        self.admnno = QtWidgets.QRadioButton(self.centralwidget)
        self.admnno.setGeometry(QtCore.QRect(220, 90, 82, 17))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.admnno.setFont(font)
        self.admnno.setObjectName("admnno")
        self.admnno_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.admnno_2.setGeometry(QtCore.QRect(220, 130, 82, 17))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.admnno_2.setFont(font)
        self.admnno_2.setObjectName("admnno_2")
        view01.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(view01)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 510, 21))
        self.menubar.setObjectName("menubar")
        view01.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(view01)
        self.statusbar.setObjectName("statusbar")
        view01.setStatusBar(self.statusbar)

        self.retranslateUi(view01)
        QtCore.QMetaObject.connectSlotsByName(view01)
        view01.setTabOrder(self.admnno, self.admnno_2)
        view01.setTabOrder(self.admnno_2, self.classwise)
        view01.setTabOrder(self.classwise, self.back)
        view01.setTabOrder(self.back, self.add)

    def retranslateUi(self, view01):
        _translate = QtCore.QCoreApplication.translate
        view01.setWindowTitle(_translate("view01", "MainWindow"))
        self.add.setText(_translate("view01", "SEARCH"))
        self.label_3.setText(_translate("view01", "admin"))
        self.back.setText(_translate("view01", "BACK"))
        self.classwise.setText(_translate("view01", "OK"))
        self.admnno.setText(_translate("view01", "Admn No."))
        self.admnno_2.setText(_translate("view01", "Roll No."))
import pic_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    view01 = QtWidgets.QMainWindow()
    ui = Ui_view01()
    ui.setupUi(view01)
    view01.show()
    sys.exit(app.exec_())
