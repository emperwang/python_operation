#/usr/bin/python3
# encoding=utf-8


dict = {}
list = []
dict['k'] = "key"
list.append(dict)
dict['k'] = "key1"
list.append(dict)
dict['k'] = "key2"
list.append(dict)
dict['k'] = "key3"
list.append(dict)

print(list)