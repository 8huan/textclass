# 数据分离示例：数据存放在excel中，通过xlrd读取出来
# 导入方法
import requests
from dbtools import query
from exceltools import read_excel # 导入read_excel方法

res = read_excel("data.xlsx", "Sheet1")
print(res[0])          #表示打印第一行的数据
url = res[0][2]        # 表示接口地址
data = eval(res[0][5]) # 表示取headers eval表示强行把数据类型转换成字典
h = eval(res[0][4])    # 请求头

res = requests.post(url=url, json=data, headers=h)
assert res.status_code == 200
assert res.json()["status"] == 200

sql = "select * from t_user where username='liuyun1'"
assert len(query(sql)) != 0
print("接口测试成功！")

token = res.json()["data"]["token"]

url1 = "http://118.24.105.78:2333/inspirer/new"
header1 = {"Content-Type":"application/json", "token":token}
data1 = {"content":"这是来自星星的数据", "ximg":"dsfsdf.jpg"}
res1 = requests.post(url=url1, json=data1, headers=header1)
print(res1.text)