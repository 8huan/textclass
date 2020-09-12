# 这里的代码就是登录相关的case

import pytest
import requests

# 跨文件夹的导入方式
import os, sys
sys.path.append(os.getcwd())
from utils.dbtools import query #导入query方法 一定是sys在前，from在后
from utils.filetools import save_file 
from utils.exceltools import read_excel #调用read_excel方法 用于读取数据

def test_01_login_success():
    # 登录成功的测试用例
    data_res = read_excel("data/测谈网测试用例.xlsx","登录") # 调取read_excel的方法，读取数据，data/测谈网测试用例.xlsx为文件的相对路径，登录为页面的名字
    url = data_res[0][2] # 读取上行取出来的值中的用例名称
    data = eval(data_res[0][4]) # 读取出来的值中的参数，读出来的数据是字符串，所以用eval强转为字典
    header = eval(data_res[0][5]) #读取出来的值中的请求头，用eval强转为字典

    res = requests.post(url=url,json=data,headers=header)
    # print(res.text) #可以打印查询到内容
    assert res.status_code == 200
    assert res.json()["status"] == 200

# pytest -s可以打印断言结果 
# 测试用例（方法的结果）：. 成功 F：失败了（代码报错，断言失败)

    # 数据库校验 
    # 直接调用query方法
    sql = "select * from t_user where username = '{}'".format(data["username"])
    assert len(query(sql)) != 0

    # 保存最后一次登录的token
    # 先取出token token传参
    token = res.json()["data"]["token"]
    save_file(token=token)

def test_02_login_failed_by_error_username():
    # 4位数账号登录失败的用例 ，注意：取的值是第二条用例
    
    data_res = read_excel("data/测谈网测试用例.xlsx", "登录")
    url = data_res[1][2] 
    data = eval(data_res[1][4])
    header = eval(data_res[1][5])
    # 失败的用例不需要取数据库查询，因为失败的数据不会写入数据库
    res = requests.post(url=url, json=data, headers=header)
    assert res.status_code == 200
    assert res.json()["status"] == int(data_res[1][6])

def test_03_login_success_by_5username():
    """
        登陆成功的测试用例
    """
    data_res = read_excel("data/测谈网测试用例.xlsx", "登录")
    url = data_res[2][2]
    data = eval(data_res[2][4])
    header = eval(data_res[2][5])

    res = requests.post(url=url, json=data, headers=header)
    assert res.status_code == 200
    assert res.json()["status"] == int(data_res[2][6])