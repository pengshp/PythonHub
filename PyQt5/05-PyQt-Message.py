#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
@version: v1.0
@author: pengshp
@license: Apache Licence 
@contact: pengshp@gmail.com
@site: https://pengshp.github.io
@software: PyCharm Community Edition
@file: 05-PyQt-Message.py
@instructions: 消息窗口提示
@time: 2017/3/5 下午5:52
"""
import sys
from PyQt5 import QtWidgets, QtGui, QtCore


class MesageBox(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self, parent=None)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("消息窗口演示程序")

    def closeEvent(self, event):  # 标题栏显示   对话窗口
        reply = QtWidgets.QMessageBox.question(self, '确认退出', '确认退出吗？',
                                               QtWidgets.QMessageBox.Yes,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    qb = MesageBox()
    qb.show()
    sys.exit(app.exec_())
