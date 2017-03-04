#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
@version: v1.0
@author: pengshp
@license: Apache Licence 
@contact: pengshp@gmail.com
@site: https://pengshp.github.io
@software: PyCharm Community Edition
@file: 05-sql-function.py
@instructions: 创建SQL语句使用的自定义基本函数
@time: 2017/3/5 上午1:37
"""
from sqlite3 import connect, Row
import binascii

db_name = 'test.db'


# 对数据进行加密，加上32位的校验码
def encrypt(mydata):
    crc = str(binascii.crc32(mydata.encode()))
    while len(crc) < 10:
        crc = '0' + crc
    return mydata + crc


# 核对校验码
def check(mydata):
    """查询成功返回名字，查询失败返回None"""
    if len(mydata) < 11:
        return None
    crc_res = str(binascii.crc32(mydata[:-10].encode()))
    while len(crc_res) < 10:
        crc_res = '0' + crc_res
    if crc_res == mydata[-10:]:
        return mydata[:-10]


con = connect(db_name)
# 参数：创建函数的名字，参数的个数，Python中的函数
# 注册check函数
con.create_function('checkk', 1, check)

cur = con.cursor()

sql_scrpit = """
drop table if exists testa;
create table if not exists testa(id integer,name text);
insert into testa (id,name) values (3,"%s");
insert into testa (id,name) values (4,"%s");
"""
names = ['Lily', 'Green']
names = tuple(encrypt(i) for i in names)
sql_scrpit = sql_scrpit % names
print(sql_scrpit)
cur.executescript(sql_scrpit)
# 查询中使用自定义的函数
cur.execute('select id,checkk(name) from testa')
for item in cur:
    print(item)

cur.execute('update testa set name=? where id=?', ('dfddkkjd1122334455', 4))
cur.execute('select id,checkk(name) from testa')
for item in cur:
    print(item)

con.commit()
con.close()
