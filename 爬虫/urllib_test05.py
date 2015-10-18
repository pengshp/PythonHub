#!/usr/bin/env python3
#-*-coding: UTF-8-*-
__author__ = 'pengshp'

import urllib.request

response=urllib.request.urlopen('http://placekitten.com/g/500/600')
cat_img=response.read()
with open('cat.jpg','wb') as f:
	f.write(cat_img)
