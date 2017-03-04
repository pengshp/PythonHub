#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

url = 'http://news.sina.com.cn/china/'
# url = 'http://www.163.com'
res = requests.get(url)
res.encoding = 'utf-8'
html = res.text
soup = BeautifulSoup(html, 'html.parser')
for news in soup.select('.news-item'):
    if len(news.select('h2')) > 0:
        title = news.select('h2')[0].text
        time = news.select('.time')[0].text
        link = news.select('a')[0]['href']
        print(title, time, link)

print("hello world!")
