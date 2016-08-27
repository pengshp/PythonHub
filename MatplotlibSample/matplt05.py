#!/usr/bin/nev python3
# -*- coding:utf-8 -*-

"""
@version: v1.0
@author: pengshp
@license: Apache Licence 
@contact: pengshp3@outlook.com
@subject: 条形图
@site: https://pengshp.github.io/
@software: PyCharm Community Edition
@file: matplt05.py
@time: 16/8/27 下午2:50
"""

import matplotlib.pyplot as plt
import numpy as np


def bar_show():
    N = 5
    y = [14, 24, 12, 18, 25]
    index = np.arange(N)
    # plt.bar(left=index, height=y, color='r', width=0.5)
    plt.barh(left=0, bottom=index, width=y)  # 横向条形图
    plt.show()


def bar_show2():
    """并列条形图"""
    index = np.arange(4)
    sales_SH = [54, 45, 76, 49]
    sales_BJ = [56, 87, 98, 46]
    bar_width = 0.3
    plt.bar(index, sales_BJ, bar_width, color='r')
    plt.bar(index + bar_width, sales_SH, bar_width, color='b')
    plt.show()


def bar_show3():
    """层叠条形图"""
    index = np.arange(4)
    sales_SH = [54, 45, 76, 49]
    sales_BJ = [56, 87, 98, 46]
    bar_width = 0.3
    plt.bar(index, sales_BJ, bar_width, color='r')
    plt.bar(index, sales_SH, bar_width, color='b', bottom=sales_BJ)
    plt.show()


if __name__ == "__main__":
    bar_show3()
