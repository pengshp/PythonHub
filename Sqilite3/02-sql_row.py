#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
@version: v1.0
@author: pengshp
@license: Apache Licence 
@contact: pengshp@gmail.com
@site: https://pengshp.github.io
@software: PyCharm Community Edition
@file: sql_row.py
@instructions: 
@time: 2017/3/5 上午12:38
"""
from sqlite3 import connect, Row

# Row是一个行对象

db_name = 'temp.db'
con = connect(db_name)
con.row_factory = Row  # 设置属性为行对象
cur = con.cursor()


def main():
    cur.execute('select * from start')
    row = cur.fetchone()  # 获取一行数据
    print(type(row))

    print('以列名访问：', row['name'])

    print('以索引号访问：', row[1])

    print('以迭代访问：')
    for item in row:
        print(item)

    print("len= ", len(row))  # 列数
    con.close()


if __name__ == '__main__':
    main()
