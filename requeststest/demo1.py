# 导入requests 是固定的导入方法
import requests
from dbtools import query # 调用dbtools.py中的query查询方法

# python调接口

# 1.构造请求
u = "http://118.24.105.78:2333/get_title_img" # 用一个变量存地址，地址是字符串类型的
# get请求
r = requests.get(u) # requests.get(u)表示向u这个接口发送了一个get请求 r表示所有的响应信息
print(r.text) # r.text:打印接口的返回值，所返回的结果是字符串

# 2.判断结果：断言实现判断http状态码和结果码
# asser 条件语句
assert r.status_code == 200 # 判断接口是不是正常的 print(r.status_code)可以获取状态码 状态码是固定的
assert r.json()["status"] == 200 # 判断结果码是否正确 r.json()的目的是把结果转换成字典 结果码是开发自己定的

# 3.数据库校验：本次要查询的所有轮播图id是否存在
data = r.json()["data"]
for i in data:
    # print（i["id"] 获取所有的id 
    # 每次循环之后，都去查询一下数据库
    sql = "select * from t_title_img where id = {}".format(i["id"])
    res = query(sql)
    print(res)
    assert len(res) != 0 #判断res长度是否为0，()这样表示长度为0，((),(),,)表示长度不为0

