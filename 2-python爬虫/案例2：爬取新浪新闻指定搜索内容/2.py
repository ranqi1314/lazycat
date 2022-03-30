# 爬取新浪新闻指定搜索内容
# 键入搜索内容
# 以html保存
# 相当于有一个带参数url连接请求


# 1.导包
import requests

# 2.寻找基础url
# https://search.sina.com.cn/?q=搜索词c=news&from=channel&ie=utf-8
base_url = 'https://search.sina.com.cn/'
# 3.以防万一，设置headers
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/77.0.3865.90 Safari/537.36',
}
# 4.补充构成url连接的键值对
key = '孙悟空'
params = {
    'q': key,
    'c': 'news',
    'from': 'channel',
    'ie': 'utf-8',
}

# 5.准备完成，发出请求
r = requests.get(base_url, headers=headers, params=params)
# 6.查看完整连接
print(r.url)

# 7.保存内容
with open('sina_news.html', 'w', encoding='utf-8') as f:
    f.write(r.content.decode('utf-8'))
