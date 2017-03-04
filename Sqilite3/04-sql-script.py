#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
@version: v1.0
@author: pengshp
@license: Apache Licence 
@contact: pengshp@gmail.com
@site: https://pengshp.github.io
@software: PyCharm Community Edition
@file: 04-sql-script.py
@instructions: 使用executescript sql脚本执行方式
@time: 2017/3/5 上午1:17
"""
from sqlite3 import connect

db_name = 'tempb.db'
con = connect(db_name)
cur = con.cursor()

# sqlite脚本，语句之间使用分号分隔
sql_str = """
    create table test (id integer,name text);
    insert into test (id,name) values (1,'Lily');
    insert into test (id,name) values (2,'Bily');
"""


def main():
    cur.executescript(sql_str)  # 一次性执行所有的sql语句
    cur.execute('select * from test')
    for item in cur:
        print(item)
    con.commit()  # 每当数据有变动时要修改commit
    con.close()


if __name__ == '__main__':
    main()
