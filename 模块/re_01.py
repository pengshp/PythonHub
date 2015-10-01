#!/usr/bin/env python3
#-*-coding: UTF-8-*-
__author__ = 'pengshp'

import re
test='010-123456'
if re.match(r'^\d{3}\-\d{3,8}$', test, flags=0):
	print ('ok')
else:
	print('failed')

#切分字符串
str1='a b  c,d   e;f'
re.split(r'[\s\,\;]+', str1, maxsplit=0, flags=0)

m=re.match(r'^(\d{3})-(\d{3,8})$', test, flags=0)
print(m.group(0)#原始字符串
print(m.group(1)#第一个字符串
print(m.group(2)#第二个字符串

#贪婪匹配
re.match(r'^(\d+)(0*)$', '102300').groups()
#非贪婪匹配
re.match(r'^(\d+?)(0*)$', '102300').groups()
