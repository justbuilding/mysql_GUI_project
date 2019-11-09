# -*- coding:utf-8 -*-
# Author: Jay-Q
from pwd import *
from trade import *
from insert_data_goods import *
from PyQt5 import QtCore, QtGui, QtWidgets
from goods_purchase import *

class user_system_MainWindow1(QtWidgets.QMainWindow):
    def __init__(self):
        super(user_system_MainWindow1,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

    def trade_management(self):
        trade_management.show()

    def goods_insert_management(self):
        goods_insert_management.show()

    def user_management(self):
        ui_management.show()


    def setupUi(self, MainWindow1):
        MainWindow1.setObjectName("MainWindow1")
        MainWindow1.resize(232, 221)
        self.centralwidget = QtWidgets.QWidget(MainWindow1)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(70, 60, 95, 100))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.trade_management)
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.goods_insert_management)
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.user_management)
        self.verticalLayout.addWidget(self.pushButton_3)
        MainWindow1.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow1)
        self.statusbar.setObjectName("statusbar")
        MainWindow1.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow1)

    def retranslateUi(self, MainWindow1):
        _translate = QtCore.QCoreApplication.translate
        MainWindow1.setWindowTitle(_translate("MainWindow1", "user_system"))
        self.pushButton.setText(_translate("MainWindow1", "购物车"))
        self.pushButton_2.setText(_translate("MainWindow1", "商品购买"))
        self.pushButton_3.setText(_translate("MainWindow1", "修改密码"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow1 = QtWidgets.QMainWindow()
    ui = user_system_MainWindow1()
    ui_management = pwd_MainWindow()
    trade_management = trade_MainWindow()
    goods_insert_management = gpurchase_MainWindow()
    ui.setupUi(MainWindow1)
    MainWindow1.show()
    sys.exit(app.exec_())

