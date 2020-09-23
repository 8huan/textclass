# 导入selenium
from selenium import webdriver

# 1.打开浏览器，并获得浏览器的句柄，Chrome的C是大写的C!!!
drier = webdriver.Chrome(executable_path='chromedriver.exe')

# 2.打开网页
driver.get("https://www.baidu.com/")

# 3.操作元素
# (通过id定位元素)
# 首先通过find_element_by_id定位元素,调用sed_keys的方法可以对输入框进行输入，“selenium”表示输入的内容。
driver.find_element_by_id('kw').send_keys("selenium")

# (通过classname定位)
driver.find_element_by_class_name('s_ipt').send_keys("selenium")

# (通过name定位)
driver.find_element_by_name('wd').send_keys("selenium")

# (通过css_selector定位)
driver.find_element_by_css_selector('#kw').send_keys("selenium")

# (通过xpath定位)
# 先定位元素，再点击，click表示元素点击
driver.find_element_by_xpath('//*[@id="su"]').click() 

# (通过文本值定位超链接)直接点击“学术”，跳出新网页
driver.find_element_by_link_text("学术").click() 

# (通过部分文字定位超链接）
driver.find_element_by_partial_link_text("术").click() 

# (通过标签定位)--不推荐使用
# driver.find_element_by_tag_name()

# 能用id就用id来定位，不能id就用xpath

# 断言、等待
import time #导入time包
from selenium import webdriver

driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.maximize_window()  # 让浏览器最大化
driver.get("http://118.24.105.78:9000/shopxo/")

driver.find_element_by_id('search-input').send_keys("连衣裙")
driver.find_element_by_id('ai-topsearch').click()

# 等待：涉及到网页加载，或者元素加载的东西，都要用等待
time.sleep(10)
lianyiqun = driver.find_element_by_xpath('/html/body/div[4]/div/ul/li[1]/div/a/p')

# 断言
assert lianyiqun.text == "ZK星星绣花雪纺连衣裙中长款sukol裙少女心温柔超仙女chic裙子夏"