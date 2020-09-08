# 导入requests 是固定的导入方法
import requests
from dbtools import query

# python调接口

# 1.构造请求
u = "http://118.24.105.78:2333/get_title_img"
r = requests.get(u)
print(res.text)

# 2.判断结果：断言实现判断http状态码和结果码
assert r.status_code == 200 # 判断接口是不是正常的
assert r.json()["status"] == 200 # 判断结果吗是否正确

# 3.数据库校验：本次要查询的所有轮播图id是否存在
data = r.json()["data"]
for i in data:
    # 每次循环之后，都去查询一下数据库
    sql = "select * from t_title_img where id = {}".format(i["id"])
    res = query(sql)
    print(res)
    # assert len(res) != 0

