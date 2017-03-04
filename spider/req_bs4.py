#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
@version: v1.0
@author: pengshp
@license: Apache Licence 
@contact: pengshp@gmail.com
@site: https://pengshp.github.io
@software: PyCharm Community Edition
@file: req_bs4.py
@time: 2017/3/4 下午5:42
"""
import requests, json, re
from bs4 import BeautifulSoup
from datetime import datetime

url = 'http://news.sina.com.cn/o/2017-03-04/doc-ifyazwha3806649.shtml'
req = requests.get(url)
req.encoding = 'utf-8'
soup = BeautifulSoup(req.text, 'html.parser')
# 获取文章标题
title = soup.select('#artibodyTitle')[0].text
print(title)

# 获取文章时间
timesource = soup.select('.time-source')[0].contents[0].strip()
dt = datetime.strptime(
    timesource,
    '%Y年%m月%d日%H:%M'
)
time = dt.strftime('%Y-%m-%d')
print(time)

# 获取文章来源
source = soup.select('.time-source span a')[0].text
print(source)

# 获取文章内容
article = []
for p in soup.select('#artibody p')[:-1]:
    article.append(p.text.strip())
'\n'.join(article)
print(article)

# 获取编辑者
editor = soup.select('.article-editor')[0].text
print(editor)

# 获取评论数
com_url = 'http://comment5.news.sina.com.cn/page/info?version=1&format=js&channel=sh&newsid=comos-fyazwha3806649&group=&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=20'
comments = requests.get(com_url)
jd = json.loads(comments.text.strip('var data='))  # json转为Python字典
counts = jd['result']['count']['total']
print("文章评论数：" + str(counts))


def getCommentCounts(newurl):
    m = re.search('doc-i(.*).shtml', newurl)
    newsid = m.group(1)
    comments = requests.get(commentURL.format(newsid))
    jd = json.loads(comments.text.strip('var data='))
    return jd['result']['count']['total']
