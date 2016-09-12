#!/usr/bin/nev python3
# -*- coding:utf-8 -*-

"""
@version: v1.0
@author: pengshp
@license: Apache Licence 
@contact: pengshp3@outlook.com
@subject: 坐标轴的位置设置
@site: https://pengshp.github.io/
@software: PyCharm Community Edition
@file: matplt09.py
@time: 16/9/12 下午1:38
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = 2 * x + 1
y2 = x ** 2

plt.figure()
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')
plt.plot(x, y2)

plt.xlim(-1, 2)
plt.ylim(-2, 3)
# plt.xlabel("I am x")
# plt.ylabel("I am y")

new_ticks = np.linspace(-1, 2, 5)
# print(new_ticks)
plt.xticks(new_ticks)  # 设置x轴的刻度值
plt.yticks([-2, -1.8, 0, 1.2],
           [r'$realy\ bad$', r'$bad\ \alpha$', r'$good$', r'$really\ good$'])
# 对应的刻度加上文字,$$美化字体,空格间加上'\'转义空格,'\alpha'是数学中的α

# 修改坐标轴的位置
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')  # 让上面的轴消失
ax.xaxis.set_ticks_position('bottom')  # 用下面的轴代替x轴
ax.yaxis.set_ticks_position('left')  # 用左边的轴代替y轴
ax.spines['bottom'].set_position(('data', 0))  # 把x轴放在y轴0的位置
ax.spines['left'].set_position(('data', 0))  # 把y轴放在x轴0的位置
plt.show()
