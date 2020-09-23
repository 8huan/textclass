import time
from selenium import webdriver
from seleniumtools import find_element

driver = webdriver.Chrome(executable_path="./chromedriver")
driver.maximize_window()  # 让浏览器最大化
driver.get("http://118.24.105.78:9000/shopxo/")

print(driver.title)
baobao = ('xpath', '//*[@id="floor1"]/div[2]/div[2]/div[1]/div/div/a')
find_element(driver, baobao).click()

# 切换到新的window
print(driver.window_handles)  # window的句柄
driver.switch_to_window(driver.window_handles[-1]) # 作用域切换到新的窗口
print(driver.title)