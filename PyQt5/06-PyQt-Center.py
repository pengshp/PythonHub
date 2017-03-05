#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
@version: v1.0
@author: pengshp
@license: Apache Licence 
@contact: pengshp@gmail.com
@site: https://pengshp.github.io
@software: PyCharm Community Edition
@file: 06-PyQt-Center.py
@instructions: 把窗口移到屏幕中间
@time: 2017/3/5 下午6:15
"""
import sys
from PyQt5 import QtWidgets, QtGui, QtCore


class Center(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self, parent=None)
        self.resize(250, 150)
        self.setWindowTitle("窗口置中程序")
        self.center()

    def center(self):
        screen = QtWidgets.QDesktopWidget().screenGeometry()  # 计算显示器的分辨率
        size = self.geometry()  # 获取QWidget窗口的大小
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)
        # 将窗口移到屏幕中间


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    center = Center()
    center.show()
    sys.exit(app.exec_())
