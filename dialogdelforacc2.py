# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogdel.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import createaccount
class Ui_dialogdel(object):
    def yess(self):
        self.window = QtWidgets.QMainWindow()
        self.ui=createaccount.Ui_createaccount()
        self.ui.setupUi(self.window)
        self.window.show()
        self.dialogdel1.hide()
    def noo(self):
        self.dialogdel1.close()
    def setupUi(self, dialogdel):
        self.dialogdel1=dialogdel
        dialogdel.setObjectName("dialogdel")
        dialogdel.resize(450, 185)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dialogdel.sizePolicy().hasHeightForWidth())
        dialogdel.setSizePolicy(sizePolicy)
        dialogdel.setMinimumSize(QtCore.QSize(450, 185))
        dialogdel.setMaximumSize(QtCore.QSize(450, 185))
        self.label = QtWidgets.QLabel(dialogdel)
        self.label.setGeometry(QtCore.QRect(-10, -10, 491, 261))
        self.label.setStyleSheet("background-color: rgb(247, 247, 247);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(dialogdel)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 41, 41))
        self.label_2.setStyleSheet("background-image: url(:/newPrefix/hiclipart.com (3) (1).png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(dialogdel)
        self.label_3.setGeometry(QtCore.QRect(80, 50, 361, 41))
        font = QtGui.QFont()
        font.setPixelSize(14)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(48, 127, 255);\n"
"color: rgb(39, 96, 255);\n"
"")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(dialogdel)
        self.label_4.setGeometry(QtCore.QRect(80, 20, 341, 41))
        font = QtGui.QFont()
        font.setPixelSize(14)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(48, 127, 255);\n"
"color: rgb(39, 96, 255);\n"
"")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(dialogdel)
        self.label_5.setGeometry(QtCore.QRect(0, 140, 451, 51))
        self.label_5.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.yes = QtWidgets.QPushButton(dialogdel)
        self.yes.setGeometry(QtCore.QRect(360, 150, 75, 23))
        self.yes.setAutoDefault(False)
        self.yes.setDefault(True)
        self.yes.setObjectName("yes")
        self.no = QtWidgets.QPushButton(dialogdel)
        self.no.setGeometry(QtCore.QRect(270, 150, 75, 23))
        self.no.setStyleSheet("")
        self.no.setAutoDefault(True)
        self.no.setDefault(False)
        self.no.setFlat(False)
        self.no.setObjectName("no")
        self.yes.clicked.connect(self.yess)
        self.no.clicked.connect(self.noo)
        self.retranslateUi(dialogdel)
        QtCore.QMetaObject.connectSlotsByName(dialogdel)
        dialogdel.setTabOrder(self.yes, self.no)
    
    def retranslateUi(self, dialogdel):
        _translate = QtCore.QCoreApplication.translate
        dialogdel.setWindowTitle(_translate("dialogdel", "Confirm"))
        self.label_3.setText(_translate("dialogdel", "Do you want to continue?"))
        self.label_4.setText(_translate("dialogdel", "Account removed successfully."))
        self.yes.setText(_translate("dialogdel", "Yes"))
        self.no.setText(_translate("dialogdel", "No"))
import pic


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialogdel = QtWidgets.QDialog()
    ui = Ui_dialogdel()
    ui.setupUi(dialogdel)
    dialogdel.show()
    sys.exit(app.exec_())
