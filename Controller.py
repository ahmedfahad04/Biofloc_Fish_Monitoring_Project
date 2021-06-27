from backend.database_module import database_manager as dm
from basic_functions import *
import ui_password as ui_pass

def reload():
    # data = connect_to_database("operational data/tank.db","tank_basic_table")
    data = dm().available_tank_reporting()

    print("REGISTERED TANKS: ", data)

    for table_no in data:
        a = dm().pre_culture_water_report(table_no)
        print("WORKING....")

        if not a:
            print("Tuple is Empty")
        else:
            print(a[0], a[1])

def verify():
    handle = ui_pass.Ui_Form()
    handle.btn_pass.clicked.connect(clickevent)


def msgBox(self, message, myicon, ):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(myicon)
        msg.setText(message)
        msg.setWindowTitle("Confirm Password")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        msg.exec_()

def clickevent(self):
    txt = self.lineEdit_pass.text()

    if txt=="1224":
        print("Correct Password")
        self.msgBox("অভিনন্দন! আপনার তথ্য সংরক্ষণ করা হয়েছে।", QtWidgets.QMessageBox.Information)
        return 1
        
    else:
        self.msgBox("আপনি ভুল পাসওয়ার্ড দিয়েছেন। আবার চেষ্টা করুন।", QtWidgets.QMessageBox.Warning)




