# 作业：
# 使用selenium进行测谈网以下代码的练习：
# 1.用户注册账号
# 2.用户登录账号
# 3.用户去点赞任意一篇文章
# 4.用户去评论任意一篇问题

import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.maximize_window()
driver.get("http://118.24.105.78:8080/ljindex/")
# 注册
time.sleep(5)
driver.find_element_by_xpath('//*[@id="unlogin"]/div[2]/a').click()
time.sleep(5)
driver.find_element_by_id('username').send_keys("th1230987") #输入账号
time.sleep(5)
driver.find_element_by_id('phonenum').send_keys("13309812354")
driver.find_element_by_id('password').send_keys("a12345678") #输入密码
time.sleep(5)
driver.find_element_by_id('confirpw').send_keys("a12345678") #再次输入密码
time.sleep(5)
driver.find_element_by_id('emailnum').send_keys("12309@qq.com") #输入邮箱
time.sleep(5)
driver.find_element_by_xpath('//*[@id="userRegist"]').click() #点击注册
time.sleep(1)
driver.quit()
# 登录
driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.maximize_window()
driver.get("http://118.24.105.78:8080/ljindex/")

time.sleep(5)
driver.find_element_by_xpath('//*[@id="unlogin"]/div[1]/a').click()
time.sleep(5)
driver.find_element_by_id('username').send_keys("th123098") # 输入账号
time.sleep(5)
driver.find_element_by_id('password').send_keys("a12345678") # 输入密码
time.sleep(5)
driver.find_element_by_xpath('//*[@id="userLogin"]').click() # 点击登录

time.sleep(5)
driver.find_element_by_xpath('//*[@id="xdth"]/li[1]/div/div[1]').click() #点击文章

time.sleep(5)
driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[3]/div[2]').click() # 点赞
time.sleep(5)
driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[3]/div[1]').click() #收藏
time.sleep(5)
driver.find_element_by_id('experience_comments_ctt').send_keys("woshilaizimoumoumoudepinglun")#评论
time.sleep(5)
driver.find_element_by_id('experience_comments_btn').click() # 点击评论
