#!/usr/bin/python3
# -*- coding: utf-8 -*-
#计算二次方根
import math
def quadratic(a,b,c):
	B=(b*b-4*a*c)
	if B>=0:
		x1=(-1*b+math.sqrt(B))/(2*a)
		x2=(-1*b-math.sqrt(B))/(2*a)
		return x1,x2
	else:
		print("It has't interger results")
print(quadratic(2, 3, 1))
print(quadratic(1, 3, -4))
