#!/usr/bin/python
#  coding:utf-8

import psycopg2

"""
操作postgresql 数据库
"""


def getdata():
    # 连接数据库
    conn = psycopg2.connect(dbname='postgres', user='fcaps_am', password='fcaps_am', host='192.168.30.10', port=5432)
    # 获得游标
    cur = conn.cursor()
    # 执行查询语句
    cur.execute("select * from am_collection_source")
    # 获取查询语句的所有结果
    rows = cur.fetchall()
    for row in rows:
        print("type rows: {}".format(type(rows)))
        print(row)
    # 执行一条更新语句
        if row[0] == 'ems1':
            cur.execute("update am_collection_source set vendor_id = '%s',cost_class = '%s' where source_id='%s' " % ('HW', 'Z', 'ems1'))
    # 执行查询语句
    cur.execute("select * from am_collection_source")
    # 获取查询语句的所有结果
    rows = cur.fetchall()
    for row in rows:
        print("type rows: {}".format(type(rows)))
        print(row)
    # 关闭资源
    conn.commit()
    cur.close()
    conn.close()


if __name__ == '__main__':
    getdata()
