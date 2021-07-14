#!/use/bin/python3
# coding=utf-8
import json
# dict
data = {
    'no': 1,
    'name': 'Runoob',
    'url': 'http://www.runoob.com'
}

json_str = json.dumps(data)
print("origin str:", repr(data))
print("json:", json_str)
# json to python dict
data2 = json.loads(json_str)
print("data2['name']:", data2['name'])
print("data2['url']:", data2['url'])