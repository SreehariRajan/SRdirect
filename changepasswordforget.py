# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'changepasswordforget.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import forgetpassword as fp
from PyQt5 import QtCore, QtGui, QtWidgets
import regex as re
import head,admin,dialogpassword
class Ui_changepasswordforget(object):
    def inchange(self):
        self.invalid.setText("")
    def texting(self):
        self.invalid.setText("")
        if len(self.new_2.text())!=0:
            self.label_5.setEnabled(True)
            self.newconfirm.setEnabled(True)
            self.showpd_2.setEnabled(True)
            
            if len(self.new_2.text())==0:
                self.showpd_2.setStyleSheet("background-image:transparent")
            else:
                self.showpd_2.setStyleSheet("background-image: url(:/newPrefix/show-password-64 (1).png);")
                self.newconfirm.setEchoMode(QtWidgets.QLineEdit.Password)
        else:
                self.showpd_2.setEnabled(False)
                self.showpd_2.setStyleSheet("background-image:transparent")
                self.label_5.setEnabled(False)
                self.newconfirm.setEnabled(False)
    def iconpass(self):
        if fp.forecho1==1:
            self.showpd.setStyleSheet("background-image: url(:/newPrefix/kisspng-computer-icons-cross-eye-5adf65cad344d8.0427956315245900268654 (1).png);")
            self.new_2.setEchoMode(QtWidgets.QLineEdit.Normal)
            fp.forecho1=2
        else:
            self.showpd.setStyleSheet("background-image: url(:/newPrefix/show-password-64 (1).png);")
            self.new_2.setEchoMode(QtWidgets.QLineEdit.Password)
            fp.forecho1=1
    def back1(self):
        self.window = QtWidgets.QMainWindow()
        self.ui=admin.Ui_admin()
        self.ui.setupUi(self.window)
        self.window.show()
        self.changepasswordforget.hide()
    def iconpass2(self):
        if fp.forechoo1==1:
            self.showpd_2.setStyleSheet("background-image: url(:/newPrefix/kisspng-computer-icons-cross-eye-5adf65cad344d8.0427956315245900268654 (1).png);")
            self.newconfirm.setEchoMode(QtWidgets.QLineEdit.Normal)
            fp.forechoo1=2
        else:
            self.showpd_2.setStyleSheet("background-image: url(:/newPrefix/show-password-64 (1).png);")
            self.newconfirm.setEchoMode(QtWidgets.QLineEdit.Password)
            fp.forechoo1=1
    def subb(self):
        self.new_2.text
        recheck = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        if len(self.new_2.text())!=0 and len(self.newconfirm.text())!=0:
            if len(self.new_2.text())>=8 and len(self.newconfirm.text())>=8:
                if self.new_2.text()==self.newconfirm.text():
                    if(recheck.search(self.new_2.text()) == None):
                        self.invalid.setText("Minimum 1 special character required")
                    else:
                        
                        newp=self.new_2.text()
                        head.forget(newp,head.forgetpcheck)
                        self.window = QtWidgets.QMainWindow()
                        self.ui=dialogpassword.Ui_dialogpassword()
                        self.ui.setupUi(self.window)
                        self.window.show()
                        self.changepasswordforget.hide()
                        
                else:
                    self.invalid.setText("Those passwords didn't match")
            else:
                self.invalid.setText("Use 8 characters or more for your password")
        else:
            self.invalid.setText("All fields are mandatory")
    def setupUi(self, changepasswordforget):
        self.changepasswordforget=changepasswordforget
        changepasswordforget.setObjectName("changepasswordforget")
        changepasswordforget.resize(719, 522)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(changepasswordforget.sizePolicy().hasHeightForWidth())
        changepasswordforget.setSizePolicy(sizePolicy)
        changepasswordforget.setMinimumSize(QtCore.QSize(719, 522))
        changepasswordforget.setMaximumSize(QtCore.QSize(719, 522))
        self.centralwidget = QtWidgets.QWidget(changepasswordforget)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-10, -30, 731, 571))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/White-Lock-Wallpaper-1080x2340-.jpg"))
        self.label.setObjectName("label")
        self.new_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.new_2.setGeometry(QtCore.QRect(250, 190, 151, 21))
        self.new_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.new_2.setObjectName("new_2")
        self.invalid = QtWidgets.QLabel(self.centralwidget)
        self.invalid.setGeometry(QtCore.QRect(250, 260, 260, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPixelSize(13)
        self.invalid.setFont(font)
        self.invalid.setStyleSheet("color: rgb(255, 3, 3);")
        self.invalid.setText("")
        self.invalid.setObjectName("invalid")
        self.ok_ = QtWidgets.QPushButton(self.centralwidget)
        self.ok_.setGeometry(QtCore.QRect(290, 340, 75, 21))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPixelSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.ok_.setFont(font)
        self.ok_.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ok_.setDefault(True)
        self.ok_.setFlat(True)
        self.ok_.setObjectName("ok_")
        self.newconfirm = QtWidgets.QLineEdit(self.centralwidget)
        self.newconfirm.setGeometry(QtCore.QRect(250, 240, 151, 21))
        self.newconfirm.setEchoMode(QtWidgets.QLineEdit.Password)
        self.newconfirm.setObjectName("newconfirm")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(90, 130, 311, 20))
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.ok_1 = QtWidgets.QPushButton(self.centralwidget)
        self.ok_1.setGeometry(QtCore.QRect(120, 340, 75, 21))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPixelSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.ok_1.setFont(font)
        self.ok_1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ok_1.setDefault(True)
        self.ok_1.setFlat(True)
        self.ok_1.setObjectName("ok_1")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(90, 130, 311, 31))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(90, 290, 311, 31))
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(90, 300, 311, 20))
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setObjectName("line_4")
        self.showpd = QtWidgets.QPushButton(self.centralwidget)
        self.showpd.setGeometry(QtCore.QRect(410, 190, 22, 16))
        self.showpd.setStyleSheet("background-image: url(:/newPrefix/show-password-64 (1).png);")
        self.showpd.setText("")
        self.showpd.setDefault(False)
        self.showpd.setFlat(True)
        self.showpd.setObjectName("showpd")
        self.showpd_2 = QtWidgets.QPushButton(self.centralwidget)
        self.showpd_2.setGeometry(QtCore.QRect(410, 240, 22, 16))
        self.showpd_2.setText("")
        self.showpd_2.setDefault(False)
        self.showpd_2.setFlat(True)
        self.showpd_2.setObjectName("showpd_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(90, 240, 191, 20))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPixelSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(90, 190, 151, 20))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPixelSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        changepasswordforget.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(changepasswordforget)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 719, 21))
        self.menubar.setObjectName("menubar")
        changepasswordforget.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(changepasswordforget)
        self.statusbar.setObjectName("statusbar")
        changepasswordforget.setStatusBar(self.statusbar)
        self.ok_1.clicked.connect(self.subb)
        self.ok_.clicked.connect(self.back1)
        self.retranslateUi(changepasswordforget)
        self.showpd_2.setEnabled(False)
        self.label_5.setEnabled(False)
        self.newconfirm.setEnabled(False)
        self.showpd_2.setStyleSheet("background-image:transparent")
        self.new_2.textChanged.connect(self.texting)
        self.showpd.clicked.connect(self.iconpass)
        self.showpd_2.clicked.connect(self.iconpass2)
        QtCore.QMetaObject.connectSlotsByName(changepasswordforget)
        changepasswordforget.setTabOrder(self.new_2, self.newconfirm)
        changepasswordforget.setTabOrder(self.newconfirm, self.ok_1)
        changepasswordforget.setTabOrder(self.ok_1, self.ok_)
        changepasswordforget.setTabOrder(self.ok_,self.showpd)
        changepasswordforget.setTabOrder(self.showpd, self.showpd_2)        
        self.new_2.textChanged.connect(self.inchange)
        self.newconfirm.textChanged.connect(self.inchange)
    def retranslateUi(self, changepasswordforget):
        _translate = QtCore.QCoreApplication.translate
        changepasswordforget.setWindowTitle(_translate("changepasswordforget", "Forget password"))
        self.ok_.setText(_translate("changepasswordforget", "Cancel"))
        self.ok_1.setText(_translate("changepasswordforget", "Submit"))
        self.label_5.setText(_translate("changepasswordforget", "CONFIRM PASSWORD"))
        self.label_6.setText(_translate("changepasswordforget", "NEW PASSWORD"))
import pic


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    changepasswordforget = QtWidgets.QMainWindow()
    ui = Ui_changepasswordforget()
    ui.setupUi(changepasswordforget)
    changepasswordforget.show()
    sys.exit(app.exec_())
