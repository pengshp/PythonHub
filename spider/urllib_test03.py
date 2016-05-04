#!/usr/bin/env python3
#-*-coding: UTF-8-*-
__author__ = 'pengshp'

#抓取百度上面搜索关键词为Jecvay Notes的网页
import urllib
import urllib.request
date={}
date['word']='Jecvay Notes'

url_values=urllib.parse.urlencode(date)
url="http://www.baidu.com/s?"
full_url=url+url_values

date=urllib.request.urlopen(full_url).read()
date=date.decode('UTF-8')
print (date)
