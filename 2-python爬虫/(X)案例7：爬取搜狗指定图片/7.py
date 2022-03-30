import requests, json, threading, time, os
from queue import Queue


class Picture(threading.Thread):
    # 初始化
    def __init__(self, num, search, url_queue=None):
        super().__init__()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
        }
        self.num = num
        self.search = search

    # 获取爬取的页数的每页图片接口url
    def get_url(self):
        url_list = []
        for start in range(self.num):
            url = 'https://pic.sogou.com/pics?query=' + self.search + '&mode=1&start=' + str(
                start * 48) + '&reqType=ajax&reqFrom=result&tn=0'
            url_list.append(url)
        return url_list

    # 获取每页的接口资源详情
    def get_page(self, url):
        response = requests.get(url.format('蔡徐坤'), headers=self.headers)
        return response.text

    #
    def run(self):
        while True:
            # 如果队列为空代表制定页数爬取完毕
            if url_queue.empty():
                break
            else:
                url = url_queue.get()  # 本页地址
                data = json.loads(self.get_page(url))  # 获取到本页图片接口资源
                try:
                    # 每页48张图片
                    for i in range(1, 49):
                        pic = data['items'][i]['pic_url']
                        reponse = requests.get(pic)
                        # 如果文件夹不存在，则创建
                        if not os.path.exists(r'C:/Users/Administrator/Desktop/' + self.search):
                            os.mkdir(r'C:/Users/Administrator/Desktop/' + self.search)
                        with open(r'C:/Users/Administrator/Desktop/' + self.search + '/%s.jpg' % (
                                str(time.time()).replace('.', '_')), 'wb') as f:
                            f.write(reponse.content)
                            print('下载成功！')
                except:
                    print('该页图片保存完毕')


if __name__ == '__main__':
    # 1.获取初始化的爬取url
    num = int(input('请输入爬取页数（每页48张）：'))
    content = input('请输入爬取内容：')
    pic = Picture(num, content)
    url_list = pic.get_url()
    # 2.创建队列
    url_queue = Queue()
    for i in url_list:
        url_queue.put(i)
    # 3.创建线程任务
    crawl = [1, 2, 3, 4, 5]
    for i in crawl:
        pic = Picture(num, content, url_queue=url_queue)
        pic.start()
