#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
@version: v1.0
@author: pengshp
@license: Apache Licence 
@contact: pengshp@gmail.com
@site: https://pengshp.github.io
@software: PyCharm Community Edition
@file: 08-PyQt-menu.py
@instructions: 菜单栏
@time: 2017/3/5 下午6:39
"""

import sys
from PyQt5 import QtWidgets, QtGui, QtCore


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize(250, 150)
        self.setWindowTitle("菜单栏示例")

        exit_menu = QtWidgets.QApplication(QtGui.QIcon(r"1.ico"), '退出', self)
        exit_menu.setShortcut("Ctrl+Q")
        exit_menu.setStatusTip("退出程序")
        exit_menu.triggered.connect(QtWidgets.qApp.quit)

        self.statusBar()

        menubar = self.menuBar()  # 创建一个菜单栏
        file = menubar.addMenu("文件")  # addMenu()方法添加一个菜单
        file.addAction(exit_menu)  # 把动作对象（这里是exit_menu）添加到 file 菜单中


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_wind = MainWindow()
    main_wind.show()
    sys.exit(app.exec_())
