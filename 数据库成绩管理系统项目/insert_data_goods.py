# -*- coding:utf-8 -*-
# Author: Jay-Q
from PyQt5.QtWidgets import QApplication
import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets

class insert_data_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(insert_data_MainWindow,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

    def insert_data(self):
        stock_id = [self.tableWidget.item(row, 0).text() for row in range(self.tableWidget.rowCount())]
        stock_name = [self.tableWidget.item(row, 1).text() for row in range(self.tableWidget.rowCount())]
        stock_num = [self.tableWidget.item(row, 2).text() for row in range(self.tableWidget.rowCount())]
        stock_price = [self.tableWidget.item(row, 3).text() for row in range(self.tableWidget.rowCount())]
        stock_kind = [self.tableWidget.item(row, 4).text() for row in range(self.tableWidget.rowCount())]
        stock_expiration_dates= [self.tableWidget.item(row, 5).text() for row in range(self.tableWidget.rowCount())]
        stock_days= [self.tableWidget.item(row, 6).text() for row in range(self.tableWidget.rowCount())]

        con = pymysql.connect('localhost', 'root', 'hjj111', 'mydb')
        with con:
            cursor = con.cursor()
            cursor.execute("insert into goods values('%s' ,'%s', '%s', '%s', '%s', '%s', '%s')" % (''.join(stock_id),
                                                                         ''.join(stock_name),''.join(stock_num),''.join(stock_price),''.join(stock_kind),''.join(stock_expiration_dates),
                                                                         ''.join(stock_days)))
            print('Data inserted successfully')

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(390, 30, 134, 21))
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

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(400, 530, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.insert_data)



        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "stock_id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "stock_name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "stock_num"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "stock_price"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "stock_kind"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "expiration_dates"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "stock_days"))
        self.lineEdit.setText(_translate("MainWindow", "插入数据到goods表"))
        self.pushButton.setText(_translate("MainWindow", "商品入库"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = insert_data_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

