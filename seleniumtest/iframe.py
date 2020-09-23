
import time
from selenium import webdriver
from seleniumtools import find_element

driver = webdriver.Chrome(executable_path="./chromedriver")
driver.maximize_window()  # 让浏览器最大化
driver.get("http://118.24.105.78:9000/shopxo/admin.php")

username = ('xpath', '/html/body/div[1]/div/div[2]/div/form/div/div[1]/input')
password = ('xpath', '/html/body/div[1]/div/div[2]/div/form/div/div[2]/input')
loginbtn = ('xpath', '/html/body/div[1]/div/div[2]/div/form/div/div[3]/button')

find_element(driver, username).send_keys("admin")
find_element(driver, password).send_keys("shopxo")
find_element(driver, loginbtn).click()

# iframe = driver.find_element_by_id('ifcontent')

# 切换到小网页
i = ('id', 'ifcontent')
iframe = find_element(driver, i)
driver.switch_to_frame(iframe)

time.sleep(5)
useraccount = ('xpath', '/html/body/div[1]/div/div[1]/ul/li[1]/div/p[2]')
a = find_element(driver, useraccount, 5)
print(a.text)

driver.switch_to_default_content() # 切换到默认的网页作用域