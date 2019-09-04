# -*- coding:utf-8 _*-
# Author:xuehua
# Email:564033627@qq.com
# Date:2019/9/2
# Function： 学习数据操作
# 安装数据库 pip install pymysql
import pymysql

# 1.连接数据库
host = "test.lemonban.com"
user = "test"
password = "test"
port = 3306
mysql = pymysql.connect(host=host, user=user, password=password, port=port)
# 2.新建查询页面,游标cursor
cursor = mysql.cursor(pymysql.cursors.DictCursor)
# 3.编写sql语句，并执行
# sql="select MAX(MobilePhone) from future.member"
# sql = "SELECT * from future.member LIMIT 10"
# sql="select count(*) from future.member"
# sql='select * from future.loan where memberid=1197 order by Id DESC LIMIT 1'
# sql="select * from future.member where mobilephone = '15810447878'"
sql="select id from future.loan where memberid = 1008 order by id desc limit 1"
cursor.execute(sql)  # 执行查询
# 4.查询结果
result = cursor.fetchone()  # 获取查询结果集中最近的一条数据返回
# results = cursor.fetchall()  # 获取全部结果集
print(type(result["id"]))
# 5.关闭查询
cursor.close()
# 6.关闭数据库连接
mysql.close()
