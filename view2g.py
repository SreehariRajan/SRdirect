# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view2.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

import retrieve,view1g
class Ui_view2(object):
    def backing(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=view1g.Ui_view1()
        self.ui.setupUi(self.window)
        self.window.show()
        self.view2.hide()
    def detail(self):
        global roll,name,clas,div,pic,phone,email,address,dateofbirth,ctr,adi
        ctr=retrieve.cteach
        adi=retrieve.admis
        dateofbirth=retrieve.dob
        roll=retrieve.r
        name=retrieve.n
        clas=retrieve.c
        div=retrieve.d
        pic=retrieve.po
        phone=retrieve.pe
        email=retrieve.e
        address=retrieve.a
        if pic==b'PHOTO NOT AVAILABLE':
            font = QtGui.QFont()
            font.setFamily("Myriad Pro")
            font.setPixelSize(18)
            font.setBold(True)
            font.setWeight(75)
            self.photo.setFont(font)
            self.photo.setStyleSheet("border: 2px solid black;")
            pic="           PHOTO \n              NOT \n       AVAILABLE"
            self.photo.setText(pic)
        else:
            self.show(pic)
    def show(self,pic):
        self.photo.setScaledContents(True) #QImage object
        self.pixmap=QtGui.QPixmap()
        picformatcheck=['png','jpg','jpeg']
        for i in range (0,len(picformatcheck)):
            self.pixmap.loadFromData(pic,picformatcheck[i])
            self.photo.setPixmap(self.pixmap)
            if self.pixmap.loadFromData(pic,picformatcheck[i])==True:
                break
            i+=1
    def setupUi(self, view2):
        self.view2=view2
        view2.setObjectName("view2")
        view2.resize(717, 531)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(view2.sizePolicy().hasHeightForWidth())
        view2.setSizePolicy(sizePolicy)
        view2.setMinimumSize(QtCore.QSize(717, 531))
        view2.setMaximumSize(QtCore.QSize(717, 531))
        self.centralwidget = QtWidgets.QWidget(view2)
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
        self.label.setGeometry(QtCore.QRect(0, -20, 751, 551))
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/ttt.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(620, 10, 31, 31))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/newPrefix/icon.png"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(650, 15, 47, 20))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPixelSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(90, 120, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPixelSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(90, 360, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPixelSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(90, 240, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPixelSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(90, 210, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPixelSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(90, 150, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPixelSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.invalid_2 = QtWidgets.QLabel(self.centralwidget)
        self.invalid_2.setGeometry(QtCore.QRect(220, 420, 151, 16))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPixelSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.invalid_2.setFont(font)
        self.invalid_2.setStyleSheet("color:rgb(238, 0, 0)\n"
"")
        self.invalid_2.setText("")
        self.invalid_2.setObjectName("invalid_2")
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(570, 440, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPixelSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.exit.setFont(font)
        self.exit.setAcceptDrops(False)
        self.exit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.exit.setCheckable(False)
        self.exit.setDefault(True)
        self.exit.setFlat(True)
        self.exit.setObjectName("exit")
        self.name = QtWidgets.QLabel(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(210, 120, 291, 21))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPixelSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.name.setFont(font)
        self.name.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.name.setText("")
        self.name.setScaledContents(False)
        self.name.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.name.setWordWrap(False)
        self.name.setObjectName("name")
        self.roll = QtWidgets.QLabel(self.centralwidget)
        self.roll.setGeometry(QtCore.QRect(210, 150, 231, 21))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPixelSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.roll.setFont(font)
        self.roll.setText("")
        self.roll.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.roll.setObjectName("roll")
        self.class_2 = QtWidgets.QLabel(self.centralwidget)
        self.class_2.setGeometry(QtCore.QRect(210, 210, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPixelSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.class_2.setFont(font)
        self.class_2.setText("")
        self.class_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.class_2.setObjectName("class_2")
        self.division = QtWidgets.QLabel(self.centralwidget)
        self.division.setGeometry(QtCore.QRect(210, 240, 231, 21))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPixelSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.division.setFont(font)
        self.division.setText("")
        self.division.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.division.setObjectName("division")
        self.address = QtWidgets.QLabel(self.centralwidget)
        self.address.setGeometry(QtCore.QRect(210, 360, 300, 151))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPixelSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.address.setFont(font)
        self.address.setText("")
        self.address.setTextFormat(QtCore.Qt.PlainText)
        self.address.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.address.setObjectName("address")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(90, 330, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPixelSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(90, 300, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPixelSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.phonenumber = QtWidgets.QLabel(self.centralwidget)
        self.phonenumber.setGeometry(QtCore.QRect(210, 300, 281, 21))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPixelSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.phonenumber.setFont(font)
        self.phonenumber.setText("")
        self.phonenumber.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.phonenumber.setObjectName("phonenumber")
        self.emailid = QtWidgets.QLabel(self.centralwidget)
        self.emailid.setGeometry(QtCore.QRect(210, 330, 291, 21))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPixelSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.emailid.setFont(font)
        self.emailid.setText("")
        self.emailid.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.emailid.setObjectName("emailid")
        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(470, 120, 161, 191))
        self.photo.setText("")
        self.photo.setObjectName("photo")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(90, 180, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPixelSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.dob = QtWidgets.QLabel(self.centralwidget)
        self.dob.setGeometry(QtCore.QRect(210, 180, 231, 21))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPixelSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.dob.setFont(font)
        self.dob.setText("")
        self.dob.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.dob.setObjectName("dob")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(90, 270, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPixelSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.cteacher = QtWidgets.QLabel(self.centralwidget)
        self.cteacher.setGeometry(QtCore.QRect(210, 270, 231, 21))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPixelSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.cteacher.setFont(font)
        self.cteacher.setText("")
        self.cteacher.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.cteacher.setObjectName("cteacher")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(90, 90, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPixelSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.adid = QtWidgets.QLabel(self.centralwidget)
        self.adid.setGeometry(QtCore.QRect(210, 90, 291, 21))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPixelSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.adid.setFont(font)
        self.adid.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.adid.setText("")
        self.adid.setScaledContents(False)
        self.adid.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.adid.setWordWrap(False)
        self.adid.setObjectName("adid")
        self.add_2 = QtWidgets.QPushButton(self.centralwidget)
        self.add_2.setGeometry(QtCore.QRect(10, 10, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPixelSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.add_2.setFont(font)
        self.add_2.setAcceptDrops(False)
        self.add_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.add_2.setCheckable(False)
        self.add_2.setDefault(True)
        self.add_2.setFlat(True)
        self.add_2.setObjectName("add_2")
        self.add_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label.raise_()
        self.invalid.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_10.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.invalid_2.raise_()
        self.exit.raise_()
        self.name.raise_()
        self.roll.raise_()
        self.class_2.raise_()
        self.division.raise_()
        self.address.raise_()
        self.label_11.raise_()
        self.label_15.raise_()
        self.phonenumber.raise_()
        self.emailid.raise_()
        self.photo.raise_()
        self.label_16.raise_()
        self.dob.raise_()
        self.label_17.raise_()
        self.cteacher.raise_()
        self.label_5.raise_()
        self.adid.raise_()
        self.add_2.raise_()
        view2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(view2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 717, 21))
        self.menubar.setObjectName("menubar")
        view2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(view2)
        self.statusbar.setObjectName("statusbar")
        view2.setStatusBar(self.statusbar)

        self.detail()
        self.name.setText(name.upper())
        self.adid.setText(adi.upper())
        self.cteacher.setText(ctr.upper())
        self.roll.setText(str(roll))
        self.class_2.setText((str(clas)).upper())
        self.phonenumber.setText(phone)
        self.division.setText(div.upper())
        self.emailid.setText(email)
        self.address.setText(address.upper())
        self.dob.setText(str(dateofbirth))
        self.exit.clicked.connect(self.backing)

        
        self.retranslateUi(view2)
        QtCore.QMetaObject.connectSlotsByName(view2)
        view2.setTabOrder(self.exit, self.add_2)

    def retranslateUi(self, view2):
        _translate = QtCore.QCoreApplication.translate
        view2.setWindowTitle(_translate("view2", "View details"))
        self.label_3.setText(_translate("view2", "guest"))
        self.label_4.setText(_translate("view2", "NAME                        :"))
        self.label_10.setText(_translate("view2", "ADDRESS                :"))
        self.label_12.setText(_translate("view2", "DIVISION                 :"))
        self.label_13.setText(_translate("view2", "CLASS                       :"))
        self.label_14.setText(_translate("view2", "ROLLNO                   :"))
        self.exit.setText(_translate("view2", "BACK"))
        self.label_11.setText(_translate("view2", "EMAIL ID                 :"))
        self.label_15.setText(_translate("view2", "PHONE NO             :"))
        self.label_16.setText(_translate("view2", "D.O.B                         :"))
        self.label_17.setText(_translate("view2", "CLASS TEACHER   :"))
        self.label_5.setText(_translate("view2", "ADMN NO               :"))
        self.add_2.setText(_translate("view2", "SEARCH"))
import pic


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    view2 = QtWidgets.QMainWindow()
    ui = Ui_view2()
    ui.setupUi(view2)
    view2.show()
    sys.exit(app.exec_())
