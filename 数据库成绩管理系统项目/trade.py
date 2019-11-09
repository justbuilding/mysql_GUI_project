# -*- coding:utf-8 -*-
# Author: Jay-Q
from PyQt5.QtWidgets import QApplication
import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets

class trade_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(trade_MainWindow,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

    def list_clear(self):
        self.tableWidget.clearContents()
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(1)

    def delete_goods(self):
        stock_id1 = [self.tableWidget.item(row, 0).text() for row in range(self.tableWidget.rowCount())]
        con = pymysql.connect('localhost', 'root', 'hjj111', 'mydb')
        with con:
            cursor = con.cursor()
            cursor.execute("delete from trade where stock_id1 = '%s' " % ''.join(stock_id1))
            print('Data deleted successfully')

    def load_data(self):
        conn = pymysql.connect("localhost","root","hjj111","mydb")
        with conn:
            cursor = conn.cursor()
            query = "select * from trade"
            cursor.execute(query)
            result1 = cursor.fetchall()
            self.tableWidget.setRowCount(0)

            for stock_id,row_data in enumerate(result1):
                self.tableWidget.insertRow(stock_id)
                for column_number,data in enumerate(row_data):
                    self.tableWidget.setItem(stock_id,column_number,QtWidgets.QTableWidgetItem(str(data)))

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
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
        self.pushButton2.setGeometry(QtCore.QRect(200, 530, 120, 28))
        self.pushButton2.setObjectName("pushButton")
        self.pushButton2.clicked.connect(self.load_data)

        self.pushButton3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton3.setGeometry(QtCore.QRect(400, 530, 90, 28))
        self.pushButton3.setObjectName("pushButton")
        self.pushButton3.clicked.connect(self.list_clear)

        self.pushButton4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton4.setGeometry(QtCore.QRect(570, 530, 90, 28))
        self.pushButton4.setObjectName("pushButton")
        self.pushButton4.clicked.connect(self.delete_goods)




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
        item.setText(_translate("MainWindow", "c_id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "stock_id"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "stock_num"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "stock_price"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "total_price"))

        self.lineEdit.setText(_translate("MainWindow", "购物车表"))
        self.pushButton2.setText(_translate("MainWindow", "加载购物车"))
        self.pushButton3.setText(_translate("MainWindow", "清空列表"))
        self.pushButton4.setText(_translate("MainWindow", "删除商品"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = trade_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

