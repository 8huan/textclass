# 练习：
# https://www.taobao.com/
# 到淘宝搜索框输入海澜之家，并且点击搜索按钮

from selenium import webdriver

driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.maximize_window() #让浏览器最大化
driver.get("https://www.taobao.com/")
driver.find_element_by_id('q').send_keys("海澜之家")
driver.find_element_by_xpath('//*[@id="J_TSearchForm"]/div[1]/button').click()

print(driver.title) # 获取网页标题
print(driver.current_url)
driver.quit() # 退出测试


