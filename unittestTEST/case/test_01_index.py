# # 首页

# # 导入unittest
# import unittest
# from selenium import webdriver # 导入webdriver
# from utils.seleniumtools import find_element # 导入动态查找的方法

# # unittest的测试用例是以类来进行管理
# class TestCaseIndex(unittest.TestCase):
    
#     # 在类开始执行的时候，执行一次
#     # 只打开一次浏览器，节约了测试的时间
#     @classmethod # 表示下面的方法是类方法
#     def setUpClass(cls): # cls 的作用等同于  self
#                          # setUpClass ：在整个类运行的时候最先运行一次，执行下面的测试用例前先执行一次
#         cls.driver = webdriver.Chrome(executable_path='driver/chromedriver')
#         cls.driver.maximize_window()

#     # 在类结束的时候，执行一次
#     @classmethod
#     def tearDownClass(cls):
#         cls.driver.quit()
#     # setUpClass和tearDownClass都是继承自unittest.TestCase的一个类

#     def setUp(self): # 放前置条件
#         self.driver.get("http://118.24.255.132:9090/shopxo/") # 表示刷新浏览器

#     def tearDown(self): # 放后置条件
#         print("我是teardown方法") # 这个内容可以随意填写

#     # 下面写单独的代码就可以了
#     def test_01_baobao(self):
#         self.driver.get("http://118.24.255.132:9090/shopxo/")
#         baobao = ('xpath', '//*[@id="floor1"]/div[2]/div[2]/div[1]/div/div/a') # 动态查找的方式
#         bb = find_element(self.driver, baobao)
#         assert bb.text == "MARNI Trunk 女士 中号拼色十字纹小牛皮 斜挎风琴包"


#     def test_02_baobao2(self):
#         self.driver.get("http://118.24.255.132:9090/shopxo/")
#         baobao = ('xpath', '//*[@id="floor1"]/div[2]/div[2]/div[2]/div/div/a')
#         bb = find_element(self.driver, baobao)
#         assert bb.text == "纽芝兰包包女士2018新款潮百搭韩版时尚单肩斜挎包少女小挎包链条"