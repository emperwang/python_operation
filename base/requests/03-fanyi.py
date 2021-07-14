# coding=utf-8
import requests

header = {"User-Agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Mobile Safari/537.36"}

date = {
    "query": "你好",
    "from": "zh",
    "to": "en",
    "token": "0822bfd159d9f21381069a91073262ab",
    "sign": "232427.485594",
}

url = "https://fanyi.baidu.com/basetrans"

res = requests.post(url, data=date, headers=header)
print(res.content.decode())
