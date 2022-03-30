import requests
from lxml import etree


class Shanbei(object):
    def __init__(self):
        self.base_url = 'https://www.shanbay.com/wordlist/110521/232414/?page=%s'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'
        }
        self.word_list = []
        self.parse()

    def get_text(self, value):
        # 防止为空报错
        if value:
            return value[0]
        return ''

    def parse(self):
        for i in range(1, 4):
            # 发送请求
            response = requests.get(self.base_url % i, headers=self.headers)
            # print(response.text)
            html = etree.HTML(response.text)
            tr_list = html.xpath('//tbody/tr')
            # print(tr_list)
            for tr in tr_list:
                item = {}  # 构造单词列表
                en = self.get_text(tr.xpath('.//td[@class="span2"]/strong/text()'))
                tra = self.get_text(tr.xpath('.//td[@class="span10"]/text()'))
                print(en, tra)
                if en:
                    item[en] = tra
                    self.word_list.append(item)


shanbei = Shanbei()