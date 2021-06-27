import PySide2
from sample import *
from basic_functions import *
from PyQt5.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from backend.database_module import database_manager as dm
from PySide2.QtWidgets import * 
from ui_password import Ui_Form as ui
import random as r


class MainWindow(QMainWindow):


    def __init__(self):
        QMainWindow.__init__(self) 

        # creating connection with ui_sample.py with these 2 lines of code.
        self.obj = Ui_MainWindow()
        self.obj.setupUi(self)

        # primary fucntion
        ongoing_preculture = list()
        self.setTabSize()
        self.all_tanks_info_tab1()
        self.pre_culture_table_manager_tab3()
        self.water_preperation_table_manager_tab2()

        # make all table read only
        self.obj.table_water_info.setEditTriggers(PySide2.QtWidgets.QTableWidget.NoEditTriggers)
        self.obj.table_show_all_tanks.setEditTriggers(PySide2.QtWidgets.QTableWidget.NoEditTriggers)
        self.obj.table_all_info.setEditTriggers(PySide2.QtWidgets.QTableWidget.NoEditTriggers)


        # self.obj.table_show_tank.setSelectionMode(QAbstractItemView.MultiSelection)
        
        # ==> working with Main Window----------------------
        # setting up windows properties
        self.setFixedSize(840, 516)
        self.obj.tabWidget.setCurrentIndex(0) # show the first tap initially
       

        # ==> working with tab operation----------------------
        # connecting buttons
        self.obj.btn_add_tank.clicked.connect(self.addTank)
        self.obj.btn_delete_tank.clicked.connect(self.rowDelete)
        self.obj.btn_prepare_water.clicked.connect(lambda: self.preparetank(ongoing_preculture))
        self.obj.tabWidget.currentChanged.connect(lambda: self.reload(ongoing_preculture))
        


        self.show()


    def reload(self, tankls):
        self.pre_culture_table_manager_tab3()

        # self.water_preperation_table_manager_tab2() # eta ekhane deya jabe na
               

    def rowDelete(self):
        id = self.obj.table_show_tank.currentRow()
        self.obj.table_show_tank.removeRow(id)


    def setTabSize(self):
         # setting table colwidth
        self.obj.table_water_info.setColumnWidth(4, 150)
        self.obj.table_water_info.setColumnWidth(3, 200)
        self.obj.table_water_info.setColumnWidth(0, 120)
        self.obj.table_water_info.setColumnWidth(1, 100)
        self.obj.table_water_info.setColumnWidth(2, 100)

        self.obj.table_show_all_tanks.setColumnWidth(0, 200)
        self.obj.table_show_all_tanks.setColumnWidth(1, 200)
        self.obj.table_show_all_tanks.setColumnWidth(2, 270)

        self.obj.table_show_tank.setColumnWidth(1, 140)


    def all_tanks_info_tab1(self):
        if self.obj.table_all_info.rowCount() != 0 :
            self.obj.stackedWidget.setCurrentWidget(self.obj.stk_table)
            
        else:
            if self.obj.table_all_info.rowCount() != 0:
                print(self.obj.table_show_tank.rowCount())
                self.obj.stackedWidget.setCurrentWidget(self.obj.stk_table)
            else:
                print("Table is empty")
            self.obj.stackedWidget.setCurrentWidget(self.obj.stk_button)


    def water_preperation_table_manager_tab2(self):
        
        primary_data = dm().pre_culture_tank_list()
        tank_list = []

        for item in primary_data:
            tank_list.append(item[0])
            print("Tanks Registered for water preperation: ",tank_list)

        # tank_list = tankls # how can I get all tanks name that have already registered for water perperation.***
   
        
        if len(tank_list) == 0:
            return
        else:
            tr = 0

            # clear table...
            rows = self.obj.table_water_info.rowCount()
            for row in range(0, rows, 1):
                self.obj.table_water_info.removeRow(row)
            
            # store value in table
            for tank_no in tank_list:
                self.obj.table_water_info.insertRow(tr) #its a must

               
                value = dm().pre_culture_water_report(tank_no)
                ph = value[0]
                tds = value[1]
               

                if tank_no == '':
                    return
                else:
                   
                    self.obj.table_water_info.setItem(tr, 0, PySide2.QtWidgets.QTableWidgetItem(str(tank_no)))
                    self.obj.table_water_info.setItem(tr, 1, PySide2.QtWidgets.QTableWidgetItem(str(ph)))
                    self.obj.table_water_info.setItem(tr, 2, PySide2.QtWidgets.QTableWidgetItem(str(tds)))

                    tr+=1
                    print("Current row: ", tr)

                
    def pre_culture_table_manager_tab3(self):
        
        # needs testing
        data = dm().available_tank_reporting() # collects the name of  #-> [tank numbers]
        print("AVAILABLE TANKS: ",data)

        self.obj.comboBox_select_tank_wp.clear()
        for row in data:
            self.obj.comboBox_select_tank_wp.addItem(row) # add the tank names into dropdown menu

       
    def addTank(self):

        fishName = self.obj.lineEdit_fish_name.text()
        days = self.obj.lineEdit_day.text()
        serial = self.obj.comboBox_select_tank_wp.currentText()
        
        date, tank_no, vol = dm().tank_basic_report(serial)

        print(fishName, days, tank_no, date, vol)
        #volume = tank_details[tank_no]

        tablerow = self.obj.table_show_tank.rowCount()
        self.obj.table_show_tank.insertRow(tablerow) #its a must

        self.obj.table_show_tank.setItem(tablerow, 0, PySide2.QtWidgets.QTableWidgetItem(tank_no))
        self.obj.table_show_tank.setItem(tablerow, 1, PySide2.QtWidgets.QTableWidgetItem(str(vol)))
        self.obj.table_show_tank.setItem(tablerow, 2, PySide2.QtWidgets.QTableWidgetItem(fishName))
        self.obj.table_show_tank.setItem(tablerow, 3, PySide2.QtWidgets.QTableWidgetItem(days))
        self.obj.table_show_tank.setItem(tablerow, 4, PySide2.QtWidgets.QTableWidgetItem(date))

        self.obj.lineEdit_fish_name.clear()
        self.obj.lineEdit_day.clear()


    def preparetank(self,ongoing_preculture):
        rows = self.obj.table_show_tank.rowCount()
        info = dict()

        for i in range(rows):
            data = i 

            tank_serial = self.obj.table_show_tank.item(data, 0).text()
            duration = self.obj.table_show_tank.item(data, 3).text()
            fish = self.obj.table_show_tank.item(data, 2).text()

            info[tank_serial] = [duration, fish]
            
            ongoing_preculture.append(tank_serial)


        ui.tableVlaues(info)

         # clear table...
        rows = self.obj.table_show_tank.rowCount()
        for row in range(0, rows):
            self.obj.table_show_tank.removeRow(row)

        self.water_preperation_table_manager_tab2() # reload the 2nd tab



# # tab1 table -> latest_water_report(self, tank_num)
# tank_num -> active_tank_reporting


app = QApplication([])
mw = MainWindow()
app.exec_()



