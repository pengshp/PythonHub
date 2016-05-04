#!/usr/bin/python3
# -*- coding: utf-8 -*-

def fact(n):
	if n==1:
		return 1
	return n*fact(n-1)
print (fact(5))
print (fact(20))

def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
