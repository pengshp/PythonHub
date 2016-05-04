#!/usr/bin/python3
# -*- coding: utf-8 -*-

def my_abs(x):
	if not isinstance(x, (int, float)): #参数类型检查
        raise TypeError('bad operand type')
	if x>0:
		return x
	else:
		return -x

a=my_abs(-100)
print(a)

def nop():
	pass
