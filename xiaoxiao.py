# # -*- coding:utf-8 -*-
# # Author: Jay-Q
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget
# #QtWidgets模块包含了一整套UI元素组件，用于建立符合系统风格的classic界面，非常方便。同时为了更方便的使用我们还明确了使用QtWidgets模块中的QApplication, QWidget。
# if __name__ == '__main__':
#
#     app = QApplication(sys.argv)
# #每个PyQt5应用程序必须创建一个应用程序对象。 sys.argv参数是来自命令行的参数列表。 Python脚本可以从shell运行。 写了这句话就能让我们的程序从命令行启动。
#     w = QWidget()
#     w.resize(250, 150)
#     w.move(300, 300)
#     w.setWindowTitle('学点编程吧出品')
#     w.show()
# #show（）方法在屏幕上显示窗口小部件。 一个小部件首先在内存中创建，然后在屏幕上显示。
#     sys.exit(app.exec_())
# #我们进入应用程序的主循环(main loop)。 事件处理从这一点开始。 主循环(main loop)从窗口系统接收事件并将它们分派到应用程序小部件。 如果我们调用exit（）方法或者主窗口小部件被破坏，那么主循环(main loop)就会结束
# #sys.exit（）方法确保一个干净的退出。
# #exec_（）方法有一个下划线。 这是因为exec是一个Python关键字。 因此，使用exec_（）
# #主循环(main loop)简单的谈一下。GUI应用程序都是事件驱动的。比如键盘事件、鼠标事件等等。还有一些事件来自于系统内部，比如定时事件、其它文件事件等等。在没有任何事件的情况下，应用程序处于睡眠状态。这种事件驱动机制，GUI应用程序都需要一个主循环(main loop)。
# # 主循环(main loop)控制应用程序什么时候进入睡眠状态，什么时候被唤醒。所以主循环(main loop)就是干这个的。

# #命令行中如果带入参数，窗口的标题就用这个参数代替，否则用默认的“学点编程吧出品”作为窗口的标题。当输入多个参数时，则合并这些参数为一个
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget
#
# if __name__ == '__main__':
#
#    app = QApplication(sys.argv)
#    try:
#        if len(sys.argv) < 2:
#            raise ValueError
#        else:
#            title = " ".join(sys.argv[1:])
#    except ValueError:
#        title = "学点编程吧出品"
#
#    w = QWidget()
#    w.resize(250, 150)
#    w.move(300, 300)
#    w.setWindowTitle(title)
#    w.show()
#
#    sys.exit(app.exec_())


# #面开始我们采用面向对象的方式进行编码
# # import sys
# # from PyQt5.QtWidgets import QApplication, QWidget,QPushButton#因为需要增加按钮，所以我们引入了QPushButton类。同时我们还需要一个来自QtCore模块的对象。
# # from PyQt5.QtGui import QIcon#从PyQt5.QtGui中引入QIcon这个类，也是为了便于图标的设定。
# # from PyQt5.QtCore import QCoreApplication
# # class Ico(QWidget):
# #
# #    def __init__(self):#这里继承了QWidget这个基类，并自定义了一个名为Ico的新类。同时对这个Ico的新类进行了初始化。
# #        super().__init__()
# #        self.initUI()#程序的GUI界面用initUI()函数创建
# #
# #    def initUI(self):
# #
# #        self.setGeometry(300, 300, 300, 220)#etGeometry（）做了两件事情：它在屏幕上定位窗口并设置它的大小；前两个参数是窗口的x和y位置；第三个是宽度；第四个是窗口的高度。
# #        self.setWindowTitle('学点编程吧出品')
# #        self.setWindowIcon(QIcon('1.ico'))
# #        qbtn = QPushButton('退出', self)#创建一个按钮。该按钮qbtn是QPushButton类的一个实例。构造函数的第一个参数是按钮的标签。第二个参数是父窗口小部件。父窗口小部件是示例窗口小部件，它是通过QWidget继承的。
# #        qbtn.clicked.connect(QCoreApplication.instance().quit)
# #        qbtn.resize(70,30)
# #        qbtn.move(50, 50)
# #        self.show()
# #
# #
# #
# # if __name__ == '__main__':
# #     app = QApplication(sys.argv)
# #     ex = Ico()
# #     sys.exit(app.exec_())

#猜数字
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLineEdit
from PyQt5.QtGui import QIcon
from random import randint


class Example(QWidget):

    def __init__(self):

        super().__init__()
        self.initUI()
        self.num = randint(1, 100)

    def initUI(self):

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('学点编程吧--猜数字')
        self.setWindowIcon(QIcon('xdbcb8.ico'))

        self.bt1 = QPushButton('我猜', self)
        self.bt1.setGeometry(115, 150, 70, 30)
        self.bt1.setToolTip('<b>点击这里猜数字</b>')
        self.bt1.clicked.connect(self.showMessage)

        self.text = QLineEdit('在这里输入数字', self)
        self.text.selectAll()
        self.text.setFocus()
        self.text.setGeometry(80, 50, 150, 30)

        self.show()

    def showMessage(self):

        guessnumber = int(self.text.text())
        print(self.num)

        if guessnumber > self.num:
            QMessageBox.about(self, '看结果', '猜大了!')
            self.text.setFocus()
        elif guessnumber < self.num:
            QMessageBox.about(self, '看结果', '猜小了!')
            self.text.setFocus()
        else:
            QMessageBox.about(self, '看结果', '答对了!进入下一轮!')
            self.num = randint(1, 100)
            self.text.clear()
            self.text.setFocus()

    def closeEvent(self, event):

        reply = QMessageBox.question(self, '确认', '确认退出吗', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())