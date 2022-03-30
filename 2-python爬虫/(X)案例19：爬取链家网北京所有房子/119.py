import requests, threading
from lxml import etree
from queue import Queue
import pymongo

class House(threading.Thread):
    def __init__(self, q=None):
        super().__init__()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
        }
        self.q = q

    # 获取网页源码
    def get_html(self, url):
        response = requests.get(url, headers=self.headers)
        return response.text

    # 获取城市拼音列表
    def get_city_url(self):
        url = 'https://bj.fang.lianjia.com/loupan/'
        html = etree.HTML(self.get_html(url))
        city = html.xpath('//div[@class="filter-by-area-container"]/ul/li/@data-district-spell')
        city_url = ['https://bj.fang.lianjia.com/loupan/{}/pg%s'.format(i) for i in city]
        return city_url

    # 爬取对应区的所有房子url
    def get_detail(self, url):
        # 使用第一页来判断是否有分页
        html = etree.HTML(self.get_html(url % (1)))
        empty = html.xpath('//div[@class="no-result-wrapper hide"]')
        if len(empty) != 0:  # 不存在此标签代表没有猜你喜欢
            i = 1
            max_house = html.xpath('//span[@class="value"]/text()')[0]
            house_url = []
            while True:  # 分页
                html = etree.HTML(self.get_html(url % (i)))
                house_url += html.xpath('//ul[@class="resblock-list-wrapper"]/li/a/@href')
                i += 1
                if len(house_url) == int(max_house):
                    break
            detail_url = ['https://bj.fang.lianjia.com/' + i for i in house_url]  # 该区所有房子的url
            self.info(detail_url)

    # 获取每个房子的详细信息
    def info(self, url):
        for i in url:
            item = {}
            page = etree.HTML(self.get_html(i))
            item['name'] = page.xpath('//h2[@class="DATA-PROJECT-NAME"]/text()')[0]
            item['price_num'] = page.xpath('//span[@class="price-number"]/text()')[0] + page.xpath(
                '//span[@class="price-unit"]/text()')[0]
            detail_page = etree.HTML(self.get_html(i + 'xiangqing'))
            item['type'] = detail_page.xpath('//ul[@class="x-box"]/li[1]/span[2]/text()')[0]
            item['address'] = detail_page.xpath('//ul[@class="x-box"]/li[5]/span[2]/text()')[0]
            item['shop_address'] = detail_page.xpath('//ul[@class="x-box"]/li[6]/span[2]/text()')[0]
            print(item)

    def run(self):
        # 1、获取所有的城市的拼音
        # city = self.get_city_url()
        # 2、根据拼音去拼接url，获取所有的数据。
        while True:
            if self.q.empty():
                break
            self.get_detail(self.q.get())


if __name__ == '__main__':
    # 1.先获取区列表
    house = House()
    city_list = house.get_city_url()
    # 2.将去加入队列
    q = Queue()
    for i in city_list:
        q.put(i)
    # 3.创建线程任务
    a = [1, 2, 3, 4]
    for i in a:
        p = House(q)
        p.start()