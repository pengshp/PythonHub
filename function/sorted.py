#!/usr/bin/python3
# -*- coding: utf-8 -*-
from operator import itemgetter
#对于两个元素x和y，如果认为x < y，则返回-1，如果认为x == y，则返回0，如果认为x > y，则返回1
sorted([36, 5, -12, 9, -21])
#[-21, -12, 5, 9, 36]
sorted([36, 5, -12, 9, -21], key=abs)
#[5, 9, -12, -21, 36]

L = ['bob', 'about', 'Zoo', 'Credit']

print(sorted(L))
print(sorted(L, key=str.lower))

students = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

print(sorted(students, key=itemgetter(0)))
print(sorted(students, key=lambda t: t[1]))
print(sorted(students, key=itemgetter(1), reverse=True))
