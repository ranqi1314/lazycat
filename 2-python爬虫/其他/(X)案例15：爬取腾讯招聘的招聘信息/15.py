import time
from lxml import html
from selenium import webdriver
etree=html.etree

driver = webdriver.PhantomJS()
base_url = 'https://careers.tencent.com/search.html?index=%s'
job=[]

def getText(text):
    if text:
        return text[0]
    else:
        return ''


def parse(text):
    html = etree.HTML(text)
    div_list = html.xpath('//div[@class="correlation-degree"]/div[@class="recruit-wrap recruit-margin"]/div')
    # print(div_list)
    for i in div_list:
        item = {}
        job_name = i.xpath('a/h4/text()')  # ------职位
        job_loc = i.xpath('a/p/span[2]/text()')  # --------地点
        job_gangwei = i.xpath('a/p/span[3]/text()')  # -----岗位
        job_time = i.xpath('a/p/span[4]/text()')  # -----发布时间
        item['职位']=job_name
        item['地点']=job_loc
        item['岗位']=job_gangwei
        item['发布时间']=job_time
        job.append(item)

if __name__ == '__main__':
    for i in range(1, 11):
        driver.get(base_url % i)
        text = driver.page_source
        # print(text)
        time.sleep(1)
        parse(text)
    print(job)