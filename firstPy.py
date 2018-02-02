# coding=utf-8
# !D:/python/firstPy.py
# -*- coding: utf-8 -*-


# coding:utf-8
from selenium import webdriver

import time # 时间模块
import json

def fib(n):
    a, b = 0, 1
    while a < n:
        print (a)
        a, b = b, a+b

fib(1000)


print('hello world!');
print "123"

driver = webdriver.Chrome()

# 启动浏览器后获取cookie
cookieStr = driver.get_cookies()

driver.get("http://www.ubody.net")

# 打开主页后获取cookie
print driver.get_cookies()

# json 格式化输出
print json.dumps(cookieStr, indent=5)


# driver.set_window_position(0,0)
# time.sleep(3)  # 设置休眠


str = "15112314954"
print(str)
# str1 = str.strip(str.__len__(str)-5)

# 截取字符串
# stamp = “1213fwfwefwfew”
# 取前面5个  stamp[:5]  取后面5个 stamp[-5:]  从前面开始取，不包括最后两个stamp[:-2] 从第1个取到第2个stamp[0:2]
driver.find_element_by_id("login_username").send_keys(str)
driver.find_element_by_id("login_password").send_keys(str[-6:])
# xpath 获取元素方式
print driver.find_element_by_xpath("//*[@id='login_username']")
# css　获取元素方式
driver.find_element_by_css_selector("#login_checkcode")
# xpath 索引查找相同元素标签的位置，定位n级从1开始
# driver.find_element_by_xpath("//select[@id='login_username']/option[n]")

# str2 = driver.find_element_by_id("login_checkcode")


# xpath 模糊匹配定位元素

#driver.find_element_by_xpath("//*[contains(text(),'忘记密码')]").click()
# 模糊匹配某个属性
#driver.find_element_by_xpath("//*[contains(@class,'col-xs-6 text-left')]").click()
# 模糊匹配以什么开头
#driver.find_element_by_xpath("//*[starts-with(@id,'')]").click()
# 模糊匹配以什么结尾
#driver.find_element_by_xpath("//*ends-with(@id,'')").click()
# 正则表达式匹配
#driver.find_element_by_xpath("//*[matchs(text(),'立即免费注册')]").click()


c1 = {
  u'domain': u'.ubody.net',
  u'secure': False,
  u'value': u'ltk036125h7oob0pub09s868l7',
  u'expiry': 1516328582,
  u'path': u'/',
  u'httpOnly': False,
  u'name': u'PHPSESSID'
}

c2 = {
  u'domain': u'.ubody.net',
  u'secure': False,
  u'value': u'4638a68be02fdbaad540925293f50a45',
  u'expiry': 1516328582,
  u'path': u'/',
  u'httpOnly': False,
  u'name': u'login_user_state'
}

c3 = {
  u'domain': u'.ubody.net',
  u'secure': False,
  u'value': u'71895270-1500547547-null%7C1500963126',
  u'expiry': 1516328582,
  u'path': u'/',
  u'httpOnly': False,
  u'name': u'CNZZDATA1261240568'
}

driver.add_cookie(c1)   # 登录必备cookie
driver.add_cookie(c2)   # 登录必备cookie
# driver.add_cookie(c3)


driver.refresh()

driver.find_element_by_class_name("login-btn").click()
# driver.find_element_by_class_name("btn-block").click()


time.sleep(100)
driver.quit()
