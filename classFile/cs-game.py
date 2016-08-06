#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
@version: v1.0
@author: pengshp
@license: MIT Licence 
@contact: pengshp3@outlook.com
@Description: cs游戏python类方法实现
@software: PyCharm Community Edition
@file: cs-game.py
@time: 2016/6/27 0027 17:14
"""


class Role(object):
    ac = None # 类变量，未初始化对象就存在内存中

    """初始化类属性"""

    def __init__(self, name, role, weapon, life_value):
        self.name = name
        self.role = role
        self.weapon = weapon
        self.life_value = life_value #实例化变量，实例化对象时被载入内存

    def buy_weapon(self, weapon):
        self.weapon = weapon
        print("%s is buy [%s]" % (self.name, weapon))
        # print(self.ac)


# 实例化对象
p1 = Role("SanJiang", "Police", "B10", 90)
t1 = Role("Chenchun", "Terrorist", "B11", 100)
# 调用类的方法
p1.buy_weapon("AK47")
t1.buy_weapon("B51")

p1.ac = "China Brand!"
t1.ac = "US Brand!"

Role.ac = "JP Brand!"
Role.weapon = "XD0" #创建了一个类变量
print("P1:", p1.weapon, p1.ac)
print("T1:", t1.weapon, t1.ac)
