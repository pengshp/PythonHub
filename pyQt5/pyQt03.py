#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
@version: v1.0
@author: pengshp
@license: MIT Licence 
@contact: pengshp3@outlook.com
@Description: 给按钮增加一个提示信息
@software: PyCharm Community Edition
@file: pyQt03.py
@time: 2016/5/15 0015 15:45
"""
import sys
from PyQt5.QtWidgets import QWidget,QToolTip,QPushButton,QApplication
from PyQt5.QtGui import QFont

class exp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif',10))
        self.setToolTip('This is a <b>widget</b>')
        btn=QPushButton('push',self)
        btn.setToolTip('press and push')
        btn.resize(btn.sizeHint())
        btn.move(40,50)
        self.setGeometry(200,300,400,500)
        self.setWindowTitle('setToolTip')
        self.show()

if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex=exp()
    sys.exit(app.exec_())