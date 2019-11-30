# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'repertoire.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_repertoire(object):
    def setupUi(self, repertoire):
        repertoire.setObjectName("repertoire")
        repertoire.resize(696, 448)
        repertoire.setStyleSheet("background-color: white\n"
"")
        self.listWidget = QtWidgets.QListWidget(repertoire)
        self.listWidget.setGeometry(QtCore.QRect(10, 110, 301, 331))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet("border: 3px solid #ff8a00;\n"
"background-color: #f7f7f7;")
        self.listWidget.setObjectName("listWidget")
        self.back_to_start = QtWidgets.QPushButton(repertoire)
        self.back_to_start.setGeometry(QtCore.QRect(10, 10, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Universal Grotesk Remake")
        font.setPointSize(12)
        self.back_to_start.setFont(font)
        self.back_to_start.setStyleSheet("border: 7px double #ff8a00;\n"
"background-color: #f7f7f7;")
        self.back_to_start.setObjectName("back_to_start")
        self.lineEdit = QtWidgets.QLineEdit(repertoire)
        self.lineEdit.setGeometry(QtCore.QRect(10, 70, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border: 3px solid #ff8a00;\n"
"background-color: #f7f7f7;")
        self.lineEdit.setMaxLength(100)
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.rb_name = QtWidgets.QRadioButton(repertoire)
        self.rb_name.setEnabled(True)
        self.rb_name.setGeometry(QtCore.QRect(120, 10, 82, 17))
        self.rb_name.setStyleSheet("")
        self.rb_name.setChecked(True)
        self.rb_name.setObjectName("rb_name")
        self.rb_date = QtWidgets.QRadioButton(repertoire)
        self.rb_date.setEnabled(True)
        self.rb_date.setGeometry(QtCore.QRect(120, 40, 82, 17))
        self.rb_date.setStyleSheet("")
        self.rb_date.setObjectName("rb_date")
        self.calendarWidget = QtWidgets.QCalendarWidget(repertoire)
        self.calendarWidget.setEnabled(False)
        self.calendarWidget.setGeometry(QtCore.QRect(320, 10, 371, 431))
        self.calendarWidget.setStyleSheet("color: black;\n"
"\n"
"")
        self.calendarWidget.setGridVisible(False)
        self.calendarWidget.setNavigationBarVisible(True)
        self.calendarWidget.setDateEditEnabled(True)
        self.calendarWidget.setObjectName("calendarWidget")

        self.retranslateUi(repertoire)
        QtCore.QMetaObject.connectSlotsByName(repertoire)

    def retranslateUi(self, repertoire):
        _translate = QtCore.QCoreApplication.translate
        repertoire.setWindowTitle(_translate("repertoire", "Репертуар"))
        self.back_to_start.setText(_translate("repertoire", "Вернуться"))
        self.rb_name.setText(_translate("repertoire", "Название"))
        self.rb_date.setText(_translate("repertoire", "Дата"))
