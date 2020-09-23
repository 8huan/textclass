"""
    整个工具的入口：都是固定的
"""

import unittest # 首先导入unittest
from utils.HTMLTestRunner import HTMLTestRunner # 导入HTMLTestRunner这个类

# 1.自动查找所有的测试用例
testcase = unittest.defaultTestLoader.discover('case', 'test_*.py') # "case"表示相对路径，

# 2.使用htmltestrunner工具来帮我们自动运行所有的case和生成测试报告
title = "这是unittest的第一次测试报告" # 文件的title
descr = "这是unittest的测试报告" # 描述
filepath = "./report/report.html" # 保存的相对路径

# 文件的读写
with open(filepath, "wb") as f: # w表示文件存在就替换 不存在就新建，b表示以二进制的方式输入（是固定的）；把文件的把柄给f
    runner = HTMLTestRunner(stream=f, title=title, description=descr)
    runner.run(testcase) # 调用run方法，运行所有的测试用例