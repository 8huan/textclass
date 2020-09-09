# import pandas as pd
# data = pd.read_excel('data.xlsx')
# print(data.values[0]) # 表示取第一行的数据

import pandas as pd
data = pd.read_excel('data.xlsx', sheet_name="sheet1") #打开文档
# print(data) #打印数据
data["编号"][data["编号"] == 100] = 1 # 如果编号=1，就把编号的值改为100
data.to_excel("data.xlsx") # 保存修改后的数据


