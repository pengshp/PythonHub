#!/usr/bin/env python3
#-*-coding: UTF-8-*-
__author__ = 'pengshp'

import urllib
import request
url='http://www.baidu.com/'
req=urllib.Request(url, data=None, headers={}, origin_req_host=None, unverifiable=False)
response=urllib.urlo(req)
the_page=response.read()
print (the_page)
