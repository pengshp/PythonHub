#!/usr/bin/nev python3
# -*- coding:utf-8 -*-

"""
@version: v1.0
@author: pengshp
@license: Apache Licence 
@contact: pengshp3@outlook.com
@subject: 饼状图
@site: https://pengshp.github.io/
@software: PyCharm Community Edition
@file: matplt07.py
@time: 16/8/27 上午2:43
"""

import matplotlib.pyplot as plt

labels = 'A', 'B', 'C', 'D'
fracs = [15, 30, 45, 10]
explode = [0, 0.05, 0, 0]  # 突出显示第二部分的值

plt.axes(aspect=1)  # 使x,y坐标比例为1:1

# autopct格式化输出每部分所占的比值,explode突出显示某部分的值,shadow=True加上阴影
plt.pie(x=fracs, labels=labels, autopct="%.0f%%", explode=explode, shadow=True)
plt.show()
