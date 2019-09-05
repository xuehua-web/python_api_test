# -*- coding:utf-8 _*-
#Author:xuehua
#Email:564033627@qq.com
#Date:2019/9/5
# Function：充值用例的执行
import unittest
from ddt import ddt, data, unpack
from common import do_excel
from common import http_request
from  common import contants, logger

logger = logger.get_logger(__name__)


@ddt
class RechargeTest(unittest.TestCase):
    do_excel = do_excel.DoExcel(contants.case_file, "recharge")
    cases = do_excel.get_cases()

    @classmethod
    def setUpClass(cls):
        logger.debug("准备测试前置")
        cls.http_request = http_request.HttpRequest2()

    @data(*cases)
    def test_recharge(self, case):
        logger.debug("开始测试:{}".format(case.title))
        resp = self.http_request.request(case.method, case.url, case.data)
        actual_code = resp.json()['code']
        # print(type(actual_code))
        try:
            self.assertEqual(str(case.exspected), actual_code)  # 判断预期结果和实际结果是否相等
            # 断言出错，就不执行后面的语句
            self.do_excel.write_result(case.case_id + 1, resp.text, "PASS")
        except AssertionError as e:
            self.do_excel.write_result(case.case_id + 1, resp.text, "Fail")
            logger.error("报错了:{}".format(e))
            raise e  # 抛出异常,但不影响后面用例的执行
        else:
            logger.debug("结束测试:{}".format(case.title))

    @classmethod
    def tearDownClass(cls):
        logger.debug("测试后置处理")
        cls.http_request.close()
        # pass