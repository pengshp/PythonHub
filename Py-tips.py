#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# https://foofish.net/idiomatic_python.html
"""
@version: v1.0
@author: pengshp
@license: Apache Licence 
@contact: pengshp@gmail.com
@site: https://pengshp.github.io
@software: PyCharm Community Edition
@file: Py-tips.py
@instructions: 
@time: 2017/3/10 上午10:09
"""
print("hello world!")
# 变量交换
a, b = 3, 4
print("a=%d,b=%d" % (a, b))
a, b = b, a
print("a=%d,b=%d" % (a, b))

# 循环遍历元素
for i in range(6):
    print(i)

# 带有索引位置的遍历
ccolors = ['red', 'green', 'blue', 'yellow']
for i, color in enumerate(ccolors):
    print(i, '------->', color)

# 字符串连接
names = ['raymond', 'rachel', 'matthew', 'roger',
         'betty', 'melissa', 'judith', 'charlie']
print(', '.join(names))

# 打开关闭文件
with open('data.txt') as f:
    data = f.read()

# 列表推导式
i * 2
for i in range(10):
    print(i)
