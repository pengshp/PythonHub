#!/usr/bin/env python3
# -*-coding: UTF-8-*-
__author__ = 'pengshp'

std1={'name': 'Michael', 'score':98}
std2={'name': 'Bob', 'score':88}

def print_score(std):
	print('%s:%s'%(std['name'],std['score']))
print_score(std1)

#使用类来实现
class Student(object):
	def __init__(self,name,score):
		self.name=name
		self.score=score

	def print_score1(self):
		print ('%s: %s' %(self.name,self.score))

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score1()
lisa.print_score1()
