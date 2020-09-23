# 首页

# 导入unittest
import unittest
from selenium import webdriver # 导入webdriver
from utils.seleniumtools import find_element # 导入动态查找的方法

# unittest的测试用例是以类来进行管理
class TestCaseIndex(unittest.TestCase):

    # 成员方法
    def test_01_baobao(self):
        # selenium的code
        driver = webdriver.Chrome(executable_path='driver/chromedriver')
        driver.maximize_window()
        driver.get("http://118.24.255.132:9090/shopxo/")
        baobao = ('xpath', '//*[@id="floor1"]/div[2]/div[2]/div[1]/div/div/a') # 动态查找的方式
        bb = find_element(driver, baobao)
        assert bb.text == "MARNI Trunk 女士 中号拼色十字纹小牛皮 斜挎风琴包"


    def test_02_baobao2(self):
        driver = webdriver.Chrome(executable_path='driver/chromedriver')
        driver.maximize_window()
        driver.get("http://118.24.255.132:9090/shopxo/")
        baobao = ('xpath', '//*[@id="floor1"]/div[2]/div[2]/div[2]/div/div/a')
        bb = find_element(driver, baobao)
        assert bb.text == "纽芝兰包包女士2018新款潮百搭韩版时尚单肩斜挎包少女小挎包链条"