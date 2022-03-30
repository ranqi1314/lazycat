# 循环请求和保存
# 两种方案

# 1.导入基本包
import requests
from lxml import html

etree = html.etree

# 3.以防万一
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/77.0.3865.90 Safari/537.36 '
}

# 4.循环请求
for i in range(1, 101):
    # 2.获取基本链接
    base_url = 'https://www.runoob.com/python/python-exercise-example{}.html'.format(i)
    r = requests.get(base_url, headers=headers)
    html1 = etree.HTML(r.text)
    # print(r.text)
    # print(html)
    content = '题目：' + html1.xpath('//div[@id="content"]/p[2]/text()')[0] + '\n'
    fenxi = html1.xpath('//div[@id="content"]/p[position()>=2]/text()')[0]
    daima = ''.join(html1.xpath('//div[@class="hl-main"]/span/text()')) + '\n'
    haha = '"""\n' + content + fenxi + daima + '\n"""'
    with open('1/练习实例%s.py' % i, 'w', encoding='utf-8') as file:
        file.write(haha)
    print(content)