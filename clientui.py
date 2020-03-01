# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'messanger.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Messanger(object):
    def setupUi(self, Messanger):
        Messanger.setObjectName("Messanger")
        Messanger.resize(542, 526)
        self.centralwidget = QtWidgets.QWidget(Messanger)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(26, 78, 491, 321))
        self.textBrowser.setObjectName("textBrowser")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(30, 420, 381, 31))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(420, 420, 101, 31))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(40, 30, 151, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 40, 51, 16))
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(280, 30, 161, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(450, 40, 61, 16))
        self.label_2.setObjectName("label_2")
        Messanger.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Messanger)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 542, 21))
        self.menubar.setObjectName("menubar")
        Messanger.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Messanger)
        self.statusbar.setObjectName("statusbar")
        Messanger.setStatusBar(self.statusbar)

        self.retranslateUi(Messanger)
        QtCore.QMetaObject.connectSlotsByName(Messanger)

    def retranslateUi(self, Messanger):
        _translate = QtCore.QCoreApplication.translate
        Messanger.setWindowTitle(_translate("Messanger", "MainWindow"))
        self.pushButton.setText(_translate("Messanger", "Send"))
        self.label.setText(_translate("Messanger", "Username"))
        self.label_2.setText(_translate("Messanger", "Password"))
