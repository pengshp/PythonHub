#!/usr/bin/nev python3
# -*- utf-8 -*-

"""
@version: v1.0
@author: pengshp
@license: Apache Licence 
@contact: pengshp3@outlook.com
@subject: 
@site: https://pengshp.github.io/
@software: PyCharm Community Edition
@file: matplt01.py
@time: 16/8/26 下午8:12
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 10)
y = 2 * x + 0.5

plt.plot(x, y)
plt.show()
