# 这里的代码就是登录相关的case

import pytest
import requests

# 跨文件夹的导入方式
import os, sys
sys.path.append(os.getcwd())
from utils.dbtools import query #一定是sys在前，from在后
from utils.filetools import save_file

def test_01_login_success():
    # 登录成功的测试用例
    url = "http://118.24.105.78:2333/login"
    data = {"username":"tunan","password":"asd123456"}
    header = {"Content-Type":"application/json"}

    res = requests.post(url=url,json=data,headers=header)
    assert res.status_code == 200
    assert res.json()["status"] == 200

    # 数据库校验
    sql = "select * from t_user where username = '{}'".format(data["username"])
    assert len(query(sql)) != 0

    # 保存最后一次登录的token
    
