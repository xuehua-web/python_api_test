# -*- coding:utf-8 _*-
#Author:xuehua
#Email:564033627@qq.com
#Date:2019/9/5
# Function：投资用例的执行
import unittest
from ddt import ddt, data, unpack
from common import do_excel, do_mysql
from common import http_request
from  common import contants, context, logger

logger = logger.get_logger(__name__)


@ddt
class InvestTest(unittest.TestCase):
    """
        投资测试思路：1.管理员登录；2.管理员加标；3,管理员审核；4.投资人登录；5.投资人正常投资；6.投资数据用例的设计
        """
    do_excel = do_excel.DoExcel(contants.case_file, "invest")
    cases = do_excel.get_cases()

    @classmethod
    def setUpClass(cls):
        logger.debug("准备测试前置")
        cls.http_request = http_request.HttpRequest2()
        cls.do_mysql = do_mysql.DoMySql()

    @data(*cases)
    def test_invest(self, case):
        logger.debug("开始测试:{}".format(case.title))
        # case.data中带有参数，需要替换一下
        case.data = context.replace(case.data)
        # print(case.data)
        if case.check_sql is not None:
            sql2 = eval(case.check_sql)["sql2"]  # 获得SQL语句
            # print(sql2)
            count = self.do_mysql.fetch_one(sql2)
            print(count)
            before = count["COUNT(*)"]  # 加标之前，用户的添标数量
            # print("before:", before)
        resp = self.http_request.request(case.method, case.url, case.data)
        actual_code = resp.json()['code']
        try:
            self.assertEqual(str(case.exspected), actual_code)  # 判断预期结果和实际结果是否相等
            # 断言出错，就不执行后面的语句
            self.do_excel.write_result(case.case_id + 1, resp.text, "PASS")
            # 判断加标成功后，查询数据库，找到loan_id
            if resp.json()['msg'] == '加标成功' and case.check_sql is not None:
                # 判断1：数据库中增加一条数据
                sql2 = eval(case.check_sql)["sql2"]
                after = self.do_mysql.fetch_one(sql2)["COUNT(*)"]
                self.assertEqual(before + 1, after)  # 判断加标后的数量是否+1
                # 取值：loan_id
                sql1 = eval(case.check_sql)["sql1"]
                loan_id = self.do_mysql.fetch_one(sql1)["id"]
                setattr(context.Context, "loan_id", str(loan_id))  # 反射
        except AssertionError as e:
            self.do_excel.write_result(case.case_id + 1, resp.text, "Fail")
            logger.error("报错了:{}".format(e))
            raise e  # 抛出异常,但不影响后面用例的执行
            # print(e)#有异常后，打印出来，但是用例还是显示绿色对勾
        else:
            logger.debug("结束测试:{}".format(case.title))

    @classmethod
    def tearDownClass(cls):
        logger.debug("测试后置处理")
        cls.http_request.close()
        cls.do_mysql.close()