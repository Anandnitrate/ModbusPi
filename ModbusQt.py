#ModbusQt

import os
import sys
import sqlite3
import minimalmodbus

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

date=15
month=6
year=2017
hour=15
minute=0
second=0
inst_name='TSS'
inst_unit='%'

inst_conc=73.36

inst_rangeLow=0
inst_rangeHigh=100

inst_resolution = 0.01


c_date=15
c_month=6
c_year=2017


class ModbusQt(QMainWindow):
    "This Class creates the main window for the ModbusQT"

    #constructor
    def __init__(self):
        #Modbus Configuration
        minimalmodbus.BAUDRATE=9600
        minimalmodbus.PARITY='N'
        minimalmodbus.BYTESIZE=8
        minimalmodbus.STOPBITS=1
        minimalmodbus.TIMEOUT=0.05
        minimalmodbus.CLOSE_PORT_AFTER_EACH_CALL=False

        #Qt Configurations
        QMainWindow.__init__(self)  #call super class contructor        self.setWindowTitle("ModbusQt")  #set the Window title
        self.setWindowTitle("Uniphos ModbusPi")

        #font properties for the text to be displayed inside status bar
        font = QFont()
        font.setPointSize(11)
        font.setWeight(30)
        self.statusBar_msg = QLabel()
        self.statusBar_msg.setFont(font)
        
        self.stacked_layout = QStackedLayout()
        self.window1()
        self.stacked_layout.addWidget(self.modbusQt_widget)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.stacked_layout)
        self.setCentralWidget(self.central_widget)
        self.stacked_layout.setCurrentIndex(0)

    def window1(self):
        """ Frame1 of the Application """

        font = QFont()
        font.setPointSize(11)
        font.setWeight(30)

        inst = minimalmodbus.Instrument('/dev/ttyUSB0',1,mode='rtu')
        date=inst.read_register(0,0,4)
        month=inst.read_register(1,0,4)
        year=inst.read_register(2,0,4)
        hour=inst.read_register(0,0,3)
        minute=inst.read_register(1,0,3)
        second=inst.read_register(2,0,3)
        c_date=inst.read_register(6,0,4)
        c_month=inst.read_register(7,0,4)
        c_year=inst.read_register(8,0,4)
        inst_conc=inst.read_register(35,0,4)
        
        #Date and Time Display
        self.date = QLabel("{:02d}-{:02d}-{:04d}".format(date,month,year))
        self.date.setAlignment(Qt.AlignLeft)
        self.time = QLabel("{:02d}:{:02d}:{:02d}".format(hour,minute,second))
        self.time.setAlignment(Qt.AlignRight)
        self.clock_layout = QHBoxLayout()
        self.clock_layout.addWidget(self.date)
        self.clock_layout.addWidget(self.time)

        #Concentration Display
        self.conc = QLabel("{:s} : {:03.2f}{:s}".format(inst_name,inst_conc,inst_unit))
        self.conc.setAlignment(Qt.AlignCenter)
        self.conc.font()

        #Range, LastCalibrationDate, LastZeroedDate, Serial No
        self.misc_layout = QGridLayout()
        self.frame = QFrame()
        self.frame.setLineWidth(10)
        self.frame.setMidLineWidth(5)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setFrameShape(QFrame.StyledPanel)

        
        self.rangeLabel = QLabel("Range")
        self.rangeValue = QLabel("{:d}-{:d}{:s}".format(inst_rangeLow,inst_rangeHigh,inst_unit))
        
        self.resolutionLabel = QLabel("Resolution")
        self.resolutionValue = QLabel("{:0.2f}{:s}".format(inst_resolution,inst_unit))
        
        self.lastCalibrationLabel = QLabel("Last Calibration")
        self.lastCalibrationValue = QLabel("{:02d}-{:02d}-{:04d}".format(c_date,c_month,c_year))

        self.misc_layout.addWidget(self.rangeLabel,0,0)
        self.misc_layout.addWidget(self.rangeValue,0,1)

        self.misc_layout.addWidget(self.resolutionLabel,1,0)
        self.misc_layout.addWidget(self.resolutionValue,1,1)
        
        self.misc_layout.addWidget(self.lastCalibrationLabel,2,0)
        self.misc_layout.addWidget(self.lastCalibrationValue,2,1)
        
        self.initial_layout = QVBoxLayout()
        self.initial_layout.addLayout(self.clock_layout)
        self.initial_layout.addWidget(self.conc)
        self.initial_layout.addLayout(self.misc_layout)

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
