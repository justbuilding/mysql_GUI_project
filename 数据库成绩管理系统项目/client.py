# -*- coding:utf-8 -*-
# Author: Jay-Q
from PyQt5.QtWidgets import QApplication
import pymysql
from system import *
from PyQt5 import QtCore, QtGui, QtWidgets

class user_mainWindow2(QtWidgets.QMainWindow):
    def __init__(self):
        super(user_mainWindow2,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

    def ui_system(self):
        ui_system.show()
        mainWindow2.close()

    def list_clear(self):
        self.tableWidget.clearContents()
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(1)

    def load_data(self):
        conn = pymysql.connect("localhost","root","hjj111","mydb")
        with conn:
            cursor = conn.cursor()
            query = "select * from client"
            cursor.execute(query)
            result1 = cursor.fetchall()
            self.tableWidget.setRowCount(0)

            for stock_id,row_data in enumerate(result1):
                self.tableWidget.insertRow(stock_id)
                for column_number,data in enumerate(row_data):
                    self.tableWidget.setItem(stock_id,column_number,QtWidgets.QTableWidgetItem(str(data)))

    def add_client(self):
        c_id1 = [self.tableWidget.item(row, 0).text() for row in range(self.tableWidget.rowCount())]
        c_name1 = [self.tableWidget.item(row, 1).text() for row in range(self.tableWidget.rowCount())]
        c_phone1 = [self.tableWidget.item(row, 2).text() for row in range(self.tableWidget.rowCount())]
        c_pwd1 = [self.tableWidget.item(row, 3).text() for row in range(self.tableWidget.rowCount())]

        con = pymysql.connect('localhost', 'root', 'hjj111', 'mydb')
        with con:
            cursor = con.cursor()
            cursor.execute("insert into client values('%s' ,'%s', '%s', '%s')" % (''.join(c_id1),
                                                                         ''.join(c_name1),''.join(c_phone1),''.join(c_pwd1)))
            print('Data inserted successfully')


    def delete_client(self):
        c_id1 = [self.tableWidget.item(row, 0).text() for row in range(self.tableWidget.rowCount())]
        con = pymysql.connect('localhost', 'root', 'hjj111', 'mydb')
        with con:
            cursor = con.cursor()
            cursor.execute("delete from client where c_id = '%s' " % ''.join(c_id1))
            print('Data deleted successfully')


    def setupUi(self, mainWindow2):
        mainWindow2.setObjectName("mainWindow2")
        mainWindow2.resize(900, 600)
        self.centralwidget = QtWidgets.QWidget(mainWindow2)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(390, 30, 70, 21))
        self.lineEdit.setObjectName("lineEdit")

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 70, 901, 441))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)

        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(200, 530, 80, 28))
        self.pushButton2.setObjectName("pushButton")
        self.pushButton2.clicked.connect(self.load_data)
        self.pushButton3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton3.setGeometry(QtCore.QRect(330, 530, 80, 28))
        self.pushButton3.setObjectName("pushButton")
        self.pushButton3.clicked.connect(self.list_clear)
        self.pushButton4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton4.setGeometry(QtCore.QRect(460, 530, 80, 28))
        self.pushButton4.setObjectName("pushButton")
        self.pushButton4.clicked.connect(self.add_client)
        self.pushButton5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton5.setGeometry(QtCore.QRect(590, 530, 80, 28))
        self.pushButton5.setObjectName("pushButton")
        self.pushButton5.clicked.connect(self.delete_client)
        mainWindow2.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow2)
        self.statusbar.setObjectName("statusbar")
        mainWindow2.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow2)
        QtCore.QMetaObject.connectSlotsByName(mainWindow2)

    def retranslateUi(self, mainWindow2):
        _translate = QtCore.QCoreApplication.translate
        mainWindow2.setWindowTitle(_translate("mainWindow2", "mainWindow2"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("mainWindow2", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("mainWindow2", "c_id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("mainWindow2", "c_name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("mainWindow2", "c_phone"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("mainWindow2", "c_pwd"))
        self.lineEdit.setText(_translate("mainWindow2", "client表"))
        self.pushButton2.setText(_translate("mainWindow2", "加载客户"))
        self.pushButton3.setText(_translate("mainWindow2", "列表清空"))
        self.pushButton4.setText(_translate("mainWindow2", "添加客户"))
        self.pushButton5.setText(_translate("mainWindow2", "删除客户"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow2 = QtWidgets.QMainWindow()
    ui = user_mainWindow2()
    ui_system = system_MainWindow1()
    ui.setupUi(mainWindow2)
    mainWindow2.show()
    sys.exit(app.exec_())


