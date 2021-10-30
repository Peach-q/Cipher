from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from cipher import Ui_Cipher


app = QtWidgets.QApplication(sys.argv)


Cipher = QtWidgets.QMainWindow()
ui = Ui_Cipher()
ui.setupUi(Cipher)
Cipher.show()
def decesar1():

    alfavit_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    smeshenie = ui.tyt_vvodit_keyword.toPlainText()
    smeshenie=int(len(str(smeshenie)))
    message = ui.tyt_vvodit_soobshenie.toPlainText()
    message=message.upper()
    itog = ''

    for i in message:
     mesto = alfavit_RU.find(i)
     new_mesto = mesto - smeshenie
     if i in alfavit_RU:
      itog += alfavit_RU[new_mesto]
    else:
     itog += i
    ui.tyt_vivodit_soobshenie.setText(itog)

ui.knopka_zashifrovat.clicked.connect(decesar1)

def decesar2():

    alfavit_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    smeshenie = ui.tyt_vvodit_keyword.toPlainText()
    smeshenie=int(len(str(smeshenie)))
    message = ui.tyt_vvodit_soobshenie.toPlainText()
    message=message.upper()
    itog = ''

    for i in message:
     mesto = alfavit_RU.find(i)
     new_mesto = mesto + smeshenie
     if i in alfavit_RU:
      itog += alfavit_RU[new_mesto]
    else:
     itog += i
    ui.tyt_vivodit_soobshenie.setText(itog)

ui.knopka_deshifrovat.clicked.connect(decesar2)

sys.exit(app.exec_())
