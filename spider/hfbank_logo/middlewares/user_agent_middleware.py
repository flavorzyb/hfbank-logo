# -*- coding: utf-8 -*-

"""
User Agent中间件
"""

from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware as ScrapyUserAgentMiddleware


class UserAgentMiddleware(ScrapyUserAgentMiddleware):
    def __init__(self, user_agent='Scrapy'):
        super(UserAgentMiddleware, self).__init__(user_agent)
        self.user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:62.0) Gecko/20100101 Firefox/62.0'
