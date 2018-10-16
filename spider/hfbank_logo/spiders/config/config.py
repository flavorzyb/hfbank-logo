# -*- coding: utf-8 -*-


class Config(object):
    words = [
        # 恒丰银行logo
        '%e6%81%92%e4%b8%b0%e9%93%b6%e8%a1%8clogo',
        # 恒丰银行标志
        '%e6%81%92%e4%b8%b0%e9%93%b6%e8%a1%8c%e6%a0%87%e5%bf%97'
        # 恒丰银行logo 矢量图
        '%e6%81%92%e4%b8%b0%e9%93%b6%e8%a1%8clogo+%e7%9f%a2%e9%87%8f%e5%9b%be',
        # 恒丰银行图标
        '%e6%81%92%e4%b8%b0%e9%93%b6%e8%a1%8c%e5%9b%be%e6%a0%87',
        # 恒丰银行机构的标志
        '%E6%81%92%E4%B8%B0%E9%93%B6%E8%A1%8C%E6%9C%BA%E6%9E%84%E7%9A%84%E6%A0%87%E5%BF%97',
    ]
    url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&rn=30&gsm=5a&1539590783093='
    max_page = 500

    @classmethod
    # 百度url
    def bd_url_list(cls):
        result = []
        for i in range(0, cls.max_page):
            for j in range(0, cls.words.__len__()):
                query = '&queryWord=' + cls.words[j] + '&word=' + cls.words[j]
                result.append(cls.url + query + '&pn=%d' % (i * 30))
        return result
