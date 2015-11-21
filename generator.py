#!/usr/bin/python3
# -*- coding: utf-8 -*-

g = (x * x for x in range(10))
for n in g:
	print (n)

#斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：
def fib(max):
	n,a,b=0,0,1
	while n<max:
		print (b)
		a,b=b,a+b
		n=n+1
	return 'done'
print (fib(6))

def fib1(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
print (fib1(8))
