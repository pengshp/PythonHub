#!/usr/bin/env python3
#-*-coding: UTF-8-*-
__author__ = 'pengshp'

import re
import urllib.request
import urllib
from collections import deque

queus=deque()
visited=set()
url='http://news.dbanotes.net'
queus.append(url)
cnt=0

while queus:
	url=queus.popleft()#d队首元素出队
	visited |={url}#标记为已访问
	print('已经爬取：'+str(cnt)+'    正在爬取<----  '+url)
	cnt+=1
	urlop=urllib.request.urlopen(url)
	if 'html' not in urlop.getheader('Content-Type'):
		continue

#为避免程序异常终止，使用try...catch处理异常
try:
	date=urlop.read().decode('UTF-8')
except:
	continue

# 正则表达式提取页面中所有队列, 并判断是否已经访问过, 然后加入待爬队列
linkre=re.compile('href="(.+?)"', flags=0)
for x in linkre.findall(date):
	if 'http' in x and x not in visited:
		queus.append(x)
		print ('加入队列----->   '+x)
