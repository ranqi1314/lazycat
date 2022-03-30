# -*- coding: utf-8 -*-
# @Author  : Niko
# @Function:

import json
import os
import re
import random
import requests
from requests.exceptions import RequestException

# 本地保存地址
base_path = 'D:/ZT_Niko/LOL皮肤抓取/lol_hero_skin'
# 人机识别信息
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/80.0.3987.122 Safari/537.36'}
# 对应的皮肤图片数据
# 处理文件名,window系统下有些字符不允许出现\/:*?"<>| K\DA皮肤引起此问题
def handle_str(_str):
    temp = re.sub('[\\\/:*?"<>|]', '', _str)
    if len(temp) == 0:
        return ''.join(str(random.choice(range(10))) for _ in range(10))
    return temp

# 下载图片
def download_img(img_url, _base_path, name):
    r = requests.get(img_url, headers=headers, stream=True)
    print(name, r.status_code)  # 返回状态码
    if r.status_code == 200:
        name = handle_str(name)
        open(_base_path + "\\" + name + '.jpg', 'wb').write(r.content)  # 将内容写入图片
        print("done")

def load_hero_skin(heroId):
    hero_img_url_prefix = 'https://game.gtimg.cn/images/lol/act/img/js/hero/'
    hero_img_url_suffix = '.js'
    response = requests.get(hero_img_url_prefix + heroId + hero_img_url_suffix, headers=headers)
    html = json.loads(response.text)  # 将网页内容以json返回
    skinsList = html.get('skins')  # 皮肤列表
    heroName = html.get('hero').get('name')  # 黑暗之女
    heroTitle = html.get('hero').get('title')  # 安妮
    heroName = handle_str(heroName)
    heroTitle = handle_str(heroTitle)
    hero_skins_path = base_path + '\\' + heroName + ' ' + heroTitle
    if not os.path.exists(hero_skins_path):
        print('不存在,创建中。。。')
        os.makedirs(hero_skins_path, 755)
    for n in skinsList:
        skinName = n.get('name')
        _chromas = n.get('chromas')  # 0:是基础、1:炫彩
        mainImg = n.get('mainImg')  # 皮肤图片地址

        if _chromas == '0':
            # 下载该图片
            download_img(mainImg, hero_skins_path, skinName)

# 获取全部英雄对象json
def get_hero_json():
    try:
        hero_list_url = 'https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js'
        response = requests.get(hero_list_url, headers=headers)
        html = json.loads(response.text)  # 将网页内容以json返回
        print('版本:', html.get('version'))
        print('文件名:', html.get('fileName'))
        print('文件更新时间:', html.get('fileTime'))
        print('总英雄数量:', len(html.get('hero')))
        for i in html.get('hero'):
            heroId = i.get('heroId')
            load_hero_skin(heroId)
    except RequestException:
        return None

def main():
    get_hero_json()

# 当.py文件被直接运行时，当.py文件以模块形式被导入时，if __name__ == '__main__'之下的代码块不被运行。
if __name__ == '__main__':
    main()


