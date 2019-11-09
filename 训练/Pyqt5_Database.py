# -*- coding:utf-8 -*-
# Author: Jay-Q
import  sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
import pymysql

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "PyQt Connecting Database"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500
        self.InitWindow()

    def InitWindow(self):
        self.button = QPushButton('DB Connection Status',self)
        self.button.setGeometry(100,100,200,50)
        self.button.clicked.connect(self.connectDB)

        self.setWindowTitle(self.title)
        self.setGeometry(self.top,self.left,self.width,self.height)
        self.show()

    def connectDB(self):
        try:
            db = pymysql.connect("localhost","root","hjj111","travel_database")
            QMessageBox.about(self,'Connection','Successfully Connected To DB')

        except pymysql.Error as e:
            QMessageBox.about(self,'Connection','Not Connected Successfully')
            sys.exit(1)

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())