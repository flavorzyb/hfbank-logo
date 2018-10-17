# -*- coding: utf-8 -*-
import scrapy
import config
import json
from baidu_pic_item import BaiDuPicItem


class BaiDuSpider(scrapy.Spider):
    name = 'baidu'
    start_urls = config.Config.bd_url_list()

    def parse(self, response):
        js = json.loads(response.body)
        data = js.get('data')
        images = []
        for v in data:
            if 'middleURL' in v:
                images.append(v['middleURL'])

        item = BaiDuPicItem()
        item['image_urls'] = images
        yield item

