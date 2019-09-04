# -*- coding:utf-8 _*-
# Author:xuehua
# Email:564033627@qq.com
# Date:2019/9/3
# Function： 测试用例的执行及测试报告的生成
import unittest
from common import HTMLTestRunnerNew
from common import contants

discover = unittest.defaultTestLoader.discover(contants.case_dir, "test_*.py")

with open(contants.report_dir + '/report.html', 'wb+') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                              title="PYTHON15 API TEST REPORT",
                                              description="q前程贷API",
                                              tester="xuehua")
    runner.run(discover)
