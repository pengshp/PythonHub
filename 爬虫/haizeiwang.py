#!/usr/bin/env python3
#-*-coding: UTF-8-*-
__author__ = 'pengshp'

import urllib2
import stmplib
import re

#设置代理
enable_proxy=True
proxy_handler=urllib2.ProxyHandler({"http":'http://some-proxy.com:8080'})
null_proxy_header=urllib2.ProxyHandler({})
if enable_proxy:
	opener=urllib2.build_opener(proxy_handler)
else:
	opener=urllib2.build_opener(null_proxy_header)
urllib2.install_opener(opener)

#发送邮件
def sendmail():
	stmp=stmplib.STMP('163.stmp.com')

#爬取网页
url="http://www.fzdm.com/manhua/002/"
def fetch(url):
	http_header={'User-Agent':'Chrome'}
	http_request=urllib2.Request(url,None,http_header)

	http_response=urllib2.urlopen(http_request,timeout=20)
	code=http_response.code()
	if code==200:
		print (http_response.info())
		print (http_response.read())
	else:
		print ("网络异常，无法访问.....")

#正则表达式匹配
def rre():
	pattern=re.compile(r.'hello')
	result1=re.match(pattern,'hello')

if result1:
	print (result1.group())
else:
	print ('匹配失败......')


if __name__ == '__main__':
	fetch(url)
