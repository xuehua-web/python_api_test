# -*- coding:utf-8 _*-
#Author:xuehua
#Email:564033627@qq.com
#Date:2019/9/5
# Function： 注册用例的执行
import unittest
from ddt import ddt, data, unpack
from common import do_excel
from common import http_request
from  common import contants
from common import do_mysql, logger

logger = logger.get_logger(__name__)


@ddt
class RegisterTest(unittest.TestCase):
    do_excel = do_excel.DoExcel(contants.case_file, "register")
    cases = do_excel.get_cases()
    do_mysql = do_mysql.DoMySql()

    @classmethod
    def setUpClass(cls):
        logger.debug("准备测试前置")
        cls.http_request = http_request.HttpRequest2()

    @data(*cases)
    def test_register(self, case):
        logger.debug("开始测试:{0}".format(case.title))
        # 加入数据库的查询
        # 如何将数据库中查询到的数据，更新到测试用例中呢？测试数据做参数化，作为标识
        if case.data.find("register_mobile") > -1:
            sql = 'select max(MobilePhone) phone from future.member'
            result = self.do_mysql.fetch_one(sql)
            max_phone = result["phone"]  # 获取最大的手机号，str
            max_phone = int(max_phone) + 1
            # 使用字符串的replace方法，指定替换
            case.data = case.data.replace("register_mobile", str(max_phone))
            # print(case.data)

        resp = self.http_request.request(case.method, case.url, case.data)
        actual = resp.text
        try:
            self.assertEqual(case.exspected, actual)  # 判断预期结果和实际结果是否相等
            # 断言出错，就不执行后面的语句
            self.do_excel.write_result(case.case_id + 1, actual, "PASS")
        except AssertionError as e:
            self.do_excel.write_result(case.case_id + 1, actual, "Fail")
            logger.error('\033[0;31m报错了:{}\033[0m'.format(e))#颜色不起作用
            raise e  # 抛出异常,但不影响后面用例的执行
        else:
            logger.debug("结束测试:{}".format(case.title))

    @classmethod
    def tearDownClass(cls):
        logger.debug("测试后置处理")
        cls.http_request.close()
        cls.do_mysql.close()