# 登录

import unittest
from selenium import webdriver
from utils.seleniumtools import find_element

class TestCaseAdminLogin(unittest.TestCase):

    def test_01_login_failed(self):
        driver = webdriver.Chrome(executable_path='./driver/chromedriver')
        driver.get("http://118.24.255.132:9090/shopxo/admin.php")
        
        username = ("name", "username")
        password = ("name", "login_pwd")
        loginbtn = ('xpath', '/html/body/div[1]/div/div[2]/div/form/div/div[3]/button')
        find_element(driver, username).send_keys("admin")
        find_element(driver, password).send_keys("shopxo")
        find_element(driver, loginbtn).click()

        index = ('xpath', '//*[@id="admin-offcanvas"]/div/ul/li[1]/a/span[2]')
        assert find_element(driver, index).text == "首页"