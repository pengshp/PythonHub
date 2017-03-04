#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
@version: v1.0
@author: pengshp
@license: Apache Licence 
@contact: pengshp@gmail.com
@site: https://pengshp.github.io
@software: PyCharm Community Edition
@file: 03-sql-many.py
@instructions: 使用executemany批量操作数据
@time: 2017/3/5 上午1:00
"""
from sqlite3 import connect, Row

db_name = 'temp.db'
con = connect(db_name)
con.row_factory = Row  # 设置属性为行对象
cur = con.cursor()


def main():
    rows = [(14, 'Lily', 12, 'BeiJing'), (6, 'John', 13, "ChongQing")]
    # 批量的插入数据
    cur.executemany('insert into start (id,name,age,address) values (?,?,?,?)', rows)
    cur.execute('select * from start')
    # 遍历每一行
    for row in cur:
        # 遍历每一行中的每一列
        for r in row:
            print(r)

    con.commit()
    con.close()


if __name__ == '__main__':
    main()
