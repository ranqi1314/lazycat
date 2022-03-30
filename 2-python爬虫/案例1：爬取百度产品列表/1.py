# 搜索百度产品，进入百度产品界面
# 需求：爬取所以产品的界面，后续提取提供html文件

# 1.导包
import requests

# 2.确定url
url = 'https://www.baidu.com/more/'

# 3.发送请求，获取响应
r = requests.get(url)

# 4.查看状态码，是否有网站反扒策略
print(r.status_code)  # 打印200,继续完成需求

# 5.查看网页内容和编码，是否可读
print(r.text)
print(r.encoding)  # 8859,不利阅读

# 6.解决乱码
# 方案1：使用备选编码
r.encoding = r.apparent_encoding
print(r.encoding)  # utf-8，解决问题

# 方案2：解码为utf-8
with open('../../../Users/Administrator/Desktop/懒猫老师的爬虫/案例1：爬取百度产品列表/index.html', 'w', encoding='utf-8') as f:
    f.write(r.content.decode('utf-8'))

# 7.查看网页信息
print(r.headers)
print(type(r.text))
print(type(r.content))
