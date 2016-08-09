#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
@version: v1.0
@author: pengshp
@license: MIT Licence 
@contact: pengshp3@outlook.com
@Description: pandas模块的基本用法 http://codingpy.com/article/a-quick-intro-to-pandas/
@software: PyCharm Community Edition
@file: pandas_semple.py
@time: 2016/8/9 0009 13:09
"""

"""
Pandas 基于两种数据类型，series 和 dataframe。
series 是一种一维的数据类型，其中的每个元素都有各自的标签。如果你之前看过这个系列关于 Numpy 的推文，
你可以把它当作一个由带标签的元素组成的 numpy 数组。标签可以是数字或者字符。
dataframe 是一个二维的、表格型的数据结构。Pandas 的 dataframe 可以储存许多不同类型的数据，并且每个轴都有标签。
你可以把它当作一个 series 的字典。
"""
import pandas as pd
#header 关键字告诉 Pandas 哪些是数据的列名。如果没有列名的话就将它设定为 None 。Pandas 非常聪明，所以这个经常可以省略。
df=pd.read_csv('uk_rain_2014.csv',header=0)#导入数据
#df.head(5)#得到前五行
#df.tail(5)#得到前五列

# Changing column labels.
df.columns = ['water_year','rain_octsep', 'outflow_octsep',
              'rain_decfeb', 'outflow_decfeb', 'rain_junaug', 'outflow_junaug']
df.head(5)

sum=len(df)#数据行数
pd.options.display.float_format='{:,.3f}'.format
df.describe()

df['rain_octsep']#通过标签提取一整列

# Creating a series of booleans based on a conditional
df.rain_octsep < 1000 # Or df['rain_octsep] < 1000

# Getting a row via a numerical index
df.iloc[30]

# Setting a new index from an existing column
df = df.set_index(['water_year'])
df.head(5)



#if __name__ == '__main__':
    