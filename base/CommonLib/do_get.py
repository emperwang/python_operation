#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request
import urllib.parse
import json

proxy_addr={
    'user': 'itnms@bmccisa.com',
    'pass': 'tre.540',
    'host': '10.4.200.21',
    'port': 18765
}
#代理认证
proxy = urllib.request.ProxyHandler({'http': 'http://%(user)s:%(pass)s@%(host)s:%(port)d' % proxy_addr})
opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
urllib.request.install_opener(opener)


# 传递的参数
dic = {'name': 'melon', 'age': 18}
# 参数转换
data = urllib.parse.urlencode(dic)
# get访问
#req = urllib.request.urlopen('http://10.4.2.52:1234/hello/pyget.do?%s' % data)
#content = req.read()
#print(content)

v = "[{'url':'period':'0','type':'1','mapinfo':[{'mapid':'3','mapprovider':'0'}],'ueinfomap':'7'},"
"{'url':'101.201.79.186/locate','period':'0','type':'1','mapinfo':[{'mapid':'3','mapprovider':'0'},{'mapid':'3','mapprovider':'0'}],'ueinfomap':'7'}] ";

json1 = {
    'url': '101.201.79.1888/locate',
    'period': '0',
    'type': 1,
    'mapinfo': [{
        'mapid': 3,
        'mapprovider': 0
    }]
}

json2 = [{
    'url': '101.201.79.1888/locate',
    'period': '0',
    'type': 1,
    'mapinfo': [{
        'mapid': 3,
        'mapprovider': 0
    }],
    'ueinfomap': 7
},{
    'url': '101.201.79.1888/locatation',
    'period': '188',
    'type': 100,
    'mapinfo': [{
        'mapid': 3,
        'mapprovider': 0
    }],
    'ueinfomap': 7
}]

print(json2)
# post访问
headers={
    'Content-Type': 'application/json'
}
req = urllib.request.Request('http://10.4.2.52:20000/receive.do', headers=headers , data=json.dumps(json1).encode('utf-8'))
# req = urllib.request.Request('http://10.4.2.52:20000/locate.do', headers=headers , data=json.dumps(json2).encode('utf-8'))
opener = urllib.request.urlopen(req)
content2=opener.read()
print(content2)