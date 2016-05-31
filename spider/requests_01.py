#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
@version: v1.0
@author: pengshp
@license: MIT Licence 
@contact: pengshp3@outlook.com
@Description: 
@software: PyCharm Community Edition
@file: requests_01.py
@time: 2016/5/17 0017 23:04
"""
import requests
import re

url="http://baidu.com/"
html=requests.get(url)
print(html.encoding)
print(html.cookies)
print(html.text)

if __name__ == '__main__':
    pass