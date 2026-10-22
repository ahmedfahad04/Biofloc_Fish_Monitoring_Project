# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_sampleHVBXIR.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################


from typing import Mapping
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import ui_reg as uiregform
import ui_delregwidget as uidelregform


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(884, 534)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:356.1, stop:0 rgba(65, 41, 90, 255), stop:1 rgba(47, 7, 67, 255));")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.frame)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setCursor(QCursor(Qt.ArrowCursor))
        self.tabWidget.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.987, y1:0, x2:0, y2:1, stop:0 rgba(19, 162, 225, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 63 12pt \"Baloo Da 2 SemiBold\";\n"
"color: rgb(0, 0, 0);\n"
"QTabBar::tab { color: rgb(0, 0, 0); }\n"
"QTabBar::tab:selected { color: rgb(0, 0, 0); }")
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tab_cultivation_monitor_0 = QWidget()
        self.tab_cultivation_monitor_0.setObjectName(u"tab_cultivation_monitor_0")
        self.gridLayout_9 = QGridLayout(self.tab_cultivation_monitor_0)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.stackedWidget = QStackedWidget(self.tab_cultivation_monitor_0)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stk_button = QWidget()
        self.stk_button.setObjectName(u"stk_button")
        self.btn_goto_newTankReg = QPushButton(self.stk_button)
        self.btn_goto_newTankReg.setObjectName(u"btn_goto_newTankReg")
        self.btn_goto_newTankReg.setEnabled(True)
        self.btn_goto_newTankReg.setGeometry(QRect(140, 190, 572, 54))
        self.btn_goto_newTankReg.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_goto_newTankReg.setStyleSheet(u"font: 63 20pt \"Baloo Da 2 SemiBold\";")
        self.btn_goto_newTankReg.setFlat(True)
        self.stackedWidget.addWidget(self.stk_button)
        self.stk_table = QWidget()
        self.stk_table.setObjectName(u"stk_table")
        self.verticalLayout = QVBoxLayout(self.stk_table)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.table_all_info = QTableWidget(self.stk_table)
        if (self.table_all_info.columnCount() < 9):
            self.table_all_info.setColumnCount(9)
        font = QFont()
        font.setFamily(u"Baloo Da 2 SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.table_all_info.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font);
        self.table_all_info.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font);
        self.table_all_info.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font);
        self.table_all_info.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font);
        self.table_all_info.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font);
        self.table_all_info.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font);
        self.table_all_info.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font);
        self.table_all_info.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font);
        self.table_all_info.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.table_all_info.setObjectName(u"table_all_info")

        self.gridLayout_3.addWidget(self.table_all_info, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_3)

        self.stackedWidget.addWidget(self.stk_table)

        self.gridLayout_9.addWidget(self.stackedWidget, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_cultivation_monitor_0, "")
        self.tab_water_info_1 = QWidget()
        self.tab_water_info_1.setObjectName(u"tab_water_info_1")
        self.gridLayout_4 = QGridLayout(self.tab_water_info_1)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.stackedWidget_2 = QStackedWidget(self.tab_water_info_1)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stk_table2 = QWidget()
        self.stk_table2.setObjectName(u"stk_table2")
        self.horizontalLayout_4 = QHBoxLayout(self.stk_table2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_3 = QFrame(self.stk_table2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.table_water_info = QTableWidget(self.frame_3)
        if (self.table_water_info.columnCount() < 5):
            self.table_water_info.setColumnCount(5)
        font1 = QFont()
        font1.setFamily(u"Baloo Da 2 SemiBold")
        font1.setPointSize(12)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font1);
        self.table_water_info.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        font2 = QFont()
        font2.setFamily(u"Baloo Da 2 SemiBold")
        font2.setPointSize(11)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font2);
        self.table_water_info.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font1);
        self.table_water_info.setHorizontalHeaderItem(2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font1);
        self.table_water_info.setHorizontalHeaderItem(3, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setFont(font1);
        self.table_water_info.setHorizontalHeaderItem(4, __qtablewidgetitem13)
        self.table_water_info.setObjectName(u"table_water_info")

        self.gridLayout_5.addWidget(self.table_water_info, 0, 0, 1, 1)

        self.btn_start_processing = QPushButton(self.frame_3)
        self.btn_start_processing.setObjectName(u"btn_start_processing")
        self.btn_start_processing.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_start_processing.setStyleSheet(u"QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:356.1, stop:0 rgba(65, 41, 90, 255), stop:1 rgba(47, 7, 67, 255));\n"
"border-radius: 12px;\n"
"}")

        self.gridLayout_5.addWidget(self.btn_start_processing, 1, 0, 1, 1)


        self.horizontalLayout_4.addWidget(self.frame_3)

        self.stackedWidget_2.addWidget(self.stk_table2)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.lbl_message = QLabel(self.page_2)
        self.lbl_message.setObjectName(u"lbl_message")
        self.lbl_message.setGeometry(QRect(140, 160, 551, 131))
        font3 = QFont()
        font3.setFamily(u"Baloo Da 2 SemiBold")
        font3.setPointSize(20)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setWeight(7)
        self.lbl_message.setFont(font3)
        self.lbl_message.setStyleSheet(u"font: 63 20pt \"Baloo Da 2 SemiBold\";")
        self.lbl_message.setAlignment(Qt.AlignCenter)
        self.stackedWidget_2.addWidget(self.page_2)

        self.gridLayout_4.addWidget(self.stackedWidget_2, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_water_info_1, "")
        self.tab_water_preperation_2 = QWidget()
        self.tab_water_preperation_2.setObjectName(u"tab_water_preperation_2")
        self.gridLayout_2 = QGridLayout(self.tab_water_preperation_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_2 = QFrame(self.tab_water_preperation_2)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMaximumSize(QSize(250, 16777215))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_select_tank_wp = QLabel(self.frame_2)
        self.label_select_tank_wp.setObjectName(u"label_select_tank_wp")
        self.label_select_tank_wp.setGeometry(QRect(10, 70, 231, 41))
        self.label_select_tank_wp.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:356.1, stop:0 rgba(65, 41, 90, 255), stop:1 rgba(47, 7, 67, 255));\n"
"font: 63 13pt \"Baloo Da 2 SemiBold\";")
        self.label_select_tank_wp.setAlignment(Qt.AlignCenter)
        self.comboBox_select_tank_wp = QComboBox(self.frame_2)
        self.comboBox_select_tank_wp.setObjectName(u"comboBox_select_tank_wp")
        self.comboBox_select_tank_wp.setGeometry(QRect(10, 120, 231, 31))
        self.comboBox_select_tank_wp.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:356.1, stop:0 rgba(65, 41, 90, 255), stop:1 rgba(47, 7, 67, 255));\n"
"font: 63 12pt \"Baloo Da 2 SemiBold\";")
        self.lineEdit_fish_name = QLineEdit(self.frame_2)
        self.lineEdit_fish_name.setObjectName(u"lineEdit_fish_name")
        self.lineEdit_fish_name.setGeometry(QRect(10, 200, 231, 41))
        self.lineEdit_fish_name.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:356.1, stop:0 rgba(65, 41, 90, 255), stop:1 rgba(47, 7, 67, 255));\n"
"font: 63 13pt \"Baloo Da 2 SemiBold\";")
        self.lineEdit_fish_name.setAlignment(Qt.AlignCenter)
        self.lineEdit_day = QLineEdit(self.frame_2)
        self.lineEdit_day.setObjectName(u"lineEdit_day")
        self.lineEdit_day.setGeometry(QRect(10, 250, 231, 41))
        self.lineEdit_day.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:356.1, stop:0 rgba(65, 41, 90, 255), stop:1 rgba(47, 7, 67, 255));\n"
"font: 63 13pt \"Baloo Da 2 SemiBold\";")
        self.lineEdit_day.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 2, 1)

        self.table_show_tank = QTableWidget(self.tab_water_preperation_2)
        if (self.table_show_tank.columnCount() < 5):
            self.table_show_tank.setColumnCount(5)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setFont(font2);
        self.table_show_tank.setHorizontalHeaderItem(0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setFont(font2);
        self.table_show_tank.setHorizontalHeaderItem(1, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setFont(font);
        self.table_show_tank.setHorizontalHeaderItem(2, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setFont(font);
        self.table_show_tank.setHorizontalHeaderItem(3, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setFont(font);
        self.table_show_tank.setHorizontalHeaderItem(4, __qtablewidgetitem18)
        self.table_show_tank.setObjectName(u"table_show_tank")
        self.table_show_tank.setStyleSheet(u"QTableWidget{\n"
"		background-color: qlineargradient(spread:pad, x1:0.948481, y1:0.074, x2:0, y2:1, stop:0.14433 rgba(35, 181, 239, 255), stop:1 rgba(255, 255, 255, 255));\n"
"   \n"
"}")

        self.gridLayout_2.addWidget(self.table_show_tank, 0, 1, 2, 3)

        self.btn_add_tank = QPushButton(self.tab_water_preperation_2)
        self.btn_add_tank.setObjectName(u"btn_add_tank")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_add_tank.sizePolicy().hasHeightForWidth())
        self.btn_add_tank.setSizePolicy(sizePolicy1)
        self.btn_add_tank.setMaximumSize(QSize(16777215, 35))
        self.btn_add_tank.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_add_tank.setStyleSheet(u"QPushButton{\n"
"\n"
"color: rgb(255, 255, 255);\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:356.1, stop:0 rgba(65, 41, 90, 255), stop:1 rgba(47, 7, 67, 255));\n"
"border-radius: 17px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.btn_add_tank.setCheckable(False)
        self.btn_add_tank.setAutoDefault(False)
        self.btn_add_tank.setFlat(True)

        self.gridLayout_2.addWidget(self.btn_add_tank, 2, 0, 1, 1)

        self.btn_delete_tank = QPushButton(self.tab_water_preperation_2)
        self.btn_delete_tank.setObjectName(u"btn_delete_tank")
        sizePolicy.setHeightForWidth(self.btn_delete_tank.sizePolicy().hasHeightForWidth())
        self.btn_delete_tank.setSizePolicy(sizePolicy)
        self.btn_delete_tank.setMaximumSize(QSize(160, 35))
        self.btn_delete_tank.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_delete_tank.setStyleSheet(u"QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:356.1, stop:0 rgba(65, 41, 90, 255), stop:1 rgba(47, 7, 67, 255));\n"
"border-radius: 15px;\n"
"}")

        self.gridLayout_2.addWidget(self.btn_delete_tank, 2, 1, 1, 1)

        self.btn_prepare_water = QPushButton(self.tab_water_preperation_2)
        self.btn_prepare_water.setObjectName(u"btn_prepare_water")
        sizePolicy1.setHeightForWidth(self.btn_prepare_water.sizePolicy().hasHeightForWidth())
        self.btn_prepare_water.setSizePolicy(sizePolicy1)
        self.btn_prepare_water.setMaximumSize(QSize(16777215, 35))
        font4 = QFont()
        font4.setFamily(u"Baloo Da 2 SemiBold")
        font4.setPointSize(12)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setWeight(7)
        self.btn_prepare_water.setFont(font4)
        self.btn_prepare_water.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_prepare_water.setStyleSheet(u"QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:356.1, stop:0 rgba(65, 41, 90, 255), stop:1 rgba(47, 7, 67, 255));\n"
"border-radius: 17px;\n"
"}")

        self.gridLayout_2.addWidget(self.btn_prepare_water, 2, 2, 1, 2)

        self.tabWidget.addTab(self.tab_water_preperation_2, "")
        self.tab_tank_basic_info_3 = QWidget()
        self.tab_tank_basic_info_3.setObjectName(u"tab_tank_basic_info_3")
        self.horizontalLayout_3 = QHBoxLayout(self.tab_tank_basic_info_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_new_tank_reg = QPushButton(self.tab_tank_basic_info_3)
        self.btn_new_tank_reg.setObjectName(u"btn_new_tank_reg")
        self.btn_new_tank_reg.setMaximumSize(QSize(250, 250))
        font5 = QFont()
        font5.setFamily(u"Baloo Da 2 SemiBold")
        font5.setPointSize(17)
        font5.setBold(False)
        font5.setItalic(False)
        font5.setWeight(7)
        self.btn_new_tank_reg.setFont(font5)
        self.btn_new_tank_reg.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_new_tank_reg.setStyleSheet(u"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:356.1, stop:0 rgba(65, 41, 90, 255), stop:1 rgba(47, 7, 67, 255));\n"
"\n"
"font: 63 17pt \"Baloo Da 2 SemiBold\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.btn_new_tank_reg)

        self.btn_delete_tank_reg = QPushButton(self.tab_tank_basic_info_3)
        self.btn_delete_tank_reg.setObjectName(u"btn_delete_tank_reg")
        self.btn_delete_tank_reg.setMaximumSize(QSize(250, 250))
        self.btn_delete_tank_reg.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_delete_tank_reg.setStyleSheet(u"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:356.1, stop:0 rgba(65, 41, 90, 255), stop:1 rgba(47, 7, 67, 255));\n"
"\n"
"font: 63 15pt \"Baloo Da 2 SemiBold\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.btn_delete_tank_reg)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)

        self.tabWidget.addTab(self.tab_tank_basic_info_3, "")
        self.tab_fish_collection_6 = QWidget()
        self.tab_fish_collection_6.setObjectName(u"tab_fish_collection_6")
        self.verticalLayout_2 = QVBoxLayout(self.tab_fish_collection_6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.btn_fish_collection = QPushButton(self.tab_fish_collection_6)
        self.btn_fish_collection.setObjectName(u"btn_fish_collection")
        sizePolicy1.setHeightForWidth(self.btn_fish_collection.sizePolicy().hasHeightForWidth())
        self.btn_fish_collection.setSizePolicy(sizePolicy1)
        self.btn_fish_collection.setMaximumSize(QSize(16777215, 35))
        self.btn_fish_collection.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_fish_collection.setMouseTracking(False)
        self.btn_fish_collection.setStyleSheet(u"QPushButton{\n"
"\n"
"color: rgb(255, 255, 255);\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:356.1, stop:0 rgba(65, 41, 90, 255), stop:1 rgba(47, 7, 67, 255));\n"
"border-radius: 17px;\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.gridLayout_7.addWidget(self.btn_fish_collection, 1, 1, 1, 1)

        self.table_show_all_tanks = QTableWidget(self.tab_fish_collection_6)
        if (self.table_show_all_tanks.columnCount() < 3):
            self.table_show_all_tanks.setColumnCount(3)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setFont(font2);
        self.table_show_all_tanks.setHorizontalHeaderItem(0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setFont(font2);
        self.table_show_all_tanks.setHorizontalHeaderItem(1, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setFont(font2);
        self.table_show_all_tanks.setHorizontalHeaderItem(2, __qtablewidgetitem21)
        self.table_show_all_tanks.setObjectName(u"table_show_all_tanks")
        self.table_show_all_tanks.setStyleSheet(u"	background-color: qlineargradient(spread:pad, x1:0.948481, y1:0.074, x2:0, y2:1, stop:0.14433 rgba(35, 181, 239, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 63 12pt \"Baloo Da 2 SemiBold\";")

        self.gridLayout_7.addWidget(self.table_show_all_tanks, 0, 0, 1, 2)


        self.verticalLayout_2.addLayout(self.gridLayout_7)

        self.tabWidget.addTab(self.tab_fish_collection_6, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.verticalLayout_4.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)
        self.stackedWidget.setCurrentIndex(1)
        self.stackedWidget_2.setCurrentIndex(0)
        self.btn_add_tank.setDefault(False)


        self.table_water_info.setColumnWidth(4, 150)
        self.table_water_info.setColumnWidth(3, 200)
        self.table_water_info.setColumnWidth(0, 120)
        self.table_water_info.setColumnWidth(1, 100)
        self.table_water_info.setColumnWidth(2, 100)

        self.table_show_all_tanks.setColumnWidth(0, 200)
        self.table_show_all_tanks.setColumnWidth(1, 200)
        self.table_show_all_tanks.setColumnWidth(2, 270)

        self.table_show_tank.setColumnWidth(1, 140)


        QMetaObject.connectSlotsByName(MainWindow)
        ## here is the code
        self.btn_goto_newTankReg.clicked.connect(self.regwin) ## here is the button click
        self.btn_delete_tank_reg.clicked.connect(self.delregwin)
        self.btn_new_tank_reg.clicked.connect(self.regwin)
        
        
        ## here is the code
    def regwin(self):
        self.Form = QtWidgets.QWidget()
        self.ui = uiregform.Ui_Form()
        self.ui.setupUi(self.Form)
        self.Form.show()   

    def delregwin(self):
        self.Form = QtWidgets.QWidget()
        self.ui =  uidelregform.Ui_Form()
        self.ui.setupUi(self.Form)
        self.Form.show() 

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_goto_newTankReg.setText(QCoreApplication.translate("MainWindow", u"\u098f\u0996\u09a8\u09cb \u099a\u09be\u09b7 \u09b6\u09c1\u09b0\u09c1 \u09b9\u09df \u09a8\u09bf\u0964   \u09a8\u09a4\u09c1\u09a8 \u099c\u09b2\u09be\u09a7\u09be\u09b0 \u09a8\u09bf\u09ac\u09a8\u09cd\u09a7\u09a8 \u0995\u09b0\u09c1\u09a8", None))
        ___qtablewidgetitem = self.table_all_info.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u099c\u09b2\u09be\u09a7\u09be\u09b0 \u09a8\u0982 ", None));
        ___qtablewidgetitem1 = self.table_all_info.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u099c\u09b2\u09be\u09a7\u09be\u09b0\u09c7\u09b0 \u0986\u09df\u09a4\u09a8", None));
        ___qtablewidgetitem2 = self.table_all_info.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u09ae\u09be\u099b\u09c7\u09b0 \u09a7\u09b0\u09a3", None));
        ___qtablewidgetitem3 = self.table_all_info.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u099a\u09be\u09b7 \u09b6\u09c1\u09b0\u09c1 \u09a6\u09bf\u09a8", None));
        ___qtablewidgetitem4 = self.table_all_info.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u099a\u09be\u09b7 \u09b6\u09c7\u09b7 \u09b9\u09a4\u09c7 \u0986\u09b0\u09cb \u09ac\u09be\u0995\u09c0 ", None));
        ___qtablewidgetitem5 = self.table_all_info.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u09b2\u09be\u09b8\u09cd\u099f \u099a\u09c7\u0995", None));
        ___qtablewidgetitem6 = self.table_all_info.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"pH", None));
        ___qtablewidgetitem7 = self.table_all_info.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"TDS", None));
        ___qtablewidgetitem8 = self.table_all_info.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u09a4\u09be\u09aa\u09ae\u09be\u09a4\u09cd\u09b0\u09be", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_cultivation_monitor_0), QCoreApplication.translate("MainWindow", u"\u099a\u09be\u09b7 \u09aa\u09b0\u09cd\u09af\u09ac\u09c7\u0995\u09cd\u09b7\u09a3", None))
        ___qtablewidgetitem9 = self.table_water_info.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u099c\u09b2\u09be\u09a7\u09be\u09b0 \u09a8\u0982 ", None));
        ___qtablewidgetitem10 = self.table_water_info.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\u099c\u09b2\u09be\u09a7\u09be\u09b0\u09c7\u09b0 \u0986\u09df\u09a4\u09a8", None));
        ___qtablewidgetitem11 = self.table_water_info.horizontalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"pH", None));
        ___qtablewidgetitem12 = self.table_water_info.horizontalHeaderItem(3)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"TDS", None));
        ___qtablewidgetitem13 = self.table_water_info.horizontalHeaderItem(4)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"\u09ae\u09a8\u09cd\u09a4\u09ac\u09cd\u09af", None));
        self.btn_start_processing.setText(QCoreApplication.translate("MainWindow", u"\u09aa\u09c1\u09a8\u09b0\u09be\u09df \u09aa\u09cd\u09b0\u09b8\u09cd\u09a4\u09c1\u09a4\u09bf \u0995\u09b0\u09c1\u09a8", None))
        self.lbl_message.setText(QCoreApplication.translate("MainWindow", u"\u098f\u0996\u09a8\u09cb \u0995\u09cb\u09a8 \u099c\u09b2\u09be\u09a7\u09be\u09b0\u09c7 \u09aa\u09be\u09a8\u09bf \u09aa\u09cd\u09b0\u09b8\u09cd\u09a4\u09c1\u09a4\u09bf \u09b6\u09c1\u09b0\u09c1 \u09b9\u09df\u09a8\u09bf", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_water_info_1), QCoreApplication.translate("MainWindow", u"\u09aa\u09be\u09a8\u09bf \u09aa\u09cd\u09b0\u09b8\u09cd\u09a4\u09a4\u09bf \u09a4\u09a5\u09cd\u09af\u09b8\u09ae\u09c2\u09b9 ", None))
        self.label_select_tank_wp.setText(QCoreApplication.translate("MainWindow", u"\u099c\u09b2\u09be\u09a7\u09be\u09b0 \u09a8\u09bf\u09b0\u09cd\u09ac\u09be\u099a\u09a8 \u0995\u09b0\u09c1\u09a8", None))
        self.lineEdit_fish_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u09ae\u09be\u099b\u09c7\u09b0 \u09a8\u09be\u09ae", None))
        self.lineEdit_day.setText("")
        self.lineEdit_day.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u09a6\u09bf\u09a8 \u09b8\u0982\u0996\u09cd\u09af\u09be ", None))
        ___qtablewidgetitem14 = self.table_show_tank.horizontalHeaderItem(0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"\u099c\u09b2\u09be\u09a7\u09be\u09b0 \u09a8\u0982 ", None));
        ___qtablewidgetitem15 = self.table_show_tank.horizontalHeaderItem(1)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"\u099c\u09b2\u09be\u09a7\u09be\u09b0 \u0986\u09df\u09a4\u09a8", None));
        ___qtablewidgetitem16 = self.table_show_tank.horizontalHeaderItem(2)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"\u09ae\u09be\u099b\u09c7\u09b0 \u09a8\u09be\u09ae", None));
        ___qtablewidgetitem17 = self.table_show_tank.horizontalHeaderItem(3)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"\u09a6\u09bf\u09a8 \u09b8\u0982\u0996\u09cd\u09af\u09be ", None));
        ___qtablewidgetitem18 = self.table_show_tank.horizontalHeaderItem(4)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"\u09a4\u09be\u09b0\u09bf\u0996", None));
        self.btn_add_tank.setText(QCoreApplication.translate("MainWindow", u"\u09af\u09cb\u0997 \u0995\u09b0\u09c1\u09a8", None))
        self.btn_delete_tank.setText(QCoreApplication.translate("MainWindow", u"\u099c\u09b2\u09be\u09a7\u09be\u09b0 \u09ac\u09be\u09a4\u09bf\u09b2 \u0995\u09b0\u09c1\u09a8", None))
        self.btn_prepare_water.setText(QCoreApplication.translate("MainWindow", u"\u09aa\u09be\u09a8\u09bf \u09aa\u09cd\u09b0\u09b8\u09cd\u09a4\u09c1\u09a4\u09bf \u0986\u09b0\u09ae\u09cd\u09ad \u0995\u09b0\u09c1\u09a8", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_water_preperation_2), QCoreApplication.translate("MainWindow", u"\u09aa\u09be\u09a8\u09bf \u09aa\u09cd\u09b0\u09b8\u09cd\u09a4\u09c1\u09a4\u09bf \u09aa\u09b0\u09cd\u09af\u09be\u09df", None))
        self.btn_new_tank_reg.setText(QCoreApplication.translate("MainWindow", u"\u09a8\u09a4\u09c1\u09a8 \u099c\u09b2\u09be\u09a7\u09be\u09b0 \u09a8\u09bf\u09ac\u09a8\u09cd\u09a7\u09a8", None))
        self.btn_delete_tank_reg.setText(QCoreApplication.translate("MainWindow", u"\u099c\u09b2\u09be\u09a7\u09be\u09b0 \u09a8\u09bf\u09ac\u09a8\u09cd\u09a7\u09a8 \u09ac\u09be\u09a4\u09bf\u09b2\u0995\u09b0\u09a8", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_tank_basic_info_3), QCoreApplication.translate("MainWindow", u"\u099c\u09b2\u09be\u09a7\u09be\u09b0 \u09a4\u09a5\u09cd\u09af \u09ac\u09cd\u09af\u09ac\u09b8\u09cd\u09a5\u09be\u09aa\u09a8\u09be", None))
        self.btn_fish_collection.setText(QCoreApplication.translate("MainWindow", u"\u09ae\u09be\u099b \u0989\u09a4\u09cd\u09a4\u09cb\u09b2\u09a8 \u0995\u09b0\u09c1\u09a8 ", None))
        ___qtablewidgetitem19 = self.table_show_all_tanks.horizontalHeaderItem(0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"\u099c\u09b2\u09be\u09a7\u09be\u09b0 \u09a8\u0982", None));
        ___qtablewidgetitem20 = self.table_show_all_tanks.horizontalHeaderItem(1)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"\u09ae\u09be\u099b", None));
        ___qtablewidgetitem21 = self.table_show_all_tanks.horizontalHeaderItem(2)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"\u099a\u09be\u09b7 \u09b6\u09c1\u09b0\u09c1\u09b0 \u09a4\u09be\u09b0\u09bf\u0996", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_fish_collection_6), QCoreApplication.translate("MainWindow", u"\u09ae\u09be\u099b \u0989\u09a4\u09cd\u09a4\u09cb\u09b2\u09a8", None))
    # retranslateUi

