#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
@version: v1.0
@author: pengshp
@license: Apache Licence 
@contact: pengshp@gmail.com
@site: https://pengshp.github.io
@software: PyCharm Community Edition
@file: 04-PyQt-quit.py
@instructions: 用按钮关闭程序
@time: 2017/3/5 下午5:32
"""
import sys
from PyQt5 import QtWidgets, QtCore, QtGui


class QuitButtoon(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("我的关闭程序")
        # 创建一个按钮放在QWidget部件上
        btn = QtWidgets.QPushButton("关闭", self)
        btn.setGeometry(10, 10, 60, 35)
        # 将信号[quit]和槽函数[quit()函数]连接起来
        btn.clicked.connect(QtWidgets.qApp.quit)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    quit_btn = QuitButtoon()
    quit_btn.show()
    sys.exit(app.exec_())
