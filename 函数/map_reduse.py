#!/usr/bin/python3
# -*- coding: utf-8 -*-
#首字母大写，其余小写的capitalize()方法
L1=['adam', 'LISA', 'barT']
def normalize(name):
	return str(name).capitalize()
L2=list(map(normalize,L1)
print (L2)

#编写一个prod()函数，可以接受一个list并利用reduce()求积
from functools  import reduce
def multipy(x,y):
	return x*y
def prod(L):
	return reduce(multipy,L)
print ('3*5*7*9=',prod([3,5,7,9]))

#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
from functools  import reduce
#小数点前的使用multipy函数
def multipy(x,y):
    return x*10+y
def str2float(s):
	return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

def str2float(s):
    s0=s.split('.')
    s1=s0[0]
    s2=s0[1]

    #小数点后的位数
    length=len(s2)
    return reduce(multipy, map(char2num,s1))+ reduce(multipy, map(char2num,s2))/(10**length)

print('str2float(\'123.456\')=',str2float('123.456'))
