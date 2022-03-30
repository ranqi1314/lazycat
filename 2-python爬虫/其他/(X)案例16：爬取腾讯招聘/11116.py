import requests,json,time,threading
from queue import Queue
class Tencent(threading.Thread):
    def __init__(self,url,headers,name,q):
        super().__init__()
        self.url= url
        self.name = name
        self.q = q
        self.headers = headers

    def run(self):
        self.parse()

    def write_to_file(self,list_):
        with open('infos1.txt', 'a+', encoding='utf-8') as fp:
            for item in list_:

                fp.write(str(item))
    def parse_json(self,text):
        #将json字符串编程python内置对象
        infos = []
        json_dict = json.loads(text)
        for data in json_dict['Data']['Posts']:
            RecruitPostName = data['RecruitPostName']
            CategoryName = data['CategoryName']
            Responsibility = data['Responsibility']
            LastUpdateTime = data['LastUpdateTime']
            detail_url = data['PostURL']
            item = {}
            item['RecruitPostName'] = RecruitPostName
            item['CategoryName'] = CategoryName
            item['Responsibility'] = Responsibility
            item['LastUpdateTime'] = LastUpdateTime
            item['detail_url'] = detail_url
            # print(item)
            infos.append(item)
        self.write_to_file(infos)
    def parse(self):
        while True:
            if self.q.empty():
                break
            page = self.q.get()
            print(f'==================第{page}页==========================in{self.name}')
            params = {
                'timestamp': '1572850797210',
                'countryId':'',
                'cityId':'',
                'bgIds':'',
                'productId':'',
                'categoryId':'',
                'parentCategoryId':'',
                'attrId':'',
                'keyword':'',
                'pageIndex': str(page),
                'pageSize': '10',
                'language': 'zh-cn',
                'area': 'cn'
            }
            response = requests.get(self.url,params=params,headers=self.headers)
            self.parse_json(response.text)

if __name__ == '__main__':
    start = time.time()
    base_url = 'https://careers.tencent.com/tencentcareer/api/post/Query?'
    headers= {
        'referer': 'https: // careers.tencent.com / search.html',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin'
    }
    #1创建任务队列
    q = Queue()
    #2给队列添加任务，任务是每一页的页码
    for page in range(1,50):
        q.put(page)
    # print(queue)
    # while not q.empty():
    #     print(q.get())
    #3.创建一个列表
    crawl_list = ['aa','bb','cc','dd','ee']
    list_ = []
    for name in crawl_list:
        t = Tencent(base_url,headers,name,q)
        t.start()
        list_.append(t)
    for l in list_:
        l.join()
    # 3.4171955585479736
    print(time.time()-start)