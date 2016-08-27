#!/usr/bin/nev python3
# -*- coding:utf-8 -*-

"""
@version: v1.0
@author: pengshp
@license: Apache Licence 
@contact: pengshp3@outlook.com
@subject: 散点图
@site: https://pengshp.github.io/
@software: PyCharm Community Edition
@file: matplt03.py
@time: 16/8/27 下午2:29
"""

import matplotlib.pyplot as plt
import numpy as np

N = 1000

x = np.random.randn(N)
y = np.random.randn(N) * 0.5

# c为点面积大小,c为颜色,marker为点的样式,alpha为透明度0-1
plt.scatter(x, y, s=50, c='r', marker='<', alpha=0.5)
plt.show()
