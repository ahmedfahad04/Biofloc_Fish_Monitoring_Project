from threading import Thread
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import test 

import time

class Worker(QRunnable):
    '''
    Worker thread
    '''

    @pyqtSlot()
    def run(self):
        '''
        Your code goes in this function
        '''
        print("Thread start")
        print("Thread complete")




class MainWindow(QMainWindow):


    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # kahini 1
        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())


        self.counter = 0

        layout = QVBoxLayout()

        self.l = QLabel("Start")
        b = QPushButton("DANGER!")

        

        # b.pressed.connect(self.popup)

        layout.addWidget(self.l)
        layout.addWidget(b)

        w = QWidget()
        w.setLayout(layout)

        self.setCentralWidget(w)

        

        self.show()

        # kahini 2
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.recurring_timer)
        self.timer.start()

       

    def oh_no(self):
        worker = Worker()
        self.threadpool.start(worker)

    def recurring_timer(self):

        worker = Worker()
        t1 = Thread(target=worker.run)
        t1.start()
        t1.join()

        # self.threadpool.start(worker)


        self.counter +=1
        self.l.setText("Counter: %d" % self.counter)
      

    def msgBox(self,message, myicon):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(myicon)
        msg.setText(message)
        msg.setWindowTitle("Confirm Password")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        msg.setFont(QFont("Baloo Da 2",12))
        msg.exec_()

    def popup(self):
        
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
        self.hide()
        win.show()

        value = 0
        def showtxt():
            info = txt.text()
            if info == '1234':
                print("Bingo!!")
                txt.clear()
                self.msgBox("অভিনন্দন! আপনার তথ্য সংরক্ষণ করা হয়েছে।", QtWidgets.QMessageBox.Information)
                value = 1
                win.hide() 
                self.show()
            else:
                print("Failed!")
                txt.clear()
                self.msgBox("আপনি ভুল পাসওয়ার্ড দিয়েছেন। আবার চেষ্টা করুন।", QtWidgets.QMessageBox.Warning)

        # execute the application


app = QApplication([])
window = MainWindow()
app.exec_()
