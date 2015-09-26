#!/usr/bin/python3
# -*- coding: utf-8 -*-
#打印杨辉三角

def triangle(n):
    L=[1]
    while True:
        yield(L)
        L.append(0)
        L=[L[i]+L[i-1] for i in range(len(L))]
        if len(L)>10:
            break
    return "done"

g=triangle(10)
for i in g:
    print(i)

L = [1]
    yield(L)
    L = [1,1]
    yield(L)
    while True:
        L = [1] + [L[ i ] + L[i + 1] for i in range(len(L) - 1)] + [1]
        yield
