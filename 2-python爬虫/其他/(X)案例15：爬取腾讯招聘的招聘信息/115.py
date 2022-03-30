import json
from lxml import etree
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from urllib import parse

class Tencent(object):
    def __init__(self,url):
        self.url = url
        self.driver = webdriver.PhantomJS()
        self.wait = WebDriverWait(self.driver,10)
        self.parse()

    def get_text(self,text):
        if text:
            return text[0]
        return ''

    def get_content_by_selenium(self,url,xpath):
        self.driver.get(url)
        webelement = self.wait.until(EC.presence_of_element_located((By.XPATH,xpath)))
        return self.driver.page_source

    def parse(self):
        html_str = self.get_content_by_selenium(self.url,'//div[@class="correlation-degree"]')
        html = etree.HTML(html_str)
        div_list = html.xpath('//div[@class="recruit-wrap recruit-margin"]/div')
        # print(div_list)
        for div in div_list:
            '''title,工作简介,工作地点,发布时间,岗位类别,详情页链接'''
            job_name = self.get_text(div.xpath('.//h4[@class="recruit-title"]/text()'))
            job_loc = self.get_text(div.xpath('.//p[@class="recruit-tips"]/span[2]/text()'))
            job_gangwei = self.get_text(div.xpath('.//p/span[3]/text()') ) # -----岗位
            job_time = self.get_text(div.xpath('.//p/span[4]/text()') ) # -----发布时间
            item = {}
            item['职位'] = job_name
            item['地点'] = job_loc
            item['岗位'] = job_gangwei
            item['发布时间'] = job_time
            print(item)
            self.write_(item)

    def write_(self,item):
        with open('Tencent_job_100page.json', 'a+', encoding='utf-8') as file:
            json.dump(item, file)

if __name__ == '__main__':
    base_url = 'https://careers.tencent.com/search.html?index=%s'
    for i in range(1,100):
        Tencent(base_url %i)