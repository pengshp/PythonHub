#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
@version: v1.0
@author: pengshp
@license: Apache Licence 
@contact: pengshp@gmail.com
@site: https://pengshp.github.io
@software: PyCharm Community Edition
@file: 09-PyQt-ToolBar.py
@instructions: 工具栏
@time: 2017/3/5 下午6:51
"""
import sys
from PyQt5 import QtWidgets, QtGui, QtCore


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize(250, 150)
        self.setWindowTitle("工具栏示例")
        # 定义了一个拥有图标、工具提示和快捷键的 action 对象
        self.exit_menu = QtWidgets.QApplication(QtGui.QIcon(r"1.ico"), '退出', self)
        self.exit_menu.setShortcut("Ctrl+Q")
        self.exit_menu.setStatusTip("退出程序")

        # 将 action 对象的triggered()信号连接到预定义的quit()槽函数
        self.exit_menu.triggered.connect(QtWidgets.qApp.quit)

        self.toolbar = self.addToolBar("退出")  # 创建一个工具栏
        self.toolbar.addAction(self.exit_menu)
        self.statusBar()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_wind = MainWindow()
    main_wind.show()
    sys.exit(app.exec_())
