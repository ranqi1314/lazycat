
# 链家：https://bj.fang.lianjia.com/loupan/
#
# 1、获取所有的城市的拼音
# 2、根据拼音去拼接url，获取所有的数据。
# 3、列表页：楼盘名称，均价，建筑面积，区域，商圈详情页：户型（[“8室5厅8卫”, “4室2厅3卫”, “5室2厅2卫”]）,朝向，图片（列表），用户点评（选爬）
# 难点1：
# 当该区没房子的时候，猜你喜欢这个会和有房子的块class一样，因此需要判断
#
# 难点2：
# 获取每个区的页数，使用js将页数隐藏
# https://bj.fang.lianjia.com/loupan/区/pg页数%s
# 我们可以发现规律，明明三页，当我们写pg5时候，会跳转第一页
# 因此我们可以使用while判断，当每个房子的链接和该区最大房子数相等代表该区爬取完毕
import requests
from lxml import etree


# 获取网页源码
def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    }
    response = requests.get(url, headers=headers)
    return response.text


# 获取城市拼音列表
def get_city_url():
    url = 'https://bj.fang.lianjia.com/loupan/'
    html = etree.HTML(get_html(url))
    city = html.xpath('//div[@class="filter-by-area-container"]/ul/li/@data-district-spell')
    city_url = ['https://bj.fang.lianjia.com/loupan/{}/pg%s'.format(i) for i in city]
    return city_url


# 爬取对应区的所有房子url
def get_detail(url):
    # 使用第一页来判断是否有分页
    html = etree.HTML(get_html(url % (1)))
    empty = html.xpath('//div[@class="no-result-wrapper hide"]')
    if len(empty) != 0:  # 不存在此标签代表没有猜你喜欢
        i = 1
        max_house = html.xpath('//span[@class="value"]/text()')[0]
        house_url = []
        while True:  # 分页
            html = etree.HTML(get_html(url % (i)))
            house_url += html.xpath('//ul[@class="resblock-list-wrapper"]/li/a/@href')
            i += 1
            if len(house_url) == int(max_house):
                break
        detail_url = ['https://bj.fang.lianjia.com/' + i for i in house_url]  # 该区所有房子的url
        info(detail_url)


# 获取每个房子的详细信息
def info(url):
    for i in url:
        item = {}
        page = etree.HTML(get_html(i))
        item['name'] = page.xpath('//h2[@class="DATA-PROJECT-NAME"]/text()')[0]
        item['price_num'] = page.xpath('//span[@class="price-number"]/text()')[0] + page.xpath(
            '//span[@class="price-unit"]/text()')[0]
        detail_page = etree.HTML(get_html(i + 'xiangqing'))
        item['type'] = detail_page.xpath('//ul[@class="x-box"]/li[1]/span[2]/text()')[0]
        item['address'] = detail_page.xpath('//ul[@class="x-box"]/li[5]/span[2]/text()')[0]
        item['shop_address'] = detail_page.xpath('//ul[@class="x-box"]/li[6]/span[2]/text()')[0]
        print(item)


def main():
    # 1、获取所有的城市的拼音
    city = get_city_url()
    # 2、根据拼音去拼接url，获取所有的数据。
    for url in city:
        get_detail(url)


if __name__ == '__main__':
    main()