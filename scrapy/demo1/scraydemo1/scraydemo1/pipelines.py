# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import json

class Scraydemo1Pipeline:

    def __init__(self):
        self.f = open("spdemo_pipeline.json", "wb")

    def process_item(self, item, spider):
        # (dict(item) 把item转换为dict
        content = json.dumps(dict(item), ensure_ascii=False)+"\n"
        # 写入文件
        self.f.write(content.encode(encoding="UTF-8"))
        # 此item返回给引擎,告诉引擎此item处理按错
        return item


    def close_spider(self, spider):
        self.f.close()