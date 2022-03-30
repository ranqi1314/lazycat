import json
import re
import requests
import random

query = 'python'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/99.0.4844.82 '
                  'Safari/537.36',
    'Refer': 'https://mp.weixin.qq.com/cgi-bin/appmsg?t=media/appmsg_edit_v2&action=edit&isNew=1&type=77&createType=8'
             '&token=301737213&lang=zh_CN',
    'host': 'https://mp.weixin.qq.com',
}
# 拿到cookies之后，去请求，会跳转到个人首页，这时候就会有token
# 构造我们的data数据包 模拟post请求，返回数据
with open('cookies.txt', 'r') as file:
    cookie = file.read()

cookies = json.loads(cookie)
# print(cookies)

url = 'https://mp.weixin.qq.com/'

response = requests.get(url, cookies)
token = re.findall(r'token=(\d+)', str(response.url))

# print(token)

data = {
    'token': token,
    'lang': 'zh_CN',
    'f': 'json',
    'ajax': ' 1',
    'random': random.random(),
    'url': query,
    'allow_reprint': '0',
    'begin': ' 0',
    'count': '10',
}

search_url = 'https://mp.weixin.qq.com/cgi-bin/operate_appmsg?sub=check_appmsg_copyright_stat'
search_response = requests.post(search_url, cookies=cookies,data=data,headers=headers)

print(search_response.text)
