# coding=utf-8
import requests

headers = {"User-Agent":""}
p = {"wd":"传智播客"}
url_temp = "https://www.baidu.com/s?"

response =requests.get(url_temp, headers=headers, params=p)

print(response.status_code)
print(response.request.url)