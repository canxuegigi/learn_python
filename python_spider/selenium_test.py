#!/usr/bin/evn python
#encoding=utf-8
#Author:canxue

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time,sys

print(sys.path)
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
#若没有再查找路径，则进行配置，或者在这指定路径
driver = webdriver.Chrome(chrome_options=chrome_options)
begin_time = time.time()
driver.get('https://www.baidu.com/')
end_time = time.time()
print('wait for %s second!!!' %int(end_time-begin_time))
print(driver.name)
print(driver.current_url)
print(driver.find_element_by_id('setf').text)

#保存访问的页面的快照截图
driver.save_screenshot('wo.png')
#通过源码知道百度的输入框的id为kw
driver.find_element_by_id('kw').send_keys(u"你妹")
driver.save_screenshot('nimei.png')

driver.find_element_by_id('su').click()
#查询有时间
time.sleep(5)
driver.save_screenshot('click.png')

#获取当前页面的cookie
#单数需要传参
print(driver.get_cookie('domain'))
#返回字典列表
print(driver.get_cookies())

#模拟输入按键
#选择输入框内容
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'a')
driver.save_screenshot('xuanze.png')

#模拟输入按键
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'x')
driver.save_screenshot('jianjie.png')

#模拟输入按键
driver.find_element_by_id('kw').send_keys(u"习近平")
driver.find_element_by_id('su').send_keys(Keys.RETURN)
time.sleep(5)
driver.save_screenshot('huiche.png')

#模拟输入按键
#最大化窗口
driver.fullscreen_window()
driver.find_element_by_id('kw').clear()
driver.save_screenshot('clear.png')

#退出浏览器
driver.quit()
