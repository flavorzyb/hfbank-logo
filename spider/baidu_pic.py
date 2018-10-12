#-*- encoding: UTF-8 -*-
#---------------------------------import------------------------------------
import re
import scrapy
import json
from tutorial.items import CtripHotel, Soufang
from scrapy import Request
from scrapy.selector import Selector
import sys
import uuid
#---------------------------------------------------------------------------
class DpSpider(scrapy.Spider):
    reload(sys)
    sys.setdefaultencoding('utf-8')
    #handle_httpstatus_list = [404,408,504]
    name = "baidu_pic"
    #allowed_domains = ["http://newhouse.cd.fang.com/"]
    download_delay = 1
    start_urls = [
        "http://www.baidu.com"
    ]


    def parse(self, response):
        '获取商铺详情页'
        req = []
        keyword='恒丰银行'
        for i in range(5):
            pn=i*30
            url='http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord='+keyword+'&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&word='+keyword+'&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=1&fr=&expermode=&pn='+str(pn)+'&rn=30&gsm=1e&1539222606261='

            r = Request(url,callback=self.parse_pic)
            req.append(r)
        return req

    def parse_pic(self, response):
        req=[]
        #print response.body
        js=json.loads(response.body)
        pics=[]
        #print s
        #piclist=s['picid']
        #print piclist
        datas=js.get('data')
        for data in datas:
            thumbURL=data.get('thumbURL')#.decode('unicode_escape')
            if thumbURL:
                pics.append(thumbURL)

        
        result={'image_urls':pics,'movieid':'baidu'}

        return result #{'data':json.dumps(dict(result)).decode('unicode_escape')}
