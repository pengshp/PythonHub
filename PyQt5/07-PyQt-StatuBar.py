#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
@version: v1.0
@author: pengshp
@license: Apache Licence 
@contact: pengshp@gmail.com
@site: https://pengshp.github.io
@software: PyCharm Community Edition
@file: 07-PyQt-StatuBar.py
@instructions: 状态栏
@time: 2017/3/5 下午6:30
"""
import sys
from PyQt5 import QtWidgets, QtGui, QtCore


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize(250, 150)
        self.setWindowTitle("状态栏示例")
        self.statusBar().showMessage("就绪")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_wind = MainWindow()
    main_wind.show()
    sys.exit(app.exec_())
