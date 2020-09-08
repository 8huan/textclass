# python 连接数据库查询
import pymysql # 要想用pymysql，就必须要导入它

def query(sql):
    # 固定的方法
    db = pymysql.connect(host='192.144.148.91', user='ljtest', password="Lj123456+", db='ljtestdb')
    # host是要连接的数据库的IP地址 
    # user数据库账号 password密码 db表示要打开的数据库名字

    # 获取查询窗口：游标
    cur = db.cursor()
    # 执行sql语句
    cur.execute(sql)
    # 获取所有的结果
    res = cur.fetchall()
    # 关闭数据库连接
    db.close()
    # 返回结果
    return res

if __name__ == "__main__":
    a = query("select * from t_user where id = 1111")
    print(a)


