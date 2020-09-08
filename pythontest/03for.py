# 遍历：把每个东西都取出来
# 遍历数组
# 有个list[80,60,59,29,99]，来判断成绩是否合格，请把不合格的成绩打印出来。
cj = [80,60,59,29,99]
for i in cj:          # 用i表示cj里的每一个元素，for i in cj表示从cj里把每个元素取出。for里的in表示取值，if的in表示判断是否存在。
    if i < 60:        
        print("不合格的成绩为：{}".format(i))  #.format()表示把括号内的值放到前面的{}里
                      # 字符串是拼接，数字是相加

# 把合格的成绩添加到一个list中，不合格的添加到另一个list中。
cj = [80,60,59,29,99]
buhege = []
hegede = []
for i in cj:
    if i < 60:
        buhege.append(i) #buhege.append()表示把()里的值添加到前面的buhege的[]中
    else:
        hegede.append(i)
print(hegede)
print(buhege)

# 遍历元组：与遍历数组的方式是一样的

# 遍历字典
zhanghao = {"username":"小星","chengji":88} 
for i in zhanghao:     # i表示每个键值对的key值：username 和 chengji
    print(i)           # 输出的结果是username 和 chengji
    print(zhanghao[i]) # 与print(zhanghao.get(i))表示的含义相同，都是取key所对应的value；
                       # print(zhanghao.get(i))表示第一次循环zhanghao.get("username")，第二次循环zhanghao.get("chengji")；
                       # zhanghao[i]表示第一次循环zhanghao["username"]，第二次循环zhanghao["chengji"]；
                       # 表示取zhanghao里的username的value和取zhanghao里的chengji的value。
# 依次循环

# keys表示输出打印所有的key值；
for i in zhanghao.keys():
    print(i)
# values表示输出打印所有的value值：
for j in zhanghao.values():
    print(j)
# items表示输出循环键值对
for i,j in zhanghao.items():
    print(i) # 输出key
    print(j) # 输出value
    print(i,j) # 输出“一对” 

# 遍历字符串
aa = "你好，欢迎你！"
for i in aa:
    print(i)

# range() 是一个序列生成器 [0,1,2,3,4,5,6,7,8,9] 一般用来生成下标
for i in range(10):
    print(i)

a = ["路人甲","路人乙","路人丙","路人丁","路人戊","路人己","路人庚","路人辛","路人壬","路人"]
# for i in range(10): range(10)表示会生成0-10的下标，0的下标表示路人甲...10的下标表示路人
                      # 即range对应了a的元素个数，可以直接用range(len(a))来表示
for i in range(len(a)):
    print(i)          # 表示输出每个元素的下标
    print(a[i])       # 表示输出每个下标所对应的元素

# 进阶的内容
a = [[1,2,3],[4,5,6]] #二维数组

for i in a:
    print(i) # a此时显示的结果是[1,2,3] [4,5,6]
# 如果要循环二维数组中值
for i in a:
    for j in i: # 表示循环i所代表的数组中的值
        print(j)

b = [{"username":"第一个","password":"123456"},{"username":"第二个","password":"123456"}]

for i in b:
    print(i) #表示循环每个字典
# 循环字典内的key/value
for i in b :
    for j in i:
        print(j)    #表示取key值
        print(i[j]) #表示取value值


# 用for循环实现用户登陆: t_user是数据的表
t_user = [{"username":"墩子", "password":"123456"}, {"username":"小玉", "password":"123456"}]
u = input("请输入账号:")
p = input("请输入密码:")
a = 1
for i in t_user:
    print('这是第{}次运行, i的值是{}'.format(a, i))
    if u == i.get("username") and p == i.get("password"):
        print("登陆成功！")
        break  # 终止循环
    else:
        # 最后一次运行都还没有这个账号：再来打印登录失败
        # 怎么来判断是最后一次运行 》 最后一次运行
        if len(t_user) == a:
            print("登陆失败")
    a = a + 1

# 什么算法，怎么实现出来
# a = ["胡", "张", "王", "夏", "张", "李"]，请用python写出a列表中重复元素的下标和值

# 排序：
# a = [1,2,3,4,555,333,22211,-1], 请使用python对a列表进行从小到大的排序


