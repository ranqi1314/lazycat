'''
	要求：抓取50页
		字段：总价，描述，评论数量，详情页链接
	用正则爬取。

'''
import requests, re,json


class Drugs:
    def __init__(self):
        self.url = url = 'https://www.111.com.cn/categories/953710-j%s.html'
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
        }
        self.Drugs_list=[]
        self.parse()

    def parse(self):
        for i in range(51):
            response = requests.get(self.url % i, headers=self.headers)
            # print(response.text)
            # 字段：药名，总价，评论数量，详情页链接
            Drugsul_pattern = re.compile('<ul id="itemSearchList" class="itemSearchList">(.*?)</ul>', re.S)
            Drugsul = Drugsul_pattern.search(response.text).group()
            # print(Drugsul)
            Drugsli_list_pattern = re.compile('<li id="producteg(.*?)</li>', re.S)
            Drugsli_list = Drugsli_list_pattern.findall(Drugsul)
            Drugsli_list = Drugsli_list
            # print(Drugsli_list)
            for drug in Drugsli_list:
                # ---药名
                item={}
                name_pattern = re.compile('alt="(.*?)"', re.S)
                name = name_pattern.search(str(drug)).group(1)
                # print(name)
                # ---总价
                total_pattern = re.compile('<span>(.*?)</span>', re.S)
                total = total_pattern.search(drug).group(1).strip()
                # print(total)
                # ----评论
                comment_pattern = re.compile('<em>(.*?)</em>')
                comment = comment_pattern.search(drug)
                if comment:
                    comment_group = comment.group(1)
                else:
                    comment_group = '0'
                # print(comment_group)
                # ---详情页链接
                href_pattern = re.compile('" href="//(.*?)"')
                href='https://'+href_pattern.search(drug).group(1).strip()
                # print(href)
                item['药名']=name
                item['总价']=total
                item['评论']=comment
                item['链接']=href
                self.Drugs_list.append(item)
drugs = Drugs()
print(drugs.Drugs_list)
