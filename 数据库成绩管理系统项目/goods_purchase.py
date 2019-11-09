# -*- coding:utf-8 -*-
# Author: Jay-Q
from PyQt5.QtWidgets import QApplication
import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets, Qt

class gpurchase_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(gpurchase_MainWindow,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

    def load_data(self):
        conn = pymysql.connect("localhost","root","hjj111","mydb")
        with conn:
            cursor = conn.cursor()
            query = "select * from goods"
            cursor.execute(query)
            result1 = cursor.fetchall()
            self.tableWidget.setRowCount(0)

            for stock_id,row_data in enumerate(result1):
                self.tableWidget.insertRow(stock_id)
                for column_number,data in enumerate(row_data):
                    self.tableWidget.setItem(stock_id,column_number,QtWidgets.QTableWidgetItem(str(data)))

    def trade_insert_data(self):
        stock_id1 = self.lineEdit3.text()
        stock_num1 = self.lineEdit_2.text()
        stock_id2 = int(stock_id1)
        con = pymysql.connect('localhost', 'root', 'hjj111', 'mydb')
        with con:
            cursor = con.cursor()
            c_id1 = cursor.execute("select c_id from client where c_name='s2'")
            stock_price1 = cursor.execute("select stock_price from goods where stock_id = %d" % stock_id2)
            stock_price2 = float(stock_id1)
            print(stock_price1)
            total_price1 = float(stock_price1) * float(stock_num1)
            cursor.execute("insert into trade values('%s' ,'%s', '%s', '%s', '%s')" % (''.join(c_id1),
                                                                         ''.join(stock_id1),''.join(stock_num1),''.join(stock_price2),''.join(total_price1)))
            print('Goods purchased successfully')

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(390, 30, 75, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit3.setGeometry(QtCore.QRect(330, 530, 80, 28))
        self.lineEdit3.setText("请输入id")
        self.lineEdit3.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(460, 530, 80, 28))
        self.lineEdit_2.setText("请输入数量")
        self.lineEdit_2.setObjectName("lineEdit_2")

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
        self.pushButton5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton5.setGeometry(QtCore.QRect(590, 530, 80, 28))
        self.pushButton5.setObjectName("pushButton")
        self.pushButton5.clicked.connect(self.trade_insert_data)
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
        self.lineEdit.setText(_translate("MainWindow", "goods商城"))
        self.pushButton2.setText(_translate("MainWindow", "加载货物"))
        self.pushButton5.setText(_translate("MainWindow", "购买货物"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = gpurchase_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())