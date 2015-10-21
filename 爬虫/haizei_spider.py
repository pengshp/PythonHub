#!/usr/bin/env python3
#-*-coding: UTF-8-*-
#Time:2015-10-19
#Function:监测海贼王的更新
__author__ = 'pengshp'

import urllib.request
import re
import smtplib

def open_url(url):
	req=urllib.request.Request(url)
	req.add_header('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.99 Safari/537.36')
	response=urllib.request.urlopen(url)
	html=response.read().decode('utf-8')
	return html

def get_value(html):
	#html_get=open_url(url)
	value_a=re.findall(r'\b<li class="pure-u-1-2 pure-u-lg-1-4"><a href="(\d+)/"\b',html)
	print(value_a)
	return int(value_a[0])

def send_mail():
	from_addr='xxxxxxxxxx@163.com'        #发送邮件邮箱
	password='xxxxxxxxx'                  #发送邮箱密码
	subject="更新提醒"
	to_addr='xxxxxxxxxxx@qq.com'          #接受邮件邮箱
	msg_string="海贼王有更新!"
	msg_str=string.join((
	"From: %s" %from_addr,
	"To: %s" %to_addr,
	"Subject: %s" %subject,
	msg_string),
	"\r\n")
	server=smtplib.SMTP("smtp.163.com",25)
	srever.login(from_addr,password)
	srever.sendmail(from_addr,to_addr,msg_str)
	srever.quit()

if __name__=='__main__':
	url='http://www.fzdm.com/manhua/002/'
	value1=802
	while True:
		#open_url(url)
		VALUEL=get_value(url)
		if VALUEL>value1:
			send_mail()
			print('发送邮件成功！')
			value1=VALUEL
		else:
			break
