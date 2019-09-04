# -*- coding:utf-8 _*-
# Author:xuehua
# Email:564033627@qq.com
# Date:2019/9/2
# Function：
import requests
from common import config
from common import contants
from common import logger

logger = logger.get_logger(__name__)


class HttpRequest:
    """
    单独的session，把上一个请求返回的cookie，指定传递到下一个请求的入参cookie中
    """

    def request(self, method, url, data=None, json=None, cookies=None):
        method = method.lower()  # 将字符串中的字母强制转换为小写
        # method = method.upper() # 将字符串中的字母强制转换为大写
        # 注意：从Excel中读取的是字符串或数字。表格中是数字的，读取出来的数据类型还是数字，其余数据类型，读取出来的都是字符串
        # request的get或post方法，传递的params、data要求是字典或元组列表
        if type(data) == str:
            data = eval(data)  # 返回数据本身的数据类型
        url = config.ReadConfig(contants.global_file).get('api', 'pre_url') + url  # url的拼接
        print(url)
        if method == 'get':
            resp = requests.get(url, params=data, cookies=cookies)
        elif method == 'post':
            if json:
                resp = requests.post(url, json=json, cookies=cookies)
            else:
                resp = requests.post(url, data=data, cookies=cookies)
        else:
            resp = None
            print("UN-support method")
        return resp


class HttpRequest2:
    """
    使用同一个session，自动传递cookie
    """

    def __init__(self):
        # 新建一个对话
        self.session = requests.sessions.session()

    def request(self, method, url, data=None, json=None):
        method = method.upper()
        if type(data) == str:
            data = eval(data)  # 返回数据本身的数据类型
        url = config.ReadConfig(contants.global_file).get('api', 'pre_url') + url  # url的拼接
        #日志的输出
        logger.debug("请求的方法:{}".format(method))
        logger.debug("请求的URL:{}".format(url))
        logger.debug("请求data:{}".format(data))

        if method == 'GET':
            resp = self.session.request(method, url, params=data)
        elif method == 'POST':
            if json:
                resp = self.session.request(method, url, json=json)
            else:
                resp = self.session.request(method, url, data=data)
        else:
            resp = None
            # print("UN-supported method")
            logger.error("UN-supported method")
        return resp

    def close(self):
        self.session.close()  # 关闭一个对话


if __name__ == '__main__':
    http_request2 = HttpRequest2()
    params = {"mobilephone": "15810447878", "pwd": "123456"}
    resp = http_request2.request('pOST', 'http://test.lemonban.com/futureloan/mvc/api/member/login', data=params)
    params = {"mobilephone": "15810447878", "amount": "1000"}
    resp2 = http_request2.request('POST', 'http://test.lemonban.com/futureloan/mvc/api/member/recharge', data=params)
    http_request2.close()
    print(resp2.status_code)
    print(resp2.text)
    print(resp.cookies)
    print(resp2.request._cookies)
