# 登录保存token
import pymysql
import pytest
import requests

# 跨文件夹导入
import os, sys
sys.path.append(os.getcwd())
from utils.dbtools import query
from utils.filetools import save_file

def test_00_login_success():
    url = "http://118.24.105.78:2333/login"
    data = {"username":"tanghh","password":"a12345678"}
    h = {"Content-Type":"application/json"}

    res = requests.post(url=url,json=data,headers=h)
    print(res.text)
    assert res.status_code == 200
    assert res.json()["status"] == 200

    sql = "select * from t_user where username = 'tanghh'"
    assert len(query(sql)) !=0

    token = res.json()["data"]["token"]
    save_file(token=token)
