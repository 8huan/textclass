
# 1. 保存信息到文件
def save_file_iid(file_path="./conf/iid.txt", iid=""):
    with open(file_path, "w") as f: # 新建一个文件保存在conf中
        f.writelines(iid)

# 2. 读取txt文件
def read_file_iid(file_path="./conf/iid.txt"):
    with open(file_path, "r") as f: # r表示只读模式
        iid = f.read()
        
    return iid # 返回数据