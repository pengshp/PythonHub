#!/usr/bin/nev python3
# -*- coding:utf-8 -*-

"""
@version: v1.0
@author: pengshp
@license: Apache Licence 
@contact: pengshp3@outlook.com
@subject: 
@site: https://pengshp.github.io/
@software: PyCharm Community Edition
@file: taobao_girl.py
@time: 2016/11/1 下午10:46
"""
import os
import threading
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver

bsObj = BeautifulSoup(driver.page_source.parge)
imagesUrl = re.findall('\/\/gtd\.alicdn\.com\/sns_logo.*\.jpg', driver.page_source)
grilUrl = bsObj.find_all("a", {"href": re.compile("\/\/.*\.html\?(userId=)\d*")})
girlsHURL = [('http:' + i['href']) for i in grilUrl]


def mkdir(path):
    isExists = os.path.exists(path)
    if not isExists:
        print("   [*] 新建文件夹", path)
        os.makedirs(path)
    else:
        print('   [+]文件夹', path, '已创建')


if __name__ == '__main__':
    if not os.path.exists(outputDir):
        os.makedirs(outputDir)

    main()
