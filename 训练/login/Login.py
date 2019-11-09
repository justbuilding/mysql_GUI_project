# -*- coding:utf-8 -*-
# Author: Jay-Q
import sys
from PyQt5.QtWidgets import QDialog
#重点和秘诀就在这里，大家注意看
from PyQt5.uic import loadUi
from ui_login import ui_login

class Login(QDialog):
    """登录窗口"""
    def __init__(self, *args):
        super(Login, self).__init__(*args)
        loadUi('Login.ui', self)   #看到没，瞪大眼睛看
        self.labelTips.hide()
        self.pushButtonOK.clicked.connect(self.slotLogin)
        self.pushButtonCancle.clicked.connect(self.slotCancle)

    def slotLogin(self):
        if self.lineEditUser.text() != "admin" or self.lineEditPasswd.text() != "123456":
            self.labelTips.show()
            self.labelTips.setText("用户名或密码错误！")
        else:
            self.accept()

    def slotCancle(self):
        self.reject()