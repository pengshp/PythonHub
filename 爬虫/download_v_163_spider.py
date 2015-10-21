#!/usr/bin/env python3
#-*-coding: UTF-8-*-
#Time:2015-10-18
#Function:下载网易公开课视频
"""
使用方法：
xxx.py http://v.163.com/special/opencourse/buildingdynamicwebsites.html
"""
__author__ = 'pengshp'

import urllib
from bs4 import BeautifulSoup
import fnmatch
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)

    for link in soup.find_all('a'):
        content = link.get('href')
        if type(content)==type(None):
            pass
        elif fnmatch.fnmatch(content, "*.mp4"):
            print content
        else:
            pass
