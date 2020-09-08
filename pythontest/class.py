# 类
class Person():
    # 成员变量：类中的变量，在整个类中都能使用
    name = "小明"
    age = 18
    sex = "男"

    # 定义一个方法
    # def walk(self):  # 无论有没有参数都要写self
    # print("人靠双脚走路")
    def walk(self,sth):   # 写参数之前必须写一个self，self是固定的
        print("人靠双脚走路{}".format(sth)) # 相当于sth是第一个参数
# 这样就定义好了一个类：
# Person这个类有name、age、sex这些成员变量，还有walk这个方法。
    
    def run(self):
        p.hobby = "唱歌"  # 初始化成员变量 如果这个变量存在就是替换，不存在就是新建
        print("这个类的名字是{}".format(self.name)) # 表示可以到成员方法中来引用name这个变量

    def test(self):
        self.run()
# 调用类：实例化类 p叫做实例化对象,也可把p称为类的把柄
p = Person()
print(p.name) #调用成员变量 打印的结果为小明
# p.walk() #调用成员方法 直接调用不用管self与普通定义的方法不同，这里的self一定不要传
p.eat("跑动") # 这里的'跑动'表示sth的参数 打印的结果为人靠双脚走路跑动

p.run()
p.hobby()
p.test()
