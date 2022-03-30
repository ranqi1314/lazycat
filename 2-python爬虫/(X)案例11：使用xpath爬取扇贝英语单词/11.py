import json

import requests
from lxml import html
etree=html.etree

base_url = 'https://www.shanbay.com/wordlist/110521/232414/?page=%s'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/78.0.3904.70 Safari/537.36 '
}


def get_text(value):
    if value:
        return value[0]
    return ''


word_list = []
for i in range(1, 4):
    # 发送请求
    response = requests.get(base_url % i, headers=headers)
    # print(response.text)
    html = etree.HTML(response.text)
    tr_list = html.xpath('//tbody/tr')
    # print(tr_list)
    for tr in tr_list:
        item = {}#构造单词列表
        en = get_text(tr.xpath('.//td[@class="span2"]/strong/text()'))
        tra = get_text(tr.xpath('.//td[@class="span10"]/text()'))
        print(en, tra)
        if en:
            item[en] = tra
            word_list.append(item)