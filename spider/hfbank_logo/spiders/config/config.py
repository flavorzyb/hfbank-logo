# -*- coding: utf-8 -*-


class Config(object):
    url = 'http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E6%81%92%E4%B8%B0%E9%93%B6%E8%A1%8Clogo&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word=%E6%81%92%E4%B8%B0%E9%93%B6%E8%A1%8Clogo&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&rn=30&gsm=5a&1539590783093=&pn='
    max_page = 500

    @classmethod
    # 百度url
    def bd_url_list(cls):
        result = []
        for i in range(0, cls.max_page):
            result.append(cls.url + '%d' % (i * 30))
        return result
