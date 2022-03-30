# -*- coding: utf-8 -*-
# @Author  : Niko
# @Function:

import requests
import re
import os

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'}
name = input('输入你要爬取的关键字：')
num = 0
x = input('您要爬取几张呢?，输入1等于60张图片。：')


for i in range(int(x)):
    url = 'https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word='+name
    res = requests.get(url,headers=headers)
    html_1 = res.content.decode()
    a = re.findall('"objURL":"(.*?)",',html_1)
    if not os.path.exists('img/'):
        os.makedirs('img/')
    for b in a:
        num = num +1
        try:
            img = requests.get(b)
        except Exception as e:
            print('第'+str(num)+'张图片无法下载------------')
            print(str(e))
            continue
        f = open('./img/'+name+str(num)+'.jpg','ab')
        print('---------正在下载第'+str(num)+'张图片----------')
        f.write(img.content)
        f.close()
print('下载完成')
