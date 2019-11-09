# -*- coding:utf-8 -*-
# Author: Jay-Q
import  sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox,QLineEdit
import pymysql

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Insert Data"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500
        self.InitWindow()

    def InitWindow(self):
        self.lineedit1 = QLineEdit(self)
        self.lineedit1.setPlaceholderText('请输入编号')
        self.lineedit1.setGeometry(200,100,200,30)

        self.lineedit2 = QLineEdit(self)
        self.lineedit2.setPlaceholderText('请输入名字')
        self.lineedit2.setGeometry(200,150,200,30)

        self.lineedit3 = QLineEdit(self)
        self.lineedit3.setPlaceholderText('请输入密码')
        self.lineedit3.setGeometry(200,200,200,30)

        self.button = QPushButton('插入数据',self)
        self.button.setGeometry(200,250,100,30)
        self.button.clicked.connect(self.InsertData)

        self.setWindowTitle(self.title)
        self.setGeometry(self.top,self.left,self.width,self.height)
        self.show()

    def InsertData(self):
        con = pymysql.connect("localhost","root","hjj111","travel_database")

        with con:
            cursor = con.cursor()
            cursor.execute("INSERT INTO travel_database.admin values('%s', '%s',  '%s')"% (''.join(self.lineedit1.text()),
                                                                                           ''.join(self.lineedit2.text()),
                                                                                           ''.join(self.lineedit3.text())))
            QMessageBox.about(self,'Connection','插入数据成功')
            self.close()


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())