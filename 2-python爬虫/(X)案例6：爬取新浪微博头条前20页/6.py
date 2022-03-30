import requests, pymysql
from lxml import html
etree=html.etree

def get_element(i):
    base_url = 'https://weibo.com/a/aj/transform/loadingmoreunlogin?'
    headers = {
        'Referer': 'https://weibo.com/?category=1760',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/77.0.3865.90 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    params = {
        'ajwvr': '6',
        'category': '1760',
        'page': i,
        'lefnav': '0',
        'cursor': '',
        '__rnd': '1573735870072',
    }
    response = requests.get(base_url, headers=headers, params=params)
    response.encoding = 'utf-8'
    info = response.json()
    return etree.HTML(info['data'])


def main():
    for i in range(1, 20):
        html = get_element(i)
        # 标题，发布人，发布时间,详情链接
        title = html.xpath('//a[@class="S_txt1"]/text()')
        author_time = html.xpath('//span[@class]/text()')
        author = [author_time[i] for i in range(len(author_time)) if i % 2 == 0]
        time = [author_time[i] for i in range(len(author_time)) if i % 2 == 1]
        url = html.xpath('//a[@class="S_txt1"]/@href')
        for j, tit in enumerate(title):
            title1 = tit
            time1 = time[j]
            url1 = url[j]
            author1 = author[j]
            # print(title1,url1,time1,author1)
            connect_mysql(title1, time1, author1, url1)


def connect_mysql(title, time, author, url):
    db = pymysql.connect(host='localhost', user='root', password='123456', database='news')
    cursor = db.cursor()
    sql = 'insert into sina_news(title,send_time,author,url) values("' + title + '","' + time + '","' + author + '","' + url + '")'
    print(sql)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()


if __name__ == '__main__':
    main()
