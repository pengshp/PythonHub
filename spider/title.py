#!/usr/bin/env python3
#Time：2015-11-6
#爬取相应网页的标题

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html=urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsobj=BeautifulSoup(html.read())
        title=bsobj.boby.h1
    except AttributeError as e:
        return None
    return title

title=getTitle("http://www.baidu.com/")
if title == None:
    print("Title could not found")
else:
    print(title)

