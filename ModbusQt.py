#ModbusQt

import os
import sys
import sqlite3

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

date=15
month=6
year=2017
hour=15
minute=0
second=0

class ModbusQt(QMainWindow):
    "This Class creates the main window for the ModbusQT"

    #constructor
    def __init__(self):
        QMainWindow.__init__(self)  #call super class contructor        self.setWindowTitle("ModbusQt")  #set the Window title
        self.setWindowTitle("Uniphos ModbusPi")

        #font properties for the text to be displayed inside status bar
        font = QFont()
        font.setPointSize(11)
        font.setWeight(30)
        self.statusBar_msg = QLabel()
        self.statusBar_msg.setFont(font)

        color = QColor()
        
        self.stacked_layout = QStackedLayout()
        self.window1()
        self.stacked_layout.addWidget(self.modbusQt_widget)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.stacked_layout)
        self.setCentralWidget(self.central_widget)
        self.stacked_layout.setCurrentIndex(0)

    def window1(self):
        self.date = QLabel("{:02d}-{:02d}-{:04d}".format(date,month,year))
        self.time = QLabel("{:02d}:{:02d}:{:02d}".format(hour,minute,second))
        self.clock_layout = QHBoxLayout()
        self.clock_layout.addWidget(self.date)
        self.clock_layout.addWidget(self.time)
        self.initial_layout = QVBoxLayout()
        self.initial_layout.addLayout(self.clock_layout)
        

        self.modbusQt_widget = QWidget()
        self.modbusQt_widget.setLayout(self.initial_layout)

def main():
    modbus_qt = QApplication(sys.argv)
    modbus_qt_window = ModbusQt()
    modbus_qt_window.show()
    modbus_qt_window.raise_() #raise instance to top of window stack
    modbus_qt.exec()

if __name__=="__main__":
    main()
