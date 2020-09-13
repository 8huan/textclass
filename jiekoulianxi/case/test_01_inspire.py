import pymysql
import pytest
import requests

# 跨文件夹导入
import os, sys
sys.path.append(os.getcwd())
from utils.dbtools import query
from utils.filetools import save_file,read_file
from utils.exceltools import read_excel
from utils.filetools_iid import save_file_iid,read_file_iid


# (1) 获取灵感接口
def test_01_inspire_0101_success():
    data_res = read_excel("data/测谈网测试用例.xlsx","灵感相关")

    url = data_res[0][4]

    res = requests.get(url)
    print(res.text)

    assert res.status_code == 200
    assert res.json()["status"] == 200

def test_01_inspire_0102_success():
    data_res = read_excel("data/测谈网测试用例.xlsx","灵感相关")

    url = data_res[1][4]

    res = requests.get(url)
    print(res.text)

    assert res.status_code == 200
    assert res.json()["status"] == 200

def test_01_inspire_0103_success():
    data_res = read_excel("data/测谈网测试用例.xlsx","灵感相关")

    url = data_res[2][4]

    res = requests.get(url)
    print(res.text)

    assert res.status_code == 200
    assert res.json()["status"] == 401

def test_01_inspire_0104_success():
    data_res = read_excel("data/测谈网测试用例.xlsx","灵感相关")

    url = data_res[3][4]

    res = requests.get(url)
    print(res.text)

    assert res.status_code == 200
    assert res.json()["status"] == 401
    
def test_01_inspire_0105_success():
    data_res = read_excel("data/测谈网测试用例.xlsx","灵感相关")

    url = data_res[4][4]

    res = requests.get(url)
    print(res.text)

    assert res.status_code == 200
    assert res.json()["status"] == 401

def test_01_inspire_0106_success():
    data_res = read_excel("data/测谈网测试用例.xlsx","灵感相关")

    url = data_res[5][4]

    res = requests.get(url)
    print(res.text)

    assert res.status_code == 200
    assert res.json()["status"] == 401

def test_01_inspire_0107_success():
    data_res = read_excel("data/测谈网测试用例.xlsx","灵感相关")

    url = data_res[6][4]

    res = requests.get(url)
    print(res.text)

    assert res.status_code == 200
    assert res.json()["status"] == 401

def test_01_inspire_0108_success():
    data_res = read_excel("data/测谈网测试用例.xlsx","灵感相关")

    url = data_res[7][4]

    res = requests.get(url)
    print(res.text)

    assert res.status_code == 200
    assert res.json()["status"] == 401

# (2) 获取灵感详情
def test_01_inspire_0201_success():
    data_res = read_excel("data/测谈网测试用例.xlsx","灵感相关")

    url = data_res[8][4]

    res = requests.get(url)
    print(res.text)

    assert res.status_code == 200
    assert res.json()["status"] == 200

def test_01_inspire_0202_success():
    data_res = read_excel("data/测谈网测试用例.xlsx","灵感相关")

    url = data_res[9][4]

    res = requests.get(url)
    print(res.text)

    assert res.status_code == 200
    assert res.json()["status"] == 200

def test_01_inspire_0203_success():
    data_res = read_excel("data/测谈网测试用例.xlsx","灵感相关")

    url = data_res[10][4]

    res = requests.get(url)
    print(res.text)

    assert res.status_code == 200
    assert res.json()["status"] == 401

def test_01_inspire_0204_success():
    data_res = read_excel("data/测谈网测试用例.xlsx","灵感相关")

    url = data_res[11][4]

    res = requests.get(url)
    print(res.text)

    assert res.status_code == 200
    assert res.json()["status"] == 401
    
def test_01_inspire_0205_success():
    data_res = read_excel("data/测谈网测试用例.xlsx","灵感相关")

    url = data_res[12][4]

    res = requests.get(url)
    print(res.text)

    assert res.status_code == 200
    assert res.json()["status"] == 401

def test_01_inspire_0206_success():
    data_res = read_excel("data/测谈网测试用例.xlsx","灵感相关")

    url = data_res[13][4]

    res = requests.get(url)
    print(res.text)

    assert res.status_code == 200
    assert res.json()["status"] == 401

def test_01_inspire_0207_success():
    data_res = read_excel("data/测谈网测试用例.xlsx","灵感相关")

    url = data_res[14][4]

    res = requests.get(url)
    print(res.text)

    assert res.status_code == 200
    assert res.json()["status"] == 401


# (3) 获取用户灵感列表

def test_01_inspire_0301_success():
    data_res = read_excel("data/测谈网测试用例.xlsx","灵感相关")

    url = data_res[15][4]

    res = requests.get(url)
    print(res.text)

    assert res.status_code == 200
    assert res.json()["status"] == 401

def test_01_inspire_0302_success():
    data_res = read_excel("data/测谈网测试用例.xlsx","灵感相关")

    url = data_res[16][4]

    res = requests.get(url)
    print(res.text)

    assert res.status_code == 200
    assert res.json()["status"] == 200

def test_01_inspire_0303_success():
    data_res = read_excel("data/测谈网测试用例.xlsx","灵感相关")

    url = data_res[17][4]

    res = requests.get(url)
    print(res.text)

    assert res.status_code == 200
    assert res.json()["status"] == 401

def test_01_inspire_0304_success():
    data_res = read_excel("data/测谈网测试用例.xlsx","灵感相关")

    url = data_res[18][4]

    res = requests.get(url)
    print(res.text)

    assert res.status_code == 200
    assert res.json()["status"] == 200

def test_01_inspire_0305_success():
    data_res = read_excel("data/测谈网测试用例.xlsx","灵感相关")

    url = data_res[19][4]

    res = requests.get(url)
    print(res.text)

    assert res.status_code == 200
    assert res.json()["status"] == 401

def test_01_inspire_0306_success():
    data_res = read_excel("data/测谈网测试用例.xlsx","灵感相关")

    url = data_res[20][4]

    res = requests.get(url)
    print(res.text)

    assert res.status_code == 200
    assert res.json()["status"] == 401

def test_01_inspire_0307_success():
    data_res = read_excel("data/测谈网测试用例.xlsx","灵感相关")

    url = data_res[21][4]

    res = requests.get(url)
    print(res.text)

    assert res.status_code == 200
    assert res.json()["status"] == 401

def test_01_inspire_0308_success():
    data_res = read_excel("data/测谈网测试用例.xlsx","灵感相关")

    url = data_res[22][4]

    res = requests.get(url)
    print(res.text)

    assert res.status_code == 200
    assert res.json()["status"] == 401

def test_01_inspire_0309_success():
    data_res = read_excel("data/测谈网测试用例.xlsx","灵感相关")

    url = data_res[23][4]

    res = requests.get(url)
    print(res.text)

    assert res.status_code == 200
    assert res.json()["status"] == 401

def test_01_inspire_0310_success():
    data_res = read_excel("data/测谈网测试用例.xlsx","灵感相关")

    url = data_res[24][4]

    res = requests.get(url)
    print(res.text)

    assert res.status_code == 200
    assert res.json()["status"] == 200


def test_01_inspire_0501_success():
    data_res = read_excel("data/测谈网测试用例.xlsx","灵感相关")

    url = data_res[32][4]
    data = eval(data_res[32][6])
    header = eval(data_res[32][7])

    res = requests.post(url=url,json=data,headers=header)
    print(res.text)
    assert res.status_code == 200
    assert res.json()["status"] == 200

    id = res.json()["data"]["inspirerid"]
    sql = "select * from t_inspirer where id={}".format(id)
    assert len(query(sql)) == 1  

    iid = str(res.json()["data"]["inspirerid"])
    save_file_iid(iid=iid)

def test_01_inspire_0502_success():
    data_res = read_excel("data/测谈网测试用例.xlsx","灵感相关")

    url = data_res[33][4]
    data = eval(data_res[33][6])
    header = eval(data_res[33][7])

    res = requests.post(url=url,json=data,headers=header)
    print(res.text)
    assert res.status_code == 200
    assert res.json()["status"] == 401

def test_01_inspire_0503_success():
    data_res = read_excel("data/测谈网测试用例.xlsx","灵感相关")

    url = data_res[34][4]
    data = eval(data_res[34][6])
    header = eval(data_res[34][7])

    res = requests.post(url=url,json=data,headers=header)
    print(res.text)
    assert res.status_code == 200
    assert res.json()["status"] == 200

def test_01_inspire_0504_success():
    data_res = read_excel("data/测谈网测试用例.xlsx","灵感相关")

    url = data_res[35][4]
    data = eval(data_res[35][6])
    header = eval(data_res[35][7])

    res = requests.post(url=url,json=data,headers=header)
    print(res.text)
    assert res.status_code == 200
    assert res.json()["status"] == 401

# (4) 用户删除灵感

def test_01_inspire_0401_success():
    data_res = read_excel("data/测谈网测试用例.xlsx","灵感相关")

    url = data_res[25][4]
    data = eval(data_res[25][6])
    header = eval(data_res[25][7])

    res = requests.post(url=url,json=data,headers=header)
    print(res.text)
    assert res.status_code == 200
    assert res.json()["status"] == 200


def test_01_inspire_0402_success():
    data_res = read_excel("data/测谈网测试用例.xlsx","灵感相关")

    url = data_res[26][4]
    data = eval(data_res[26][6])
    header = eval(data_res[26][7])

    res = requests.post(url=url,json=data,headers=header)
    print(res.text)
    assert res.status_code == 200
    assert res.json()["status"] == 401


def test_01_inspire_0403_success():
    data_res = read_excel("data/测谈网测试用例.xlsx","灵感相关")

    url = data_res[27][4]
    data = eval(data_res[27][6])
    header = eval(data_res[27][7])

    res = requests.post(url=url,json=data,headers=header)
    print(res.text)
    assert res.status_code == 200
    assert res.json()["status"] == 401


def test_01_inspire_0404_success():
    data_res = read_excel("data/测谈网测试用例.xlsx","灵感相关")

    url = data_res[28][4]
    data = eval(data_res[28][6])
    header = eval(data_res[28][7])

    res = requests.post(url=url,json=data,headers=header)
    print(res.text)
    assert res.status_code == 200
    assert res.json()["status"] == 401


def test_01_inspire_0405_success():
    data_res = read_excel("data/测谈网测试用例.xlsx","灵感相关")

    url = data_res[29][4]
    data = eval(data_res[29][6])
    header = eval(data_res[29][7])

    res = requests.post(url=url,json=data,headers=header)
    print(res.text)
    assert res.status_code == 200
    assert res.json()["status"] == 401


def test_01_inspire_0406_success():
    data_res = read_excel("data/测谈网测试用例.xlsx","灵感相关")

    url = data_res[30][4]
    data = eval(data_res[30][6])
    header = eval(data_res[30][7])

    res = requests.post(url=url,json=data,headers=header)
    print(res.text)
    assert res.status_code == 200
    assert res.json()["status"] == 401


def test_01_inspire_0407_success():
    data_res = read_excel("data/测谈网测试用例.xlsx","灵感相关")

    url = data_res[31][4]
    data = eval(data_res[31][6])
    header = eval(data_res[31][7])

    res = requests.post(url=url,json=data,headers=header)
    print(res.text)
    assert res.status_code == 200
    assert res.json()["status"] == 401


