import requests
import asyncio
import aiohttp
import time


class Crawl_Image:
    def __init__(self):
        self.url = 'https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js'
        self.url1 = "https://game.gtimg.cn/images/lol/act/img/js/hero/{}.js"
        self.path = r'E:\ZT_Niko\LOL皮肤抓取\lol_hero_skin'
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        }

    async def get_image(self, url):
        '''异步请求库aiohttp 加快图片 url 的网页请求'''
        async with aiohttp.ClientSession() as session:
            response = await session.get(url)
            content = await response.read()
            return content

    async def download_image(self, image):
        html = await self.get_image(image[0])
        with open(self.path + "\\" + image[1] + '.jpg', 'wb') as f:
            f.write(html)
        print('下载第{}张图片成功'.format(image[1]))

    def run(self):
        hero_list = requests.get(self.url, headers=self.headers).json()
        print(hero_list)
        for hero in hero_list['hero']:
            heroId = hero['heroId']
            skins = requests.get(self.url1.format(heroId)).json()['skins']

            task = [asyncio.ensure_future(self.download_image((skin['mainImg'], skin['name']))) for skin in skins]

            loop = asyncio.get_event_loop()
            # 执行协程
            loop.run_until_complete(asyncio.wait(task))


if __name__ == '__main__':
    crawl_image = Crawl_Image()
    crawl_image.run()
