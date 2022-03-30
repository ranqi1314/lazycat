import time, json
from lxml import etree
from selenium import webdriver

base_url = 'https://search.douban.com/book/subject_search?search_text=python&cat=1001&start=%s'

driver = webdriver.PhantomJS()


def get_text(text):
    if text:
        return text[0]
    return ''


def parse_page(text):
    html = etree.HTML(text)
    div_list = html.xpath('//div[@id="root"]/div/div/div/div/div/div[@class="item-root"]')
    # print(div_list)
    for div in div_list:
        item = {}
        '''
        图书名称,评分,评价数,详情页链接,作者,出版社,价格,出版日期
        '''
        name = get_text(div.xpath('.//div[@class="title"]/a/text()'))
        scores = get_text(div.xpath('.//span[@class="rating_nums"]/text()'))
        comment_num = get_text(div.xpath('.//span[@class="pl"]/text()'))
        detail_url = get_text(div.xpath('.//div[@class="title"]/a/@href'))
        detail = get_text(div.xpath('.//div[@class="meta abstract"]/text()'))
        if detail:
            detail_list = detail.split('/')
        else:
            detail_list = ['未知', '未知', '未知', '未知']
        # print(detail_list)
        if all([name, detail_url]):  # 如果名字和详情链接为true
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
            write_singer(item)


def write_singer(item):
    with open('book.json', 'a+', encoding='utf-8') as file:
        json.dump(item, file)


if __name__ == '__main__':
    for i in range(10):
        driver.get(base_url % (i * 15))
        # 等待
        time.sleep(2)
        html_str = driver.page_source
        parse_page(html_str)