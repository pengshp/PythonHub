#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
@version: v1.0
@author: pengshp
@license: MIT Licence 
@contact: pengshp3@outlook.com
@Description: 个性化图标
@software: PyCharm Community Edition
@file: pyQt02.py
@time: 2016/5/15 0015 15:33
"""
import sys
from PyQt5.QtWidgets import QWidget,QApplication
from PyQt5.QtGui import QIcon

class Exp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Icon')
        self.setGeometry(300,200,300,200)
        self.setWindowIcon(QIcon('heart.ico'))

        self.show()

if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex=Exp()
    sys.exit(app.exec_())