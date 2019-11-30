# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'start_page.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StartPage(object):
    def setupUi(self, StartPage):
        StartPage.setObjectName("StartPage")
        StartPage.resize(543, 373)
        font = QtGui.QFont()
        font.setPointSize(26)
        StartPage.setFont(font)
        StartPage.setStyleSheet("background-color: white\n"
"")
        self.centralwidget = QtWidgets.QWidget(StartPage)
        self.centralwidget.setObjectName("centralwidget")
        self.nextPage = QtWidgets.QPushButton(self.centralwidget)
        self.nextPage.setGeometry(QtCore.QRect(440, 2, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Universal Grotesk Remake")
        font.setPointSize(10)
        self.nextPage.setFont(font)
        self.nextPage.setStyleSheet("background-color: #f7f7f7;\n"
"                            border: 7px double #ff8a00;")
        self.nextPage.setObjectName("nextPage")
        self.previousPage = QtWidgets.QPushButton(self.centralwidget)
        self.previousPage.setEnabled(False)
        self.previousPage.setGeometry(QtCore.QRect(0, 0, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Universal Grotesk Remake")
        font.setPointSize(10)
        self.previousPage.setFont(font)
        self.previousPage.setStyleSheet("background-color: #f7f7f7;\n"
"                            border: 7px double #ff8a00;")
        self.previousPage.setObjectName("previousPage")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 0, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Universal Grotesk Remake")
        font.setPointSize(24)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 59, 541, 311))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.Dram_theatre_ok = QtWidgets.QPushButton(self.page)
        self.Dram_theatre_ok.setGeometry(QtCore.QRect(170, 150, 201, 111))
        font = QtGui.QFont()
        font.setFamily("Universal Grotesk Remake")
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        self.Dram_theatre_ok.setFont(font)
        self.Dram_theatre_ok.setStyleSheet("border: 7px double #ff8a00;\n"
"background-color: #f7f7f7;")
        self.Dram_theatre_ok.setObjectName("Dram_theatre_ok")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(0, 20, 541, 51))
        font = QtGui.QFont()
        font.setFamily("Universal Grotesk Remake")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #ff8a00;\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(0, 60, 541, 51))
        font = QtGui.QFont()
        font.setFamily("Universal Grotesk Remake")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #ff8a00;\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        StartPage.setCentralWidget(self.centralwidget)

        self.retranslateUi(StartPage)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(StartPage)

    def retranslateUi(self, StartPage):
        _translate = QtCore.QCoreApplication.translate
        StartPage.setWindowTitle(_translate("StartPage", "Театры"))
        self.nextPage.setText(_translate("StartPage", "Следующий"))
        self.previousPage.setText(_translate("StartPage", "Предыдущий"))
        self.label_3.setText(_translate("StartPage", "Выберите театр"))
        self.Dram_theatre_ok.setText(_translate("StartPage", "Перейти"))
        self.label.setText(_translate("StartPage", "Самарский академический театр драмы"))
        self.label_2.setText(_translate("StartPage", " им. М. Горького"))
