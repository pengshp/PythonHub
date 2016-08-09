#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
@version: v1.0
@author: pengshp
@license: MIT Licence 
@contact: pengshp3@outlook.com
@Description: 科学计算库Numpy的用法
@software: PyCharm Community Edition
@file: numpy_Tutorial.py
@time: 2016/8/7 0007 9:39
"""
import numpy as np


def basic():
    a = np.array([1, 2, 3])
    print(type(a))
    print(a.shape)
    print(a[0], a[1])
    a[0] = 5
    print(a)

def basic2():
    a=np.zeros((2,2))
    print(a)

    b=np.ones((1,2))
    print(b)

    c=np.full((2,2),7)
    print(c)

    d=np.eye(2) #单位矩阵
    print(d)

    e=np.random.random((2,2))
    print(e)


if __name__ == '__main__':
    basic2()
