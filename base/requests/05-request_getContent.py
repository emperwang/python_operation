# -*- encoding:UTF-8 -*-

import requests

# 访问百度
url = "http://www.baidu.com"

response = requests.get(url)
print(response)

# 设置对应的编码,并打印相应的 html
# response.encoding = "utf-8"
# print(response.text)

# 另一种打印结果的方法
print(response.content.decode())
# 参数可以设置解码格式
# print(response.content.decode("UTF-8"))
