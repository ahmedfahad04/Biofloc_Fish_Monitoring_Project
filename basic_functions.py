import sqlite3
from PyQt5.QtWidgets import *

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem

def connect_to_database(DbName, tableName):

    try:
        connection = sqlite3.connect(DbName)
        print("Database connected")
    except:
        print("Failed to connect with database.")

    cur = connection.cursor()
    query = "SELECT * FROM {}".format(tableName)

    return cur.execute(query)



