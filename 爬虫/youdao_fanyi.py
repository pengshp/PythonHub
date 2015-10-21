#!/usr/bin/env python3
#-*-coding: UTF-8-*-
__author__ = 'pengshp'

import urllib.request
import urllib.parse
import json

url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
content=input('请输入要翻译的内容：')

#模拟浏览器实现隐藏，避免被服务器识别为爬虫被屏蔽
head={}
head['User-Agent']='Mozilla/5.0 (Windows NT 6.3;WOw64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.99 Safari/537.36'

#提交表单数据
date={}
date['type']='AUTO'
date['i']=content
date['doctype']='json'
date['xmlVersion']='1.8'
date['keyfrom']='fanyi.web'
date['ue']='UTF-8'
date['action']='FY_BY_CLICKBUTTON'
date['typoResult']='true'
date=urllib.parse.urlencode(date).encode('utf-8')

req=urllib.request.Request(url,date,head)
response=urllib.request.urlopen(req)
html=response.read().decode('utf-8')

target=json.loads(html)
print('翻译结果：%s' %(target['translateResult'][0][0]['tgt']) )
