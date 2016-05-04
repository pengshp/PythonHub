#!/usr/bin/env python3
#-*-coding: UTF-8-*-
#Time:2015-10-18
#Function:下载煎蛋网的妹子图片
__author__ = 'pengshp'

import urllib.request
import os
import time
def url_open(url):
	req=urllib.request.Request(url)
	req.add_header('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.99 Safari/537.36')
	response=urllib.request.urlopen(url)
	time.sleep(0.5)
	html=response.read()
	return html

def get_page(url):
	html=url_open(url).decode('utf-8')
	a=html.find('current-comment-page')+23
	b=html.find(']',a)
	return html[a:b]

def find_imgs(url):
	html=url_open(url).decode('utf-8')
	img_addrs=[]
	a=html.find('img src=')
	while a != -1:
		b=html.find('.jpg',a,a+255)
		if b != -1:
			img_addrs.append(html[a+9:b+4])
		else:
			b=a+9
		a=html.find('img src=',b)
	return img_addrs

def save_imgs(folder,img_adders):
	for each in img_adders:
		filename=each.split('/')[-1]
		with open(filename, mode=wb, buffering=None) as f:
			img=url_open(each)
			f.write(img)

def download_mm(floder='OOXX',pages=10):
	os.mkdir(floder)
	os.chdir(floder)
	url="https://jandan.net/ooxx/"
	page_mun=int(get_page(url))

	for i in range(pages):
		page_mun-=i
		page_url=url+'page-'+str(page_mun)+'#comments'
		img_addrs=find_imgs(page_url)
		save_imgs=(floder,img_addrs)

if __name__=='__main__':
	download_mm()
