import time
from test import *
from sample import *
from basic_functions import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from backend.database_module import database_manager as dm
from PyQt5.QtWidgets import *
from threading import *



class MainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

        # creating connection with ui_sample.py with these 2 lines of code.
        self.obj = Ui_MainWindow()
        self.obj.setupUi(self)


        # primary fucntion
        self.initialize()
        self.all_tanks_info_tab1()
        self.water_preperation_table_manager_tab2()
        self.pre_culture_table_manager_tab3()
        self.fish_culture_termination_tab5()

        # ==> working with Main Window----------------------
        self.obj.tabWidget.setCurrentIndex(0)  # show the first tap initially
        

        # make all table read only
        self.obj.table_water_info.setEditTriggers(
            QtWidgets.QTableWidget.NoEditTriggers)
        self.obj.table_show_all_tanks.setEditTriggers(
            QtWidgets.QTableWidget.NoEditTriggers)
        self.obj.table_all_info.setEditTriggers(
            QtWidgets.QTableWidget.NoEditTriggers)


        # ==> working with tab operation----------------------
        # connecting buttons

        self.obj.btn_add_tank.clicked.connect(self.addTank)
        self.obj.btn_delete_tank.clicked.connect(self.rowDelete)
        self.obj.btn_prepare_water.clicked.connect(self.preparetank)
        self.obj.btn_fish_collection.clicked.connect(self.collectfish)
        self.obj.tabWidget.currentChanged.connect(self.Reload)


        self.show()
         

    # section - 1: different helper methods 
    def initialize(self):
      
        '''This method will initialize each tab after the user start the application and will set the 
        opening screen for each of these tabs'''

        # tab2
        try:
            table_row = dm().pre_culture_tank_list() 
            if table_row == 0:
                print("Row: ",self.obj.table_show_tank.rowCount())
                self.obj.stackedWidget_2.setCurrentWidget(self.obj.page_2)
        
            else:
                print("Option 1")
                self.obj.stackedWidget_2.setCurrentWidget(self.obj.stk_table2)

        except:
            print("Option 2")
            self.obj.stackedWidget_2.setCurrentWidget(self.obj.page_2)

    def msgBox(self, boxtitle,message, myicon):
      
        '''This  method shows different message boxes based on different situations with different messages'''

        msg = QtWidgets.QMessageBox()
        msg.setIcon(myicon)
        msg.setText(message)
        msg.setWindowTitle(boxtitle)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        msg.setFont(QFont("Baloo Da 2",12))
        x = msg.exec_()
        return x

    def popup(self, tanks, id):
      
        '''This method generates the password seeking GUI'''

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

        if id == 1:
            btn.clicked.connect(lambda: self.passchecker1(win, txt, tanks))
        elif id == 2:
            btn.clicked.connect(lambda: self.passchecker2(win, txt))

        btn.setFont(QFont("Baloo Da 2",12))


        # setting the widget into the layout
        lay.addWidget(lbl)
        lay.addWidget(txt)
        lay.addWidget(btn)
        lay.setAlignment(Qt.AlignCenter)

        # set the layout in the main application window
        win.setLayout(lay)
        win.show()

    def passchecker1(self, win, txt, tanks):
     
        '''Check the password for Tab3'''

        global value

        info = txt.text()
        if info == '1234':
            txt.clear()
            
            s = list()
            f = list()
            t = list()
            # tank_no, fish, days
            
            for name, attr in tanks.items():
                
                s.append(name)
                t.append(attr[0])
                f.append(attr[1])

            for no, fish, time in zip(s,f,t):
                dm().pre_culture_entry(no,fish,time) # erro handling

            # clear table...
            self.clrtable(self.obj.table_show_tank)
            

            self.msgBox("Confirm Password","অভিনন্দন! আপনার তথ্য সংরক্ষণ করা হয়েছে।", QtWidgets.QMessageBox.Information)
            win.hide()

        else:
            txt.clear()
            self.msgBox("Confirm Password","আপনি ভুল পাসওয়ার্ড দিয়েছেন। আবার চেষ্টা করুন।", QtWidgets.QMessageBox.Warning)

    def passchecker2(self, win, txt):
       
        '''Check password for Tab5'''


        info = txt.text()
        if info == '1234': # password matching
            print("Bingo!!")

            row = self.obj.table_show_all_tanks.currentIndex().row()
            item = self.obj.table_show_all_tanks.item(row, 0).text()


            cell_id = self.obj.table_show_all_tanks.currentRow()
            self.obj.table_show_all_tanks.removeRow(cell_id)


            print("fish collected from: ", item)
            dm().available_tank_relisting(item)

            txt.clear()
            self.msgBox("Tank Selection Checker","মাছ উত্তোলোন করুন", QtWidgets.QMessageBox.Information)
            win.hide()  

        else:
            print("Failed!")
            txt.clear()
            self.msgBox("Tank Selection Checker","আপনি ভুল পাসওয়ার্ড দিয়েছেন। আবার চেষ্টা করুন।", QtWidgets.QMessageBox.Warning)
  
    def recurring_timer(self):
        self.counter +=1
        print("THREAD: ",self.counter)

    def clrtable(self, tableName):

         # clear table...
        rows = tableName.rowCount()

        # step-1: select all rows
        for i in range(rows):
            tableName.selectRow(i)

        # step-2: collect the row id and remove the row. iterate all the row to clear the table
        for row in range(rows):
            id = tableName.currentRow()
            tableName.removeRow(id)
            # print("Deleting ", row , " rows!!")

    # section - 2: method for managing each tabs individually(4 methods)
    def all_tanks_info_tab1(self):

        '''Controls the information flow of Tab1'''

        if self.obj.table_all_info.rowCount() != 0:
            self.obj.stackedWidget.setCurrentWidget(self.obj.stk_table)

            # tank_num = dm().active_tank_reporting()
            # for tank in tank_num:
            #     info = dm().latest_water_report(tank)
            #     ph = info[0]
            #     tds = info[1]
            #     temp = info[2]
 

        else:
            if self.obj.table_all_info.rowCount() != 0:
                print(self.obj.table_show_tank.rowCount())
                self.obj.stackedWidget.setCurrentWidget(self.obj.stk_table)
            else:
                print("Table is empty")

            self.obj.stackedWidget.setCurrentWidget(self.obj.stk_button)

    def water_preperation_table_manager_tab2(self):

        '''Controls the information flow of Tab2'''    
        
        # clear table..
        self.clrtable(self.obj.table_water_info)


        #fetching tank list
        tank_list = []
        try:
            primary_data = dm().pre_culture_tank_list() 
        
            for item in primary_data:
                tank_list.append(item[0])
                # print("Water preperation Running Tab_2: ", tank_list)
        except:
            pass



        # inserting information
        if len(tank_list) == 0:
            return
        else:
          
            # store value in table
            for tank_no in tank_list:
                            
                value = dm().pre_culture_water_report(tank_no)
                ph = value[0]
                tds = value[1]              

                if tank_no == '' :
                    print("Empty")
                    return

                else:
                    
                    tr = self.obj.table_water_info.rowCount()
                    self.obj.table_water_info.insertRow(tr)  # its a must

                    self.obj.table_water_info.setItem(
                        tr, 0, QtWidgets.QTableWidgetItem(str(tank_no)))
                    self.obj.table_water_info.setItem(
                        tr, 1, QtWidgets.QTableWidgetItem(str(ph)))
                    self.obj.table_water_info.setItem(
                        tr, 2, QtWidgets.QTableWidgetItem(str(tds)))
                                        
    def pre_culture_table_manager_tab3(self):

        '''Controls the information flow of Tab3'''



        # needs testing
        # collects the name of  #-> [tank numbers]
        data = dm().available_tank_reporting()
        print("AVAILABLE TANKS Tab_3: ", data)

        self.obj.comboBox_select_tank_wp.clear()
        for row in data:
            # add the tank names into dropdown menu
            self.obj.comboBox_select_tank_wp.addItem(row)
        
    def fish_culture_termination_tab5(self):

        '''Controls the information flow of Tab5'''


        tank_num = dm().active_tank_reporting()
        
        tr = 0
        for tanks in tank_num:  
            all_tank = dm().tank_status_report(tanks)
            tank = all_tank[0]
            fish = all_tank[2]
            time = all_tank[3]

            print(tank, fish, time)
            self.obj.table_show_all_tanks.insertRow(tr)  # its a must

            self.obj.table_show_all_tanks.setItem(
                tr, 0, QtWidgets.QTableWidgetItem(str(tank)))
            self.obj.table_show_all_tanks.setItem(
                tr, 1, QtWidgets.QTableWidgetItem(str(fish)))
            self.obj.table_show_all_tanks.setItem(
                tr, 2, QtWidgets.QTableWidgetItem(str(time)))

            tr += 1
         
        #  available tank relisting

        # data ??


    # section - 3: these methods are connected to buttons
    def collectfish(self):

        '''This method perform the action of collecting fish when the btn_fish_collection button is pressed'''


        row = self.obj.table_show_all_tanks.currentIndex().row()
        item = self.obj.table_show_all_tanks.item(row, 0).text()


        #error handling - [empty table row]
        print(item)
        box = self.msgBox("Tank Selection Check", "আপনি কি {} এর মাছ উত্তোলন করেত চান?".format(item), QMessageBox.Warning)
        print(box)
        if box == 1024:
            print("show pass box")
            self.popup("",2)    
        else:
            return

    def addTank(self):

        '''Add the tanks, fish name and culturing time in table for starting the pre culture stage in tab3'''


        fishName = self.obj.lineEdit_fish_name.text()
        days = self.obj.lineEdit_day.text()
        serial = self.obj.comboBox_select_tank_wp.currentText()

        date, tank_no, vol = dm().tank_basic_report(serial)

        #error handling - [empty fish and time]
        if fishName == '' or days == '':
            self.msgBox("Empty Cell Checking","মাছের নাম এবং দিন সংখ্যা পূরণ করুন। এই দুটি ঘর ফাকা রাখা যাবে না।", QMessageBox.Warning)
            return
        
        # #error handling - [same tank selection]
        # if serial in tanks:
        #     self.msgBox("Duplicate Tank Selection", "আপনি ইতোমধ্যে এই জালাধার নির্বাচন করেছেন। অন্য জলাধার নির্বাচন করুন।", QMessageBox.Warning)
        #     return 
        # else:
        #     tanks.append(serial)


        tablerow = self.obj.table_show_tank.rowCount()
        self.obj.table_show_tank.insertRow(tablerow)  # its a must

        self.obj.table_show_tank.setItem(
            tablerow, 0, QtWidgets.QTableWidgetItem(tank_no))
        self.obj.table_show_tank.setItem(
            tablerow, 1, QtWidgets.QTableWidgetItem(str(vol)))
        self.obj.table_show_tank.setItem(
            tablerow, 2, QtWidgets.QTableWidgetItem(fishName))
        self.obj.table_show_tank.setItem(
            tablerow, 3, QtWidgets.QTableWidgetItem(days))
        self.obj.table_show_tank.setItem(
            tablerow, 4, QtWidgets.QTableWidgetItem(date))

        self.obj.lineEdit_fish_name.clear()
        self.obj.lineEdit_day.clear()

    def preparetank(self):

        '''Adds the tank to pre_culture_tanks list to show that these tanks 
        is undergoing the pre culture stage.'''

      
        # fetching information
        rows = self.obj.table_show_tank.rowCount()
        info = dict()

        # iterating through the rows to collect the data
        for i in range(0, rows, 1):
            data = i

            tank_serial = self.obj.table_show_tank.item(data, 0).text()
            duration = self.obj.table_show_tank.item(data, 3).text()
            fish = self.obj.table_show_tank.item(data, 2).text()

        
            info[tank_serial] = [duration, fish]

       
        # check password
        self.popup(info, 1)
       
    def Reload(self):

        '''This method will reload all Frontend activities in run time'''

        self.pre_culture_table_manager_tab3()
        self.water_preperation_table_manager_tab2()
     
    def rowDelete(self):

        '''Delete any table row by selecting current row'''

        id = self.obj.table_show_tank.currentRow()
        self.obj.table_show_tank.removeRow(id)

  


# execute the application

# # tab1 table -> latest_water_report(self, tank_num) -> ei table theke just 'last check' column er data nibo
# tank_num -> active_tank_reporting

app = QApplication([])
mw = MainWindow()
app.exec_()











































