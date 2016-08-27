#!/usr/bin/nev python3
# -*- coding:utf-8 -*-

"""
@version: v1.0
@author: pengshp
@license: Apache Licence 
@contact: pengshp3@outlook.com
@subject: 箱形图
@site: https://pengshp.github.io/
@software: PyCharm Community Edition
@file: matplt08.py
@time: 16/8/27 上午3:07
"""

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(100)

# 4x1000的数组
datas = np.random.normal(size=(1000, 4), loc=0, scale=1)

labels = ['A', 'B', 'C', 'D']

plt.boxplot(datas, sym='o')

plt.show()
