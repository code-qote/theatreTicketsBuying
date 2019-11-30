# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'accepting.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Accepting(object):
    def setupUi(self, Accepting):
        Accepting.setObjectName("Accepting")
        Accepting.resize(400, 243)
        self.listWidget = QtWidgets.QListWidget(Accepting)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 401, 141))
        self.listWidget.setStyleSheet("border: 3px solid #ff8a00;\n"
"background-color: #f7f7f7;")
        self.listWidget.setObjectName("listWidget")
        self.lineEdit = QtWidgets.QLineEdit(Accepting)
        self.lineEdit.setGeometry(QtCore.QRect(10, 170, 381, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border: 3px solid #ff8a00;\n"
"background-color: #f7f7f7;")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Accepting)
        self.label.setGeometry(QtCore.QRect(10, 150, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.Accept = QtWidgets.QPushButton(Accepting)
        self.Accept.setGeometry(QtCore.QRect(230, 210, 75, 31))
        self.Accept.setStyleSheet("border: 7px double #ff8a00;\n"
"background-color: #f7f7f7;")
        self.Accept.setObjectName("Accept")
        self.cancel = QtWidgets.QPushButton(Accepting)
        self.cancel.setGeometry(QtCore.QRect(310, 210, 75, 31))
        self.cancel.setStyleSheet("border: 7px double #ff8a00;\n"
"background-color: #f7f7f7;")
        self.cancel.setObjectName("cancel")
        self.label_2 = QtWidgets.QLabel(Accepting)
        self.label_2.setEnabled(False)
        self.label_2.setGeometry(QtCore.QRect(10, 210, 121, 16))
        self.label_2.setStyleSheet("color: red")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Accepting)
        QtCore.QMetaObject.connectSlotsByName(Accepting)

    def retranslateUi(self, Accepting):
        _translate = QtCore.QCoreApplication.translate
        Accepting.setWindowTitle(_translate("Accepting", "Подтверждение"))
        self.label.setText(_translate("Accepting", "Введите ваш email"))
        self.Accept.setText(_translate("Accepting", "ОК"))
        self.cancel.setText(_translate("Accepting", "Отмена"))
