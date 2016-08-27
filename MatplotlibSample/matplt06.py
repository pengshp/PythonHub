#!/usr/bin/nev python3
# -*- coding:utf-8 -*-

"""
@version: v1.0
@author: pengshp
@license: Apache Licence 
@contact: pengshp3@outlook.com
@subject: 直方图
@site: https://pengshp.github.io/
@software: PyCharm Community Edition
@file: matplt06.py
@time: 16/8/27 上午2:22
"""
import matplotlib.pyplot as plt
import numpy as np


def hist_show():
    num = 100  # 均值
    sigmx = 20  # 标准差
    x = num + sigmx * np.random.randn(2000)

    plt.hist(x, bins=50, color='red', normed=True)  # 10个直方红色,标准化
    plt.show()


def hist2d_show():
    """双变量直方图"""
    x = np.random.randn(1000) + 2
    y = np.random.randn(1000) + 3
    plt.hist2d(x, y, bins=40)
    plt.show()

if __name__ == '__main__':
    hist2d_show()
