# -*- coding:utf-8 _*-
#Author:xuehua
#Email:564033627@qq.com
#Date:2019/9/5
# Function： 操作数据库
import pymysql
from common import config
from common import contants


class DoMySql:
    """
    完成与MySql数据库的一个交互
    """

    def __init__(self):
        read_config = config.ReadConfig(contants.mysql_file)
        host = read_config.get("mysql", "host")
        user = read_config.get("mysql", "user")
        password = read_config.get("mysql", "password")
        port = read_config.getInt("mysql", "port")
        # 1.连接数据库
        self.mysql = pymysql.connect(host=host, user=user, password=password, port=port)
        # 2.新建一个查询页面
        # self.cursor = self.mysql.cursor()
        self.cursor = self.mysql.cursor(pymysql.cursors.DictCursor)  # 单个结果集返回字典，对个结果集返回的是列表，每个元素是字典格式

    def fetch_one(self, sql):
        # 3.执行SQL语句
        self.cursor.execute(sql)
        self.mysql.commit()  # commit,提交当前事务，及时充值生效
        # 4.获取查询结果集中的最近一条数据，返回的是一个元组
        return self.cursor.fetchone()

    def fetch_all(self, sql):
        self.cursor.execute(sql)
        self.mysql.commit()
        # 获取全部结果集，返回的是元组套元组
        return self.cursor.fetchall()

    def close(self):
        # 5.关闭查询页面
        self.cursor.close()
        # 6.关闭数据库连接
        self.mysql.close()