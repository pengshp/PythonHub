#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
@version: v1.0
@author: pengshp
@license: MIT Licence 
@contact: pengshp3@outlook.com
@Description: 
@software: PyCharm Community Edition
@file: matploylib_02.py
@time: 2016/8/7 0007 21:48
"""
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


def basic():
    n = 256
    x = np.linspace(-np.pi, np.pi, n, endpoint='True')
    y = np.sin(2 * x)
    plt.plot(x, y + 1, color='blue', alpha=1.00)  # 生成填充图形
    plt.plot(x, y - 1, color="blue", alpha=1.00)
    plt.show()


def basic_3D():
    """3D图形的绘制"""
    fig = plt.figure()
    ax = Axes3D(fig)
    x = np.arange(-4, 4, 0.25)
    y = np.arange(-4, 4, 0.25)
    x, y = np.meshgrid(x, y)
    r = np.sqrt(x ** 2 + y ** 2)
    z = np.sin(r)
    ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap="hot")
    plt.show()


if __name__ == '__main__':
    basic_3D()
