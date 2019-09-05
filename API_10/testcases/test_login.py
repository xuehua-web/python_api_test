# -*- coding:utf-8 _*-
#Author:xuehua
#Email:564033627@qq.com
#Date:2019/9/5
# Function： 登录测试用例的执行，使用 unitest,ddt
import unittest
from ddt import ddt, data, unpack
from common import do_excel
from common import http_request
from  common import contants, logger

logger = logger.get_logger(__name__)


@ddt
class LoginTest(unittest.TestCase):
    do_excel = do_excel.DoExcel(contants.case_file, "login")
    cases = do_excel.get_cases()

    @classmethod
    def setUpClass(cls):
        logger.debug("准备测试前置")
        cls.http_request = http_request.HttpRequest2()

    @data(*cases)
    def test_login(self, case):
        # 日志输出
        logger.debug("开始测试:{}".format(case.title))
        # print(case.title)
        resp = self.http_request.request(case.method, case.url, case.data)
        actual = resp.text
        try:
            self.assertEqual(case.exspected, actual)  # 判断预期结果和实际结果是否相等
            # 断言出错，就不执行后面的语句
            self.do_excel.write_result(case.case_id + 1, actual, "PASS")
        except AssertionError as e:
            self.do_excel.write_result(case.case_id + 1, actual, "Fail")
            logger.error("报错了:{0}".format(e))
            raise e  # 抛出异常,但不影响后面用例的执行
        else:
            logger.debug("结束测试:{0}".format(case.title))
            # print("测试用例:[{}],执行成功！".format(case.title))

    @classmethod
    def tearDownClass(cls):
        logger.debug("测试后置处理")
        cls.http_request.close()