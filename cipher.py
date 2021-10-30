# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cipher2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Cipher(object):
    def setupUi(self, Cipher):
        Cipher.setObjectName("Cipher")
        Cipher.resize(1100, 600)
        Cipher.setMinimumSize(QtCore.QSize(1100, 600))
        Cipher.setMaximumSize(QtCore.QSize(1100, 600))
        Cipher.setStyleSheet("background-color: rgb(250, 240, 239);\n"
"border-color: rgb(118, 0, 59);")
        self.centralwidget = QtWidgets.QWidget(Cipher)
        self.centralwidget.setObjectName("centralwidget")

        self.knopka_zashifrovat = QtWidgets.QPushButton(self.centralwidget)
        self.knopka_zashifrovat.setGeometry(QtCore.QRect(630, 20, 150, 50))
        self.knopka_zashifrovat.setStyleSheet("background-color: rgb(209, 209, 209);")
        self.knopka_zashifrovat.setObjectName("knopka_zashifrovat")

        self.knopka_deshifrovat = QtWidgets.QPushButton(self.centralwidget)
        self.knopka_deshifrovat.setGeometry(QtCore.QRect(870, 20, 150, 50))
        self.knopka_deshifrovat.setStyleSheet("background-color: rgb(209, 209, 209);")
        self.knopka_deshifrovat.setObjectName("knopka_deshifrovat")

        self.tyt_vivodit_soobshenie = QtWidgets.QTextBrowser(self.centralwidget)
        self.tyt_vivodit_soobshenie.setGeometry(QtCore.QRect(600, 190, 400, 380))
        self.tyt_vivodit_soobshenie.setStyleSheet("border-color: rgb(145, 145, 145);\n"
                                                  "background-color: rgb(239, 239, 239);")
        self.tyt_vivodit_soobshenie.setObjectName("tyt_vivodit_soobshenie")

        self.soobshenie_vvod = QtWidgets.QLabel(self.centralwidget)
        self.soobshenie_vvod.setGeometry(QtCore.QRect(60, 150, 281, 20))
        self.soobshenie_vvod.setObjectName("soobshenie_vvod")

        self.soobshenie_vivod = QtWidgets.QLabel(self.centralwidget)
        self.soobshenie_vivod.setGeometry(QtCore.QRect(720, 150, 281, 20))
        self.soobshenie_vivod.setObjectName("soobshenie_vivod")

        self.label_vvedite_keyword = QtWidgets.QLabel(self.centralwidget)
        self.label_vvedite_keyword.setGeometry(QtCore.QRect(10, 20, 300, 31))
        self.label_vvedite_keyword.setObjectName("label_vvedite_keyword")

        self.label_viberite_language = QtWidgets.QLabel(self.centralwidget)
        self.label_viberite_language.setGeometry(QtCore.QRect(10, 80, 520, 31))
        self.label_viberite_language.setObjectName("label_viberite_language")

        self.tyt_vvodit_keyword = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.tyt_vvodit_keyword.setGeometry(QtCore.QRect(230, 20, 300, 40))
        self.tyt_vvodit_keyword.setStyleSheet("background-color: rgb(239, 239, 239);")
        self.tyt_vvodit_keyword.setObjectName("tyt_vvodit_keyword")

        self.tyt_vvodit_soobshenie = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.tyt_vvodit_soobshenie.setGeometry(QtCore.QRect(40, 190, 400, 380))
        self.tyt_vvodit_soobshenie.setStyleSheet("background-color: rgb(239, 239, 239);")
        self.tyt_vvodit_soobshenie.setObjectName("tyt_vvodit_soobshenie")

        Cipher.setCentralWidget(self.centralwidget)

        self.retranslateUi(Cipher)
        QtCore.QMetaObject.connectSlotsByName(Cipher)

    def retranslateUi(self, Cipher):
        _translate = QtCore.QCoreApplication.translate

        Cipher.setWindowTitle(_translate("Cipher", "MainWindow"))

        self.knopka_zashifrovat.setText(_translate("Cipher", "Зашифровать"))
        self.knopka_deshifrovat.setText(_translate("Cipher", "Дешифровать"))

        self.soobshenie_vvod.setText(_translate("Cipher", "Введите сообщение сюда"))
        self.soobshenie_vivod.setText(_translate("Cipher", "Результат"))

        self.label_vvedite_keyword.setText(_translate("Cipher", "Введите ключ-слово:"))
        self.label_viberite_language.setText(_translate("Cipher", "Программа поддерживает только русский язык."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Cipher = QtWidgets.QMainWindow()
    ui = Ui_Cipher()
    ui.setupUi(Cipher)
    Cipher.show()
    sys.exit(app.exec_())

