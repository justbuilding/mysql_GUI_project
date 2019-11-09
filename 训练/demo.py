# -*- coding:utf-8 -*-
# Author: Jay-Q
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication
import login

app = QApplication(sys.argv)
Login = login.login()
if Login.exec():
    print("登录成功")
else:
    print("登录退出")
sys.exit(app.exec())
