# -*- coding:utf-8 -*-
# Author: Jay-Q
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication
import Login

app = QApplication(sys.argv)
login = Login.Login()
if login.exec():
    print("登录成功")
else:
    print("登录退出")
sys.exit(app.exec())
