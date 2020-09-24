from utils.seleniumtools import find_element

class AdminLoginPage():

    # 1.把用到的元素封装到成员变量
    def __init__(self,driver): # 是一个构造方法/初始化方法，用来初始化成员变量
        self.driver = driver
        self.username = ('name', 'username')
        self.password = ('name', 'login_pwd')
        self.loginbtn = ('xpath', '/html/body/div[1]/div/div[2]/div/form/div/div[3]/button')
        self.url = "http://118.24.255.132:9090/shopxo/admin.php?s=/admin/logininfo.html"

    # 2.封装操作的步骤
    def login(self, u, p):
        find_element(self.driver, self.username).send_keys(u)
        find_element(self.driver, self.password).send_keys(p)
        find_element(self.driver, self.loginbtn).click()