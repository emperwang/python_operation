# -*- encoding:UTF-8 -*-

import requests
from lxml import etree

url = "https://movie.douban.com/chart"

header = {"User-Agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Mobile Safari/537.36"}

response = requests.get(url, headers=header)
html_str = response.content.decode()

# etree 处理
html_element = etree.HTML(html_str)
print(type(html_element))
# 获取请求
hrefs = html_element.xpath("//div[@class='indent']/div/table//div[@class='pl2']/a/@href ")

print(hrefs)
