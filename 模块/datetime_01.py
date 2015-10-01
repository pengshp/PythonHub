#!/usr/bin/env python3
#-*-coding: UTF-8-*-
__author__ = 'pengshp'

#datetime是模块，datetime模块还包含一个datetime类，通过from datetime import #datetime导入的才是datetime这个类
from datetime import datetime
now=datetime.now()
print(now)

dt=datetime(2015, 10, 1, 12, 30, 00)
print(dt)
print(dt.timestamp())

t = 1429417200.0
print(datetime.fromtimestamp(t)) # 本地时间
print(datetime.utcfromtimestamp(t)) # UTC时间
