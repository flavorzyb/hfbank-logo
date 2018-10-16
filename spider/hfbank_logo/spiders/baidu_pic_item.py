# -*- coding: utf-8 -*-
import scrapy


class BaiDuPicItem(scrapy.Item):
    image_urls = scrapy.Field()
    images = scrapy.Field()
