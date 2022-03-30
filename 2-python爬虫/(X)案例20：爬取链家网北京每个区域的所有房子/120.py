import json, threading
from selenium import webdriver
from lxml import etree
from queue import Queue


class Lianjia(threading.Thread):
    def __init__(self, city_list=None, city_name_list=None):
        super().__init__()
        self.driver = webdriver.PhantomJS()
        self.city_name_list = city_name_list
        self.city_list = city_list

    def get_element(self, url):  # 获取element对象的
        self.driver.get(url)
        html = etree.HTML(self.driver.page_source)
        return html

    def get_city(self):
        html = self.get_element('https://bj.lianjia.com/ershoufang/')
        city_list = html.xpath('//div[@data-role="ershoufang"]/div/a/@href')
        city_list = ['https://bj.lianjia.com' + url + 'pg%s' for url in city_list]
        city_name_list = html.xpath('//div[@data-role="ershoufang"]/div/a/text()')
        return city_list, city_name_list

    def run(self):
        lis = []  # 存放所有区域包括房子
        while True:
            if self.city_name_list.empty() and self.city_list.empty():
                break
            item = {}  # 存放一个区域
            sum_house = []  # 存放每个区域的房子
            item['区域'] = self.city_name_list.get()  # 城区名字
            for page in range(1, 3):
                # print(self.city_list.get())
                html = self.get_element(self.city_list.get() % page)
                '''名称, 房间规模，建设时间, 朝向, 详情页链接'''
                title_list = html.xpath('//div[@class="info clear"]/div/a/text()')  # 所有标题
                detail_url_list = html.xpath('//div[@class="info clear"]/div/a/@href')  # 所有详情页
                detail_list = html.xpath('//div[@class="houseInfo"]/text()')  # 该页所有的房子信息列表，
                for i, content in enumerate(title_list):
                    house = {}
                    detail = detail_list[i].split('|')
                    house['名称'] = content  # 名称
                    house['规模'] = detail[0] + detail[1]  # 规模
                    house['建设时间'] = detail[-2]  # 建设时间
                    house['朝向'] = detail[2]  # 朝向
                    house['详情链接'] = detail_url_list[i]  # 详情链接
                    sum_house.append(house)
            item['二手房'] = sum_house
            lis.append(item)
            print(item)


if __name__ == '__main__':
    q1 = Queue()#路由
    q2 = Queue()#名字
    lj = Lianjia()
    city_url, city_name = lj.get_city()
    for c in city_url:
        q1.put(c)
    for c in city_name:
        q2.put(c)
        # 创建一个列表，列表的数量就是开启线程的数量
    crawl_list = [1, 2, 3, 4, 5]
    for crawl in crawl_list:
        # 实例化对象
        LJ = Lianjia(city_name_list=q2,city_list=q1)
        LJ.start()