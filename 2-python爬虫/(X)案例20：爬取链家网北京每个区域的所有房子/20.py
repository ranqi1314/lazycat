#爬取链家二手房信息。
# 要求：
# 1.爬取的字段:
# 名称,房间规模、价格,建设时间,朝向,详情页链接
# 2.写三个文件：
# 1.简单py 2.面向对象 3.改成多线程

from selenium import webdriver
from lxml import html
etree=html.etree


def get_element(url):
    driver.get(url)
    html = etree.HTML(driver.page_source)
    return html


lis = []  # 存放所有区域包括房子
driver = webdriver.PhantomJS()
html = get_element('https://bj.lianjia.com/ershoufang/')
city_list = html.xpath('//div[@data-role="ershoufang"]/div/a/@href')
city_name_list = html.xpath('//div[@data-role="ershoufang"]/div/a/text()')
for num, city in enumerate(city_list):
    item = {}  # 存放一个区域
    sum_house = []  # 存放每个区域的房子
    item['区域'] = city_name_list[num]  # 城区名字
    for page in range(1, 3):
        city_url = 'https://bj.lianjia.com' + city + 'pg' + str(page)
        html = get_element(city_url)
        '''名称, 房间规模，建设时间, 朝向, 详情页链接'''
        title_list = html.xpath('//div[@class="info clear"]/div/a/text()')  # 所有标题
        detail_url_list = html.xpath('//div[@class="info clear"]/div/a/@href')  # 所有详情页
        detail_list = html.xpath('//div[@class="houseInfo"]/text()')  # 该页所有的房子信息列表，
        city_price_list = html.xpath('//div[@class="totalPrice"]/span/text()')
        for i, content in enumerate(title_list):
            house = {}
            detail = detail_list[i].split('|')
            house['名称'] = content  # 名称
            house['价格']=city_price_list[i]+'万'#价格
            house['规模'] = detail[0] + detail[1]  # 规模
            house['建设时间'] = detail[-2]  # 建设时间
            house['朝向'] = detail[2]  # 朝向
            house['详情链接'] = detail_url_list[i]  # 详情链接
            sum_house.append(house)
    item['二手房'] = sum_house
    print(item)
    lis.append(item)