# -*- encoding:UTF-8 -*-

import scrapy


class Spdemo1Spider(scrapy.Spider):
    name = 'spdemo1'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        pass
