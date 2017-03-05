#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
@version: v1.0
@author: pengshp
@license: Apache Licence 
@contact: pengshp@gmail.com
@site: https://pengshp.github.io
@software: PyCharm Community Edition
@file: 10-PyQt-Program.py
@instructions: 
@time: 2017/3/5 下午7:00
"""
import sys
from PyQt5 import QtWidgets, QtGui, QtCore


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize(350, 250)
        self.setWindowTitle("综合程序")
        text_edit = QtWidgets.QTextEdit()
        self.setCentraWidget(text_edit)

        # 定义了一个拥有图标、工具提示和快捷键的 action 对象
        exit_action = QtWidgets.QApplication(QtGui.QIcon(r"1.ico"), '退出', self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.setStatusTip("退出程序")
        # 将 action 对象的triggered()信号连接到预定义的quit()槽函数
        exit_action.triggered.connect(QtWidgets.qApp.quit)

        self.statusBar()
        self.menubar = self.menuBar()  # 创建一个菜单栏
        file = self.menubar.addMenu("文件")  # addMenu()方法添加一个菜单
        file.addAction(exit_menu)  # 把动作对象（这里是exit_menu）添加到 file

        self.toolbar = self.addToolBar("退出")  # 创建一个工具栏
        self.toolbar.addAction(self.exit_menu)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_wind = MainWindow()
    main_wind.show()
    sys.exit(app.exec_())
