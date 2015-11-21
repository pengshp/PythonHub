#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 默认情况下，dict迭代的是key。如果要迭代value，可以用for value in d.values()，如果要同时迭代key和value，可以用for k, v in d.items()

from collections import Iterable
isinstance('abc', Iterable) # str是否可迭代
isinstance([1,2,3], Iterable) # list是否可迭代
isinstance(123, Iterable) # 整数是否可迭代

#内建的isinstance函数可以判断一个变量是不是字符串：

#列表生成式
L1 = ['Hello','World', 18, 'Apple', None]
l2 = [x.lower() for x in L1 if isinstance(x,str)]
print(l2)
