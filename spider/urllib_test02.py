#!/usr/bin/env python3
#-*-coding: UTF-8-*-
__author__ = 'pengshp'

import urllib.request
url="http://www.baidu.com"
date=urllib.request.urlopen(url).read()
date=date.decode('UTF-8')
print(date)
