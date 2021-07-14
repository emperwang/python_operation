#/use/bin/env python
# coding:utf-8

import pymysql

"""
操作mysql数据库
"""


def getdata():
    conn = pymysql.connect(host='localhost', user='root', passwd='admin', port=3306, charset='utf8')
    cur = conn.cursor()
    conn.select_db('ssm')
    count = cur.execute('select * from user')
    print('there are {} rows record.'.format(count))
    # 获取所有
    result = cur.fetchall()
    # 获取一个结果
    #result = cur.fetchone()
    # 获取指定数量的结果
    # result5 = cur.fetchmany(2)
    for i in result:
        print(i)

    print('*'*50)
    # 插入数据
    cur.execute("insert into user(name, age, address) values('zhaoqi1', 20, 'beijing2'),('zhao2', 30, 'beijing4')")
    count = cur.execute('select * from user')
    print('there are {} rows record.'.format(count))
    # 获取所有
    result = cur.fetchall()
    for i in result:
        print(i)

    conn.commit()
    cur.close()
    conn.close()


if __name__ == '__main__':
    getdata()