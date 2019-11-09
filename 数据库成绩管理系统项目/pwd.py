# -*- coding:utf-8 -*-
# Author: Jay-Q
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import pymysql
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class pwd_MainWindow(QtWidgets.QMainWindow):
    #初始化界面
    def __init__(self):
        super(pwd_MainWindow,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
    #窗口内各种物件大小和位置
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(386, 127)

        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit.setGeometry(QtCore.QRect(165, 20, 100, 20))
        self.lineEdit.setText("")
        self.lineEdit.setContextMenuPolicy(Qt.NoContextMenu)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(165, 50, 100, 20))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setContextMenuPolicy(Qt.NoContextMenu)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(100, 24, 45, 15))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(100, 54, 45, 15))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(110, 90, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 90, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralWidget)
        #按钮连接
        self.pushButton.clicked.connect(self.word_get)
        self.pushButton_2.clicked.connect(MainWindow.close)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "密码修改界面"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "请输入密码"))
        self.lineEdit.setContextMenuPolicy(Qt.NoContextMenu)
        self.lineEdit_2.setContextMenuPolicy(Qt.NoContextMenu)
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "再次输入密码"))#设置QLineEdit对象的上下文菜单的策略,使得密码输入框无法右键菜单复制
        self.label.setText(_translate("MainWindow", "新密码"))
        self.label_2.setText(_translate("MainWindow", "新密码"))
        self.pushButton.setText(_translate("MainWindow", "确定"))
        self.pushButton_2.setText(_translate("MainWindow", "取消"))

    def word_get(self):
        c_pwd1= self.lineEdit.text()
        c_pwd2 = self.lineEdit_2.text()
        if c_pwd1 == c_pwd2:
            con = pymysql.connect('localhost', 'root', 'hjj111', 'mydb')
            with con:
                myCursor = con.cursor()
                sql = "update client set c_pwd=%s where c_name='s2'" %''.join(c_pwd1)
                myCursor.execute(sql)
                print('Data updated successfully')
        else:
            QMessageBox.warning(self,
                    "警告",
                    "两次输入不一致！",
                    QMessageBox.Yes)
            self.lineEdit.setFocus()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = pwd_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
