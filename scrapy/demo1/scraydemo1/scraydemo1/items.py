# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Scraydemo1Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 姓名
    name = scrapy.Field()
    title = scrapy.Field()
    info = scrapy.Field()
