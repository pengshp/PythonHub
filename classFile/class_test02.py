#!/usr/bin/env python3
#-*-coding: UTF-8-*-
__author__ = 'pengshp'

#数据的封装和私有变量
class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))
#外部代码获取数据
	def get_name(self):
		return self.__name
	def get_score(self):
		return self.__score

#外部代码修改数据
	def set_score(self,score):
		if 0 <= score <= 100:
			self.__score=score
		else:
			raise ValueError('bad score')
