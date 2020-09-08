# # 作业1：
# # b = [{"username":"郭子", "password":"123456"}, {"username":"小玉", "password":"123456"},]
# # 输入一个账号和密码，如果b中存在这个账号，那就注册失败，如果b中没有这个账号，就到b里面去添加账号和密码

# a = 1
# b = [{"username":"郭子", "password":"123456"}, {"username":"小玉", "password":"123456"}]
# u = input("请输入账号:")
# p = input("请输入密码:")
# for i in b:
#     if u == i.get("username") and p == i.get("password"):
#         print("注册失败！")
#         break  
#     else:
#         if len(b) == a:
#             print("注册成功")
#             c = {"username":u,"password":p}
#             b.append(c)
#             break
#     print(b)
#     a = a + 1

# #作业2：
# # 请使用python查询商品表t_goods表里面的商品名为 iPhone的价格，
# #  并且判断价格如果价格大于5488，则显示买不起，否则显示买买买。
# # 作业的数据库信息：

# # 118.24.105.78
# # root
# # 1qaz!QAZ123***123
# # # 数据库：ljtestdb

# import pymysql # 要想用pymysql，就必须要导入它

# def query(sql):
#     # 固定的方法
#     db = pymysql.connect(host='118.24.105.78', user='root', password="1qaz!QAZ123***123", db='ljtestdb')
#     # host是要连接的数据库的IP地址 
#     # user数据库账号 password密码 db表示要打开的数据库名字

#     # 获取查询窗口：游标
#     cur = db.cursor()
#     # 执行sql语句
#     cur.execute(sql)
#     # 获取所有的结果
#     res = cur.fetchall()
#     # 关闭数据库连接
#     db.close()
#     # 返回结果
#     return res

# if __name__ == "__main__":
#     a = query("select * from t_goods where goods = 'iPhone12'")
#     print(a)

 
#     # good = input ("请输入商品名：")
#     sql = "select * from t_goods where goods = 'iPhone12'"
    
#     res = query(sql)
#     if int(res[0][-1]) > 5488:
#         print("买不起")
#     else:
#         print("买买买")

# 简单：
# 1. 计算1000之内，偶数的个数  (x % n ==0)

# 1.1
a = 1
b = []
c = []
while a > 0 and a <= 1000:
    if a % 2 == 0:
        b.append(a)
        # print(b)
    else:
        c.append(a)
        # print(c)
    a = a + 1
print(len(b))

# 1.2
a = 1
b = []
while a > 0 and a <= 1000:
    if a % 2 == 0:
        b.append(a)
    a = a + 1
print(len(b))

# 2. 将一个数组逆序输出 [22,33,1,4,5,6,7]

# 2.1
d = [22,33,1,4,5,6,7]
d.sort(reverse=True)
a = 0
for i in d:
    if a < 7:
        print(i)

# 2.2 用冒泡排序法：两个for嵌套

# 3.输入一个整数，判断该整数的因数有哪些？ 4  （2）10 （2/5）

# 3.1
g = int(input("请输入一个1000以内的正整数："))
h = g 
j = []
k = []
if g < 1000 and g > 0:
    while h > 0 and h <= g:
        if g % h == 0:
            if h != 1 and h != g:
                j.append(h)
        else:
            k.append(h)
        h = h - 1
    print("它的因数除了1和{}之外，还有{}。(注：若[]无内容，则说明只有1和{}两个因数。）".format(g,j,g))
else:
    print("请输入1000以内的正整数！")

# 3.2

# 4.把这个字典中用户名包含“美”字的名字，复制到新的列表中 {"username":"乔美丽"，"username2":"刘美丽", "username3"：“郭美丽”：“username3”："username4:"郭然然""}  
# > 结果为 ["乔美丽", "刘美丽", "郭美丽"]

# 4.1
e = {"username":"乔美丽","username2":"刘美丽","username3":"郭美丽","username4":"郭然然"}  
f = []
for i in e.values():
    if "美" in i:
        f.append(i)
print(f)
