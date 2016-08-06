#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
@version: v1.0
@author: pengshp
@license: MIT Licence 
@contact: pengshp3@outlook.com
@Description: 
@software: PyCharm Community Edition
@file: matplot.py
@time: 2016/7/13 0013 17:26
"""

import numpy as np
import matplotlib.pyplot as plt

'''
x=np.linspace(0,2*np.pi,50) # 生成一个包含50个元素的数组
plt.plot(x,np.sin(x),'r-o',x,np.sin(2*x),'g--') # 红色圆点标记和绿色虚线标记
plt.show()
'''

'''
# 使用子图
x=np.linspace(0,2*np.pi,50)
plt.subplot(2,1,1) # (行，列，活跃区)
plt.plot(x,np.sin(x),'r')

plt.subplot(2,1,2)
plt.plot(x,np.cos(x),'g')
plt.show()
'''

'''
# 简单的散点图
x=np.linspace(0,2*np.pi,50)
y=np.sin(x)
plt.scatter(x,y) # 散点图
plt.show()
'''

'''
# 彩色映射散点图
x=np.random.rand(1000)
y=np.random.rand(1000)
siez= np.random.rand(1000)*50

colour=np.random.rand(1000)
plt.scatter(x,y,siez,colour) #所绘点的大小和颜色
plt.colorbar() # 添加一个颜色栏
plt.show()
'''

'''
# 直方图
x=np.random.rand(1000)
plt.hist(x,50) # 50代表数据容器的个数，数据容器越多，图形上的数据条越多
plt.show()
'''

# 标题，标签和图例
x = np.linspace(0, 2 * np.pi, 50)
plt.plot(x, np.sin(x), 'r-x', label='Sin(x)')
plt.plot(x, np.cos(x), 'g-^', label='Cos(x)')
plt.legend()  # 展示图例
plt.xlabel('Rads')  # 给x轴添加标签
plt.ylabel('Amplitude')
plt.title('Sin and Cos Waves')  # 添加图形标题
plt.show()
