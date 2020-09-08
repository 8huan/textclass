
# 对于加法而言，可以定义一个方法，来做加法
def add(s1,s2):   
    # s1 s2都表示参数，参数=方法里面的变量
    sum = s1 + s2 
    return sum #返回sum的值
# a = 1 + 1
# b = 2 + 2
a = add(1,1) # 这是一个赋值语句
b = add(2,2)
print(a)
print(b)

#练习：自定义一个减法方法/函数，要求去调用这个方法，显示返回值
def cut(s1,s2):
    t = s1 -s2
    return t
a = cut (3,1)
b = cut (0,2)
print(a)
print(b)

# 定义方法是有几个参数就写几个参数，没有参数就不写
# 参数为空：
def log():
    print("我是一个log方法")

log()

#参数有默认值
def add(s1=100,s2=100):   
    # s1=100,s2=100都表示默认值
    sum = s1 + s2 
    return sum #返回sum的值
# a = 1 + 1
# b = 2 + 2
a = add(1,1) # 这是一个赋值语句
b = add(2,2)
c = add()
d = add(s2=200,s1=1) #传参的时候给指定参数的值
print(a)
print(b)
print(c)
print(d)
# a、b传了参数所以输出的结果是1+1/2+2的和 
# c没有传参数，所以输出的结果是默认值（100+100）的和 
# d表示200+1的和

# 定义一个登录方法
def login(username,password):
    a = 1
    t_user = [{"username":"墩子", "password":"123456"}, {"username":"小玉", "password":"123456"}]
    for i in t_user:
        print('这是第{}次运行, i的值是{}'.format(a, i))
        if u == i.get("username") and p == i.get("password"):
            print("登陆成功！")
            break  # 终止循环
        else:
            if len(t_user) == a:
                print("登陆失败")
        a = a + 1

u = input("请输入账号:")
p = input("请输入密码:")
login(u,p)