#!/usr/bin/nev python3
# -*- coding:utf-8 -*-

"""
@version: v1.0
@author: pengshp
@license: Apache Licence 
@contact: pengshp3@outlook.com
@subject: 折线图
@site: https://pengshp.github.io/
@software: PyCharm Community Edition
@file: matplt04.py
@time: 16/8/27 下午2:45
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 5)

y = x ** 2

plt.plot(x, y)

plt.show()
