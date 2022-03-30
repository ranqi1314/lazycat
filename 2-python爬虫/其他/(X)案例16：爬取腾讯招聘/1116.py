import requests, json, threading


class Tencent(threading.Thread):
    def __init__(self, i):
        super().__init__()
        self.i = i
        self.base_url = 'https://careers.tencent.com/tencentcareer/api/post/Query?'
        self.headers = {
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
            'referer': 'https://careers.tencent.com/search.html'
        }

    def run(self):
        self.parse()

    def parse(self):
        params = {
            'timestamp': '1572850838681',
            'countryId': '',
            'cityId': '',
            'bgIds': '',
            'productId': '',
            'categoryId': '',
            'parentCategoryId': '',
            'attrId': '',
            'keyword': '',
            'pageIndex': str(self.i),
            'pageSize': '10',
            'language': 'zh-cn',
            'area': 'cn'
        }
        response = requests.get(self.base_url, headers=self.headers, params=params)
        self.parse_json(response.text)

    def parse_json(self, text):
        # 将json字符串编程python内置对象
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

    def write_to_file(self, list_):
        for item in list_:
            with open('infos.txt', 'a+', encoding='utf-8') as fp:
                fp.writelines(str(item) + '\n')


if __name__ == '__main__':
    for i in range(1, 50):
        t = Tencent(i)
        t.start()
