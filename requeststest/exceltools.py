# 读取excel

import xlrd

def read_excel(excel_path, sheet_name, skip_first=True):
    results = []
    datas = xlrd.open_workbook(excel_path) # datas就是在打开表格
    table = datas.sheet_by_name(sheet_name) # 表示读取具体哪个表
    if skip_first == True:
        start_row = 1
    else:
        start_row = 0

    # 循环读取每一行的数据
    for row in range(start_row, table.nrows):
        results.append(table.row_values(row))

    return results

print(read_excel("data.xlsx", "Sheet1"))
