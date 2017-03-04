#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
@version: v1.0
@author: pengshp
@license: Apache Licence 
@contact: pengshp@gmail.com
@site: https://pengshp.github.io
@software: PyCharm Community Edition
@file: 07-sql-binary-file.py
@instructions: 二进制文件操作
@time: 2017/3/5 上午2:06
"""
from sqlite3 import connect

db_name = 'test.db'

con = connect(db_name)
cur = con.cursor()
'''
数据类型转换
Python       SQL
None         NULL
int          integer
str          text
bytes        blob  [二进制位]
'''
sql_scrpit = """
drop table if exists testa;
create table if not exists testa(id integer,data blob);
"""
cur.executescript(sql_scrpit)

f = open('test.jpg', 'rb')

cur.execute('insert into testa (id,data) values (3,?)', (f.read(),))

cur.execute('select * from testa where id=3')
record = cur.fetchone()
f2 = open('tt.jpg', "wb+")
f2.write(record[1])
f.close()
f2.close()
con.commit()
con.close()
