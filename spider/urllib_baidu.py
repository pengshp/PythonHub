#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
@version: v1.0
@author: pengshp
@license: MIT Licence 
@contact: pengshp3@outlook.com
@Description: 百度爬虫
@software: PyCharm Community Edition
@file: urllib_baidu.py
@time: 2016/7/10 0010 23:13
"""
import urllib.request

url="http://www.baidu.com"
req=urllib.request.urlopen(url)

html=req.read().decode('UTF-8')

print(html)
