#!/usr/bin/python3
# -*- coding: utf-8 -*-

#在一个list中，删掉偶数，只保留奇数
def is_odd(n):
	return n%2==1
list(filter(is_odd,[1,2,4,5,6,7,9,10,15])

#把一个序列中的空字符串删掉
def not_empty(s):
	return s and s.strip()#删除空白字符
list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])
