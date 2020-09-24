import unittest
from selenium import webdriver
from utils.seleniumtools import find_element
from po.AdminLoginPage import AdminLoginPage # 导入页面对象

# @unittest.skip("!23")
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
        
    def test_02_po_login(self):
        driver = webdriver.Chrome(executable_path='./driver/chromedriver')
        driver.get("http://118.24.255.132:9090/shopxo/admin.php")

        # 实例化类
        login_page = AdminLoginPage(driver)
        login_page.login("admin", "shopxo") 
        # 调用login方法 填入账号密码 ，就不用调用find_element方法
        # 现在调用的方法都是通过页面对象，这个类封装好的内容来完成的
        # 不用再写find_element，运行方法跟之前没有区别