# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'play.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_play(object):
    def setupUi(self, play):
        play.setObjectName("play")
        play.resize(791, 523)
        play.setStyleSheet("background-color: white\n"
"")
        self.label = QtWidgets.QLabel(play)
        self.label.setGeometry(QtCore.QRect(9, 10, 781, 251))
        self.label.setText("")
        self.label.setObjectName("label")
        self.listWidget = QtWidgets.QListWidget(play)
        self.listWidget.setGeometry(QtCore.QRect(0, 310, 121, 211))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet("border: 3px solid #ff8a00;\n"
"background-color: #f7f7f7;")
        self.listWidget.setObjectName("listWidget")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(play)
        self.plainTextEdit.setGeometry(QtCore.QRect(130, 330, 661, 191))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setStyleSheet("border: 3px solid #ff8a00;\n"
"background-color: #f7f7f7;")
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label_2 = QtWidgets.QLabel(play)
        self.label_2.setGeometry(QtCore.QRect(140, 270, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.director = QtWidgets.QLabel(play)
        self.director.setGeometry(QtCore.QRect(140, 300, 421, 21))
        font = QtGui.QFont()
        font.setFamily("Universal Grotesk Remake")
        font.setPointSize(14)
        self.director.setFont(font)
        self.director.setObjectName("director")
        self.label_3 = QtWidgets.QLabel(play)
        self.label_3.setGeometry(QtCore.QRect(570, 280, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.author = QtWidgets.QLabel(play)
        self.author.setGeometry(QtCore.QRect(570, 301, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Universal Grotesk Remake")
        font.setPointSize(14)
        self.author.setFont(font)
        self.author.setObjectName("author")
        self.name = QtWidgets.QLabel(play)
        self.name.setGeometry(QtCore.QRect(8, 10, 781, 201))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(40)
        self.name.setFont(font)
        self.name.setStyleSheet("background-color: rgba(255, 0, 0, 0);\n"
"color: white;")
        self.name.setAlignment(QtCore.Qt.AlignCenter)
        self.name.setObjectName("name")
        self.back = QtWidgets.QPushButton(play)
        self.back.setGeometry(QtCore.QRect(10, 10, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Universal Grotesk Remake")
        font.setPointSize(11)
        self.back.setFont(font)
        self.back.setStyleSheet("border: 7px double #ff8a00;\n"
"background-color: #f7f7f7;")
        self.back.setObjectName("back")
        self.label_4 = QtWidgets.QLabel(play)
        self.label_4.setGeometry(QtCore.QRect(0, 270, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(play)
        QtCore.QMetaObject.connectSlotsByName(play)

    def retranslateUi(self, play):
        _translate = QtCore.QCoreApplication.translate
        play.setWindowTitle(_translate("play", "form"))
        self.label_2.setText(_translate("play", "Режиссер"))
        self.director.setText(_translate("play", "TextLabel"))
        self.label_3.setText(_translate("play", "Автор"))
        self.author.setText(_translate("play", "TextLabel"))
        self.name.setText(_translate("play", "TextLabel"))
        self.back.setText(_translate("play", "Вернуться"))
        self.label_4.setText(_translate("play", "Выберите время"))
