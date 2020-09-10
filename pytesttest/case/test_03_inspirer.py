
import pytest
import requests

# 跨文件夹的导入方式
import os, sys
sys.path.append(os.getcwd())
from utils.dbtools import query  # 一定是sys在前from在后
from utils.filetools import save_file, read_file

def test_01_fblg():
    url = "http://118.24.105.78:2333/inspirer/new"
    data = {"content":"内容","ximg":"dsfsdf.jpg"}
    header = {"Content-Type":"application/json", "token":read_file()}

    res = requests.post(url=url, json=data, headers=header)
    print(res.text)
    assert res.status_code == 200
    assert res.json()["status"] == 200
    # 数据库查询
    id = res.json()["data"]["inspirerid"]
    sql = "select * from t_inspirer where id={}".format(id)
    assert len(query(sql)) == 1