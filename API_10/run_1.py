# -*- coding:utf-8 _*-
#Author:xuehua
#Email:564033627@qq.com
#Date:2019/9/5
# Function： 测试用例的执行,
import unittest
from testcases import test_add, test_recharge, test_register, test_invest, test_login
from common import contants, HTMLTestRunnerNew

suite = unittest.TestSuite()  # 创建一个测试套件TestSuite
# 通过模块名来加载用例
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromModule(test_invest))
suite.addTest(loader.loadTestsFromModule(test_login))
suite.addTest(loader.loadTestsFromModule(test_register))
suite.addTest(loader.loadTestsFromModule(test_recharge))
suite.addTest(loader.loadTestsFromModule(test_add))

with open(contants.report_dir + '/report.html', 'wb+') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                              verbosity=2,
                                              title="PYTHON15 API TEST REPORT",
                                              description="q前程贷API",
                                              tester="xuehua")
    runner.run(suite)