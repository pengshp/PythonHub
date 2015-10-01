#!/usr/bin/env python3
#-*-coding: UTF-8-*-
__author__ = 'pengshp'

#继承和多态
class Animal(object):
	def run(self):
		print('Animal is running.....')

class Dog(Animal):
	def run(self):
		print('Dog is running.....')

class Cat(Animal):
	def run(self):
		print('Cat is running.....')

dog=Dog()
dog.run()

cat=Cat()
cat.run()

class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')
