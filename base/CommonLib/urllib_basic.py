#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import urllib.request
import urllib.parse


# --------------------------------------------------------------------------------
url = "http://www.baidu.com"
# urlparse  将url解析成各个组件
# ParseResult(scheme='http', netloc='www.baidu.com', path='', params='', query='', fragment='')
parsed = urllib.parse.urlparse(url)
print(parsed)


# --------------------------------------------------------------------------------
# urljoin(baseurl, newurl, allowFrag=None)  将url的根域名和新url拼接成为一个完整的url
new_path = urllib.parse.urljoin(url,'index.html')
print(new_path)  # http://www.baidu.com/index.html

# --------------------------------------------------------------------------------


def use_proxy(proxy_addr, url):
    # 通过当前主机设置的代理,然后才能访问到外网地址
    proxy = urllib.request.ProxyHandler({'http': 'http://%(user)s:%(pass)s@%(host)s:%(port)d' % proxy_addr})
    opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)
    data = urllib.request.urlopen(url).read(10).decode('utf-8')
    return data

# urlopen(url,data,timeout) 打开一个url的方法,返回一个文件对象,然后可以进行类似文件操作
proxy_addr={
    'user': 'itnms@bmccisa.com',
    'pass': 'tre.540',
    'host': '10.4.200.21',
    'port': 18765
}
# 打开百度网页
req = use_proxy(proxy_addr, "http://www.baidu.com")
print(req)

# --------------------------------------------------------------------------------
# urlencode() 将dict中的键值对以连接符&划分
dic = {'name': 'melon', 'age': 18}
data = urllib.parse.urlencode(dic)
print(data)

