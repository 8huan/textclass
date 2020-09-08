
# if 条件语句
a = 18
if a > 18:         #冒号是英文状态下的
    print("成年")
else:
    print("未成年")

# >/>= 

# </<=

# ==等于 一个等于号=是赋值，两个等号是判断语句
b = 123
c = 1234
if b == c:
    print("b=c")
else:
    print("b不等于c")

#!= 不等于
b = 123
c = 123
if b != c:
    print("b=c")
else:
    print("b不等于c")

# 字符串条件 in ，判断某个字符是否在另一个字符串中
t = "12345a"
y = "a"
if y in t:
    print("y属于t")
else:
    print("不存在")

#练习1：1．	请输入你的年龄，判断是否成年？
b = input("请输入你的年龄：")
a = float(b)
if a >= 18:
    print("成年啦！")
else:
    print("没成年噢。")

#练习2：请输入一个字符串，判断字符串的长度是否大于6个字，
#       如果大于就输出内容合格，否则就显示不合格
b = input("请输入内容：")
c = len(b)
if c>6:
    print("内容合格")
else:
    print("不合格")

# 多条件 :输入长度为3，名字为小星星，同时满足（and)
name = input("请输入你的名字：")
if name == "小星星" and len(name) ==3:
    print("是你啦")
else:
    print("很遗憾")

#输入长度为3或者名字为小星星（or)
name = input("请输入你的名字：")
if name == "小星星" or len(name) ==3:
    print("是你啦")
else:
    print("很遗憾")

name = input("请输入你的名字：")
if len(name) ==3:
    if name == "小星星":
        print("是你啦")
    else:
        print("很遗憾噢")
else:
    print("很遗憾")

#练习：输入一个账号，输入一个密码，要求判断账号的长度大于5位，并且小于8位。
# 如果输入账号为张三12345，密码为123456就可以登陆成功，否则就登录失败。
c = input("请输入账号：")
a = len(c)
b = input("请输入密码：")
if a > 5 and a < 8:
    if c == "张三12345":
        if b == "123456":
            print("登录成功")
        else:
            print("密码错误")
    else:
        print("账号错误！")
else:
    print("账号错误！！")

# while
# 有个list[80,60,59,29,99]，
# 来判断成绩是否合格，请把不合格的成绩打印出来。
a = 0 #用来表示cj的下标
cj = [80,60,59,29,99]
while a < 5: #5可以用len(cj)来代替，就可以随着数组的增加而改变个数
    if cj[a] < 60:
        print("不合格的成绩为：{}".format(cj[a]))
        #。format()表示把括号内的值放到前面的{}里
        # 字符串是拼接，数字是相加
    a = a + 1

#练习
# 红绿灯有60秒，
# 红灯35s，绿灯20s，黄灯5s，
# 红灯打印35次，绿灯打印20次，黄灯打印5次
a = 1
while a <= 60:
    if a > 0 and a <36:
        print("红灯")
    if a >= 36 and a < 56:
        print("绿灯")
    if a >= 56 and a <= 60:
        print("黄灯")
    a = a + 1




