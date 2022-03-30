# 爬取百度贴吧前十页
# 涉及到翻页,需要构造url
# 需要遍历请求

# 1.导包
import requests, os

# 2.确定url链接
# https://tieba.baidu.com/f?ie=utf-8&kw=jk&fr=search
# https://tieba.baidu.com/f?kw=jk&ie=utf-8&pn=50
# https://tieba.baidu.com/f?kw=jk&ie=utf-8&pn=100
base_url = 'https://tieba.baidu.com/'
# 3.设置头部，以防万一
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/77.0.3865.90 Safari/537.36',
}

# 4.5.设置存储路径,导入os包
dirname = './tieba/jk/'
if not os.path.exists(dirname):
    os.makedirs(dirname)

# 4.循环请求和保存
for i in range(0, 10):  # 设置页数
    params = {
        'ie': 'utf-8',
        'kw': 'jk',
        'pn': str(i * 50)  # 50倍递增
    }
    # 发出请求
    r = requests.get(base_url, headers=headers, params=params)
    # 5.保存
    with open(dirname + 'jk第%s页.html' % (i + 1), 'w', encoding='utf-8') as f:
        f.write(r.content.decode('utf-8'))
print('完成！')
