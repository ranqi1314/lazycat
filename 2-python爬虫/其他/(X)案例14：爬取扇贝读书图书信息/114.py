from lxml import etree
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from urllib import parse


class Douban(object):
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.PhantomJS()
        self.wait = WebDriverWait(self.driver, 10)
        self.parse()

    # 判断数据是否存在，不存在返回空字符
    def get_text(self, text):
        if text:
            return text[0]
        return ''

    def get_content_by_selenium(self, url, xpath):
        self.driver.get(url)
        # 等待,locator对象是一个元组,此处获取xpath对应的元素并加载出来
        webelement = self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        return self.driver.page_source

    def parse(self):
        html_str = self.get_content_by_selenium(self.url, '//div[@id="root"]/div/div/div/div')
        html = etree.HTML(html_str)
        div_list = html.xpath('//div[@id="root"]/div/div/div/div/div')
        for div in div_list:
            item = {}
            '''图书名称+评分+评价数+详情页链接+作者+出版社+价格+出版日期'''
            name = self.get_text(div.xpath('.//div[@class="title"]/a/text()'))
            scores = self.get_text(div.xpath('.//span[@class="rating_nums"]/text()'))
            comment_num = self.get_text(div.xpath('.//span[@class="pl"]/text()'))
            detail_url = self.get_text(div.xpath('.//div[@class="title"]/a/@href'))
            detail = self.get_text(div.xpath('.//div[@class="meta abstract"]/text()'))
            if detail:
                detail_list = detail.split('/')
            else:
                detail_list = ['未知', '未知', '未知', '未知']
            if all([name, detail_url]):  # 如果列表里的数据为true方可执行
                item['书名'] = name
                item['评分'] = scores
                item['评论'] = comment_num
                item['详情链接'] = detail_url
                item['出版社'] = detail_list[-3]
                item['价格'] = detail_list[-1]
                item['出版日期'] = detail_list[-2]
                author_list = detail_list[:-3]
                author = ''
                for aut in author_list:
                    author += aut + ' '
                item['作者'] = author
                print(item)


if __name__ == '__main__':
    kw = 'python'
    base_url = 'https://search.douban.com/book/subject_search?'
    for i in range(10):
        params = {
            'search_text': kw,
            'cat': '1001',
            'start': str(i * 15),
        }
        url = base_url + parse.urlencode(params)
        Douban(url)
