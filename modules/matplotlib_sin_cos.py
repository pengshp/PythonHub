#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
@version: v1.0
@author: pengshp
@license: MIT Licence 
@contact: pengshp3@outlook.com
@Description: Matplotlib库画sin和cos函数
@software: PyCharm Community Edition
@file: matplotlib_sin_cos.py
@time: 2016/8/9 0009 14:37
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-np.pi, np.pi, 256, endpoint='True')  # 从 −π 到 +π 等间隔的 256 个值
c, s = np.cos(x), np.sin(x)

plt.figure(figsize=(8, 6), dpi=80)
plt.subplot(1, 1, 1)
# 绘制余弦曲线，使用蓝色的、连续的、宽度为 1 （像素）的线条
plt.plot(x, c, color="blue", linewidth=1.0, linestyle="-", label="cosine")

# 绘制正弦曲线，使用绿色的、连续的、宽度为 1 （像素）的线条
plt.plot(x, s, color="green", linewidth=1.0, linestyle="-", label='sine')

# 设置横轴的上下限
plt.xlim(-4.0, 4.0)

# 设置纵轴的上下限
plt.ylim(-1.0, 1.0)

# 设置横轴记号
plt.xticks(np.linspace(-4, 4, 9, endpoint="True"))

# 设置纵轴记号
plt.xticks(np.linspace(-4, 4, 9, endpoint="True"))

# 以分辨率72来保存照片
plt.savefig("exercice_2.png", dpi=72)

# gca()方法返回当前轴
ax = plt.gca()

# 将其中上和右坐标轴设置为无色
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# 其中下和左坐标轴移动到(0, 0)
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

# 在左上角添加图例
plt.legend(loc="upper left")

# 添加注释
t = 2 * np.pi / 3
plt.plot([t, t], [0, np.cos(t)], color='blue', linewidth=2.5, linestyle="--")
plt.scatter([t, ], [np.cos(t), ], 50, color='blue')

plt.annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
             xy=(t, np.sin(t)), xycoords='data',
             xytext=(+10, +30), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

plt.plot([t, t], [0, np.sin(t)], color='red', linewidth=2.5, linestyle="--")
plt.scatter([t, ], [np.sin(t), ], 50, color='red')

plt.annotate(r'$\cos(\frac{2\pi}{3})=-\frac{1}{2}$',
             xy=(t, np.cos(t)), xycoords='data',
             xytext=(-90, -50), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(16)
    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.65))

plt.show()

# if __name__ == '__main__':
