#!/usr/bin/python3
# -*- coding: utf-8 -*-

def power(x,n):
	s=1
	while n>0:
		n=n-1
		s=s*x
	return s

a=power(5, 2)
b=power(5, 4)
print (a)
print (b)
#默认参数
def power1(x,n=2):
	s=1
	while n>0:
		n=n-1
		s=s*x
	return s
c=power1(5)
d=power1(5,4)
print (c)
print (d)

def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

#默认参数必须指向不变对象！list is not
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
