#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
@version: v1.0
@author: pengshp
@license: Apache Licence 
@contact: pengshp@gmail.com
@site: https://pengshp.github.io
@software: PyCharm Community Edition
@file: 06-sql-functions.py
@instructions: 创建SQL语句使用的自定义聚合函数
@time: 2017/3/5 上午1:52
"""
from sqlite3 import connect

db_name = 'test.db'


class AbsSum:
    def __init__(self):
        self.s = 0

    # 一步一步的执行
    def step(self, v):
        self.s += abs(v)

    # 返回最后的结果
    def finalize(self):
        return self.s


con = connect(db_name)
# 参数：SQL函数，参数个数，类名
# 创建聚合的SQL函数
con.create_aggregate('abssum', 1, AbsSum)

cur = con.cursor()

sql_scrpit = """
drop table if exists testa;
create table if not exists testa(id integer,name text,score integer);
insert into testa (id,name,score) values (3,"Lily",8);
insert into testa (id,name,score) values (4,"Jhon",-7);
"""
cur.executescript(sql_scrpit)

cur.execute('select abssum(score) from testa')
for item in cur:
    print(item)

con.commit()
con.close()
