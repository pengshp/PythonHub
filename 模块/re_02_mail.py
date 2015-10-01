#!/usr/bin/env python3
#-*-coding: UTF-8-*-
__author__ = 'pengshp'

#正则练习题

#P1 所有@gmail.com和@microsoft.com的邮箱被筛选出来

import re
my_str_list=['Kami@163.com','Kami@gmail.com','Kami_new@gmail.com','Kami@microsoft.com','qqqq','jack@gmail.com','Tom@gmail.com','Kami@163.com']
my_re_gmail = re.compile(r'[0-9a-zA-Z]+@(gmail|microsoft).com')  #匹配gmail的正则
gmail_list=[x for x in my_str_list if my_re_gmail.match(x)]
print(gmail_list)


#P2 提取带Kami的Email地址
my_re_name_email = re.compile(r'[0-9a-zA-Z]*Kami[0-9a-zA-Z]*@(gmail|microsoft|163).com')
name__email_list=[x for x in my_str_list if my_re_name_email.match(x)]
print(name__email_list)
