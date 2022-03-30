# 爬取百度翻译接口url
# 利用python程序输出关键词翻译
# Post请求

# 1.导包
import requests

# 2.获取url
base_url = 'https://fanyi.baidu.com/sug'

# 3.获取关键字信息
kw = input('请输入要翻译的英文单词：')
data = {
    'kw': kw
}

# 4.请求头,以防万一
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/77.0.3865.90 Safari/537.36',
}

# 5.请求
r = requests.post(base_url, headers=headers, data=data)

# 6.浏览器看到，是列表，所以我们要打印，观察输出结果
print(r.json())  # 不方便观察

# 7.人性化处理
result = ''
for i in r.json()['data']:
    result += i['v'] + '\n'
print(kw + '的翻译结果为：')
print(result)
