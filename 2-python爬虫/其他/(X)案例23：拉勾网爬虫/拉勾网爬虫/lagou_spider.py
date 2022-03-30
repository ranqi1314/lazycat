import requests  # 帮助我们发送请求
import xlwt
import time


def get_json(url, data):  # 获取岗位信息
    # 模拟浏览器上网
    headers = {
        'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/81.0.4044.9 Safari/537.36',
    }
    # time.sleep(3)
    session = requests.session()
    temp_url = 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
    session.get(url=temp_url, headers=headers)
    cookie = session.cookies
    response = session.post(url, data=data, headers=headers, cookies=cookie)
    result = response.json()
    info = result['content']['positionResult']['result']
    info_list = []
    for job in info:
        information = []
        information.append(job['positionId'])  # 岗位对应ID
        information.append(job['city'])  # 岗位对应城市
        information.append(job['companyFullName'])  # 公司全名
        information.append(job['companyLabelList'])  # 福利待遇
        information.append(job['district'])  # 工作地点
        information.append(job['education'])  # 学历要求
        information.append(job['firstType'])  # 工作类型
        information.append(job['formatCreateTime'])  # 发布时间
        information.append(job['positionName'])  # 职位名称
        information.append(job['salary'])  # 薪资
        information.append(job['workYear'])  # 工作年限
        info_list.append(information)
    return info_list


def main():
    info_result = []
    # 岗位id 城市 公司全名 福利待遇 工作地点 学历要求 工作类型 发布时间 职位名称 薪资 工作年限
    title = ['岗位id', '城市', '公司全名', '福利待遇', '工作地点', '学历要求', '工作类型', '发布时间', '职位名称', '薪资', '工作年限']
    info_result.append(title)
    for x in range(1, 6):
        url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
        data = {
            'first': 'false',
            'pn': x,
            'kd': 'python',
        }
        try:
            info = get_json(url, data)
            info_result = info_result + info
            print("第%s页正常采集" % x)
        except Exception as  msg:
            print("第%s页出现问题" % x)
        # 创建workbook,即excel
        workbook = xlwt.Workbook(encoding='utf-8')
        # 创建表
        worksheet = workbook.add_sheet('lagouzp1')
        for i, row in enumerate(info_result):
            print(row)
            for j, col in enumerate(row):
                # print(col)
                worksheet.write(i, j, col)
            workbook.save('lagouzp.xls')


if __name__ == '__main__':
    main()
