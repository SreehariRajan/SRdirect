# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu1.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

import add,mod0,view02option,promote,del1,retrieve,first,removeacc,head
class Ui_menu(object):
    def removee(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=removeacc.Ui_admin()
        self.ui.setupUi(self.window)
        self.window.show()
        self.menu.hide()
    def back1(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=first.Ui_first()
        self.ui.setupUi(self.window)
        self.window.show()
        self.menu.hide()
    def disablebuttons(self):
        if retrieve.disabletest()==True:
            self.modify.setEnabled(False)
            self.delete_2.setEnabled(False)
            self.promoting.setEnabled(False)
            if head.exstucheck()==True:
                self.view.setEnabled(True)
            else:
                self.view.setEnabled(False)
        else:
            self.modify.setEnabled(True)
            self.delete_2.setEnabled(True)
            self.view.setEnabled(True)
            self.promoting.setEnabled(True)
    def addd(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=add.Ui_add_2()
        self.ui.setupUi(self.window)
        self.window.show()
        self.menu.hide()
    def modd(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=mod0.Ui_mod0()
        self.ui.setupUi(self.window)
        self.window.show()
        self.menu.hide()
    def delt(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=del1.Ui_del1()
        self.ui.setupUi(self.window)
        self.window.show()
        self.menu.hide()
    def vie(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=view02option.Ui_view0()
        self.ui.setupUi(self.window)
        self.window.show()
        self.menu.hide()
    def promo(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=promote.Ui_promote()
        self.ui.setupUi(self.window)
        self.window.show()
        self.menu.hide()
    def setupUi(self, menu):
        self.menu=menu
        menu.setObjectName("menu")
        menu.resize(717, 531)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(menu.sizePolicy().hasHeightForWidth())
        menu.setSizePolicy(sizePolicy)
        menu.setMinimumSize(QtCore.QSize(717, 531))
        menu.setMaximumSize(QtCore.QSize(717, 531))
        self.centralwidget = QtWidgets.QWidget(menu)
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
        self.label.setGeometry(QtCore.QRect(0, -20, 751, 551))
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/student shaming.jpg"))
        self.label.setObjectName("label")
        self.add = QtWidgets.QPushButton(self.centralwidget)
        self.add.setGeometry(QtCore.QRect(140, 70, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPixelSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.add.setFont(font)
        self.add.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.add.setDefault(True)
        self.add.setFlat(True)
        self.add.setObjectName("add")
        self.delete_2 = QtWidgets.QPushButton(self.centralwidget)
        self.delete_2.setGeometry(QtCore.QRect(140, 230, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPixelSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.delete_2.setFont(font)
        self.delete_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.delete_2.setDefault(True)
        self.delete_2.setFlat(True)
        self.delete_2.setObjectName("delete_2")
        self.modify = QtWidgets.QPushButton(self.centralwidget)
        self.modify.setGeometry(QtCore.QRect(140, 150, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPixelSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.modify.setFont(font)
        self.modify.setAutoFillBackground(False)
        self.modify.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.modify.setDefault(True)
        self.modify.setFlat(True)
        self.modify.setObjectName("modify")
        self.view = QtWidgets.QPushButton(self.centralwidget)
        self.view.setGeometry(QtCore.QRect(140, 310, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPixelSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.view.setFont(font)
        self.view.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.view.setAutoDefault(False)
        self.view.setDefault(True)
        self.view.setFlat(True)
        self.view.setObjectName("view")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(620, 10, 31, 31))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/newPrefix/icon.png"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(650, 20, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPixelSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.removeaccount = QtWidgets.QPushButton(self.centralwidget)
        self.removeaccount.setGeometry(QtCore.QRect(0, 450, 160, 31))
        font = QtGui.QFont()
        font.setPixelSize(14)
        font.setUnderline(True)
        font.setStrikeOut(False)
        self.removeaccount.setFont(font)
        self.removeaccount.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.removeaccount.setAcceptDrops(True)
        self.removeaccount.setAutoFillBackground(False)
        self.removeaccount.setStyleSheet("color: rgb(48, 127, 255);\n"
"color: rgb(39, 96, 255);\n"
"")
        self.removeaccount.setInputMethodHints(QtCore.Qt.ImhNone)
        self.removeaccount.setCheckable(False)
        self.removeaccount.setDefault(False)
        self.removeaccount.setFlat(True)
        self.removeaccount.setObjectName("forget")
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(560, 430, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPixelSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.exit.setFont(font)
        self.exit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.exit.setDefault(True)
        self.exit.setFlat(True)
        self.exit.setObjectName("exit")
        self.promoting = QtWidgets.QPushButton(self.centralwidget)
        self.promoting.setGeometry(QtCore.QRect(140, 390, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPixelSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.promoting.setFont(font)
        self.promoting.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.promoting.setAutoDefault(False)
        self.promoting.setDefault(True)
        self.promoting.setFlat(True)
        self.promoting.setObjectName("promoting")
        menu.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(menu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 717, 21))
        self.menubar.setObjectName("menubar")
        menu.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(menu)
        self.statusbar.setObjectName("statusbar")
        menu.setStatusBar(self.statusbar)

        self.disablebuttons()
        self.add.clicked.connect(self.addd)
        self.modify.clicked.connect(self.modd)
        self.delete_2.clicked.connect(self.delt)
        self.view.clicked.connect(self.vie)
        self.promoting.clicked.connect(self.promo)
        self.exit.clicked.connect(self.back1)
        self.retranslateUi(menu)
        QtCore.QMetaObject.connectSlotsByName(menu)

        self.removeaccount.clicked.connect(self.removee)
        menu.setTabOrder(self.add,self.modify)
        menu.setTabOrder(self.modify,self.delete_2)
        menu.setTabOrder(self.delete_2,self.view)
        menu.setTabOrder(self.view,self.promoting)
        menu.setTabOrder(self.promoting,self.removeaccount)
        menu.setTabOrder(self.removeaccount,self.exit)

        
    def retranslateUi(self, menu):
        _translate = QtCore.QCoreApplication.translate
        menu.setWindowTitle(_translate("menu", "Admin"))
        self.add.setText(_translate("menu", "ADD"))
        self.delete_2.setText(_translate("menu", "DELETE"))
        self.modify.setText(_translate("menu", "UPDATE"))
        self.view.setText(_translate("menu", "SEARCH"))
        self.label_3.setText(_translate("menu", "admin"))
        self.exit.setText(_translate("menu", "EXIT"))
        self.promoting.setText(_translate("menu", "PROMOTE"))
        self.removeaccount.setText(_translate("admin", "Remove account"))
import pic


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    menu = QtWidgets.QMainWindow()
    ui = Ui_menu()
    ui.setupUi(menu)
    menu.show()
    sys.exit(app.exec_())
