# coding=utf-8
import requests

# 定义代理
proxy = {"http": "http://183.196.97.125:46006"}
# 定义请求头
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
            "Accept": "* / *",
            "Accept - Encoding": "gzip, deflate, br"}
# 访问的地址
url = "http://www.baidu.com"
# 使用代理进行访问
res = requests.post(url, proxies=proxy, headers=headers)
print(res)