# -*- encoding:UTF-8 -*-

import scrapy
from scraydemo1.items import Scraydemo1Item

class Spdemo1Spider(scrapy.Spider):
    # 爬虫名, 启动爬虫时 需要的参数 *必需
    name = 'spdemo1'
    # 爬虫域范围, 允许爬虫在这个域名下进行爬取
    allowed_domains = ['itcast.cn']
    # 起始 url 列表,爬虫执行后第一批请求,将从这个列表里面进行获取
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        print("--" * 100)
        print(type(response))
        node_list = response.xpath("//div[@class='li_txt']")

        # 用来存储所有item字段
        items = []
        for node in node_list:
            # 创建item
            item = Scraydemo1Item()
            # .extract 将xpath对象转换为 Unicode字符串
            name = node.xpath("./h3/text()").extract()
            title = node.xpath("./h4/text()").extract()
            info = node.xpath("./p/text()").extract()
            item['name'] = name[0]
            item['title'] = title[0]
            item['info'] = info[0]
            # items.append(item)

            # 这里直接返回的是items,那么引擎会把此item发送给 pipeline
            yield item
        # 可以把此items 直接输出到文件中
        # scrapy crawl spdemo1 -o data.json
        # return items
        # 如果返回的request请求,则会此返回给调度器
        # return scrapy.Request(url)

