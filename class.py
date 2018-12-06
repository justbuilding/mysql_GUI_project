# class Geese:
#     '''大雁类'''
#     def __init__(self,beak,wing,claw):
#         print("我是大雁类，我有以下特征:")
#         print(beak)
#         print(wing)
#         print(claw)
#
# beak_1 = "啄的长度和头部长度几乎相等"
# wing_1 = "翅膀长而尖"
# claw1 = "爪子是蹼状的"
#
# wildGoose = Geese(beak_1,wing_1,claw1)

# import sys
# def show_MainWindow():
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec())
#
# if __name__ == "__main__":
#     show_MainWindow()

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication, QHBoxLayout, QVBoxLayout)

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.Init_UI()
    def Init_UI(self):
        self.setGeometry(300,300,400,300)
        self.setWindowTitle('学点编程吧')

        bt1 = QPushButton('剪刀', self)
        bt2 = QPushButton('石头', self)
        bt3 = QPushButton('布', self)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(bt1)
        hbox.addWidget(bt2)
        hbox.addWidget(bt3)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exit(app.exec_())