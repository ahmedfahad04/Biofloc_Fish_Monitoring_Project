# from backend.database_module import database_manager as dm

# handler = dm()
# # print(handler.pre_culture_tank_list())


# # print(handler.pre_culture_water_report("TANK_9")
# import pprint as p
# p.pprint(dir(handler))

from PyQt5 import QtGui, QtWidgets
from PyQt5 import QtCore
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

def popup():
    app2 =  QApplication([])
    win = QWidget()

    # all widgets
    lay = QVBoxLayout()
    btn = QPushButton("নিশ্চিত করুন")
    lbl = QLabel("পাসওয়ার্ড")
    txt = QLineEdit()

    # widget modification
    txt.setPlaceholderText("আপনার পাসওয়ার্ড লিখুন")
    txt.setValidator(QIntValidator())
    txt.setFixedSize(300,30)
    txt.setFont(QFont("Baloo Da 2",12))

    lbl.setFixedSize(300,80)
    lbl.setAlignment(Qt.AlignLeft)
    lbl.setFont(QFont("Baloo Da 2",30))

    btn.clicked.connect(lambda: showtxt())
    btn.setFont(QFont("Baloo Da 2",12))

    # setting the widget into the layout
    lay.addWidget(lbl)
    lay.addWidget(txt)
    lay.addWidget(btn)
    lay.setAlignment(Qt.AlignCenter)

    # set the layout in the main application window
    win.setLayout(lay)
    win.show()

    value = 0
    def showtxt():
        info = txt.text()
        if info == '1234':
            print("Bingo!!")
            txt.clear()
            msgBox("অভিনন্দন! আপনার তথ্য সংরক্ষণ করা হয়েছে।", QtWidgets.QMessageBox.Information)
            value = 1
            win.hide() 
        else:
            print("Failed!")
            txt.clear()
            msgBox("আপনি ভুল পাসওয়ার্ড দিয়েছেন। আবার চেষ্টা করুন।", QtWidgets.QMessageBox.Warning)

    # execute the application
    app2.exec_()


def msgBox(message, myicon):
    msg = QtWidgets.QMessageBox()
    msg.setIcon(myicon)
    msg.setText(message)
    msg.setWindowTitle("Confirm Password")
    msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
    msg.setFont(QFont("Baloo Da 2",12))
    msg.exec_()

def maincode():
    app = QApplication([])
    popup().show()
    app.exec_()
