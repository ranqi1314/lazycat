# 1.首先登陆微信公众号   selenium
# 通过selenium驱动浏览器 打开登陆页面 输入账号密码 登陆 获取cookies
import time
import json
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://mp.weixin.qq.com/")

driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/div[2]/a').click()
driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/div[1]/form/div[1]/div[1]/div/span/input').clear()
driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/div[1]/form/div[1]/div[1]/div/span/input').send_keys(
    '1968834877@qq.com')
time.sleep(2)  # 延迟输入

driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/div[1]/form/div[1]/div[2]/div/span/input').send_keys(
    'password')
time.sleep(2)
driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/div[1]/form/div[3]/label').click()  # 点击
time.sleep(2)
driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/div[1]/form/div[4]/a').click()

time.sleep(15)
cookies = driver.get_cookies()  # 获取登陆之后的cookies
print(cookies)


#cookies格式不一样  这是字典
cookie={}
for items in cookies:
    cookie[items.get('name')]=items.get('value')

#保存
with open('cookies.txt', 'w') as file:  #txt存字符串,通过json模块存入
    file.write(json.dumps(cookie))

driver.close()

