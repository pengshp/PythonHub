#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
# Function: 建立一个窗口
__author__ = 'pengshp'

import sys
from PyQt5.QtWidgets import QApplication,QWidget

if __name__ == '__main__':
    app=QApplication(sys.argv)

    w=QWidget()
    w.resize(250,150)
    w.move(300,300)
    w.setWindowTitle('First PyQt5!')
    w.show()

    sys.exit(app.exec_())