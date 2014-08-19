# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WaffenexporteItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    supplier = scrapy.Field()
    recipient = scrapy.Field()
    year = scrapy.Field()
    tiv = scrapy.Field()
