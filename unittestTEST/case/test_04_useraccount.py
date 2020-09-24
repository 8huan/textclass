import unittest,time
from selenium import webdriver
from utils.seleniumtools import find_element
from utils.filetools import read_file, save_file

class TestCaseAdminUserCount(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='driver\chromedriver.exe')
        # cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.driver.get("http://118.24.255.132:9090/shopxo/admin.php")
        # 通过url来判断用户是否登录
        curl = "http://118.24.255.132:9090/shopxo/admin.php?s=/admin/logininfo.html"
        
        # 没有登录就自动登录，登录就不用管
        if self.driver.current_url == curl: # 如果没有登录，就调用登录方法
            username = ('name','username')
            password = ('name','login_pwd')
            loginbtn = ('xpath','/html/body/div[1]/div/div[2]/div/form/div/div[3]/button')

            find_element(self.driver,username).send_keys("admin")
            find_element(self.driver,password).send_keys("shopxo")
            find_element(self.driver,loginbtn).click()
        
        # 切换作用域（进入到首页之后，切换小网页）
        eframe = find_element(self.driver,('id','ifcontent'))
        self.driver.switch_to_frame(eframe)

        time.sleep(3) # 因为元素会变化

    def test_01_user_count(self):
        usercount = ('xpath','/html/body/div[1]/div/div[1]/ul/li[1]/div/p[2]')
        assert find_element(self.driver,usercount).text == "2"

    def test_02_order_count(self):
        ordercount = ('xpath','/html/body/div[1]/div/div[1]/ul/li[2]/div/p[2]')
        assert find_element(self.driver,ordercount).text == "1"

        