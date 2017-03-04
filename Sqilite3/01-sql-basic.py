#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
@version: v1.0
@author: pengshp
@license: Apache Licence 
@contact: pengshp@gmail.com
@site: https://pengshp.github.io
@software: PyCharm Community Edition
@file: 01-sql-basic.py
@time: 2017/3/4 下午10:10
"""
from sqlite3 import connect

db_name = 'temp.db'
con = connect(db_name)  # 建立数据库连接对象
cur = con.cursor()  # 建立游标对象

cur.execute('create table start (id integer,name text,age integer,address text)')
rows = [(1, "王俊凯", 16, "重庆"), (2, "王源", 15, "重庆"), (3, "易烊千玺", 15, "怀化")]


# 插入数据
def sql_insert():
    for item in rows:
        cur.execute("insert into start (id,name,age,address) values (?,?,?,?)", item)


# 查询数据
def sql_select():
    cur.execute('select * from start')
    print("插入数据....")
    for row in cur:
        print(row)


# 修改数据
def sql_update():
    cur.execute('update start set age=? where id=?', (16, 3))


def main():
    sql_insert()
    sql_select()
    sql_update()
    sql_select()
    con.commit()  # 提交事务
    con.close()  # 操作完成后关闭连接对象


if __name__ == '__main__':
    main()
