# 这个文件下面存放所有关于首页模块的接口的相关的测试用例
import pytest
import requests

def test_01_lbt(): # 引入方法 普通方法命名 test_运行顺序数字_方法名字
    # 这里面就写requests的代码
    url = "http://118.24.105.78:2333/get_title_img"
    res = requests.get(url) #(url=url可以省略写法为url,但是如果有参数要写明，如header=xxx)
    assert res.status_code == 200
    assert res.json()["status"] == 200
# 直接在终端输入pytest运行就可以了

    # 数据库验证

def test_02_tjjc(): #首页的第二个接口
    url = "http://118.24.105.78:2333/getcoures?pagenum=1"
    res = requests.get(url)
    assert res.status_code == 200
    assert res.json()["status"] == 200

    # 数据库验证