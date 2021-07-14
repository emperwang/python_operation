#!/usr/bin/python
# coding=utf-8

import datetime
import time
import json

def add(a, b=None):
    # 判断参数是否为空
    if b is None:
        print('not pass b')
    # 判断参数的类型
    print(isinstance(a, int))

# 两个时间的比较   先把字符串转换为 时间，再跟时间进行对比
def timeOper():
    timStr = '2020-03-27T13:00:21'
    pattern = '%Y-%m-%dT%H:%M:%S'
    res = time.strftime(pattern, time.localtime())
    print(res)
    tim = time.strptime(timStr, pattern)
    print(time.strftime(pattern, tim))
    print((time.mktime(tim) - time.time()) > 0)



def jsonArr():
    str = '[{"vendor_id":"HW","vendor_name":"华为"},{"vendor_id":"ZX","vendor_name":"中兴"},{"vendor_id":"FH","vendor_name":"烽火"},{"vendor_id":"ER","vendor_name":"爱立信"},{"vendor_id":"NS","vendor_name":"诺西"},{"vendor_id":"AS","vendor_name":"上海贝尔（阿朗）"},{"vendor_id":"DT","vendor_name":"大唐"},{"vendor_id":"PT","vendor_name":"普天"},{"vendor_id":"SS","vendor_name":"江西山水"},{"vendor_id":"OP","vendor_name":"和记奥普泰"},{"vendor_id":"GW","vendor_name":"格林威尔"},{"vendor_id":"NE","vendor_name":"浩瀚深度"},{"vendor_id":"NB","vendor_name":"诺基亚贝尔"},{"vendor_id":"HC","vendor_name":"华三"},{"vendor_id":"CI","vendor_name":"思科"},{"vendor_id":"HY","vendor_name":"杭研"},{"vendor_id":"JP","vendor_name":"Juniper"}]'
    res = json.loads(str)
    for i in res:
        print (i)



if __name__ == '__main__':
    # add(1)
    # timeOper()
    jsonArr()