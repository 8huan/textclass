# 这个文件下面存放所有的首页相关的测试用例
import pytest
import requests

def test_01_lbt():
    # 这里面就写requests的代码
    url = "http://118.24.105.78:2333/get_title_img"
    res = requests.get(url)
    assert res.status_code == 200
    assert res.json()["status"] == 200

    # 数据库验证

def test_02_tjjc():
    url = "http://118.24.105.78:2333/getcoures?pagenum=1"
    res = requests.get(url)
    assert res.status_code == 200
    assert res.json()["status"] == 200

    # 数据库验证