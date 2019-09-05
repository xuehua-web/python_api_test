# -*- coding:utf-8 _*-
#Author:xuehua
#Email:564033627@qq.com
#Date:2019/9/5
#Function：
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # API_3
print(base_dir)

case_file = os.path.join(base_dir, 'data', 'cases.xlsx')
# print(case_file)

sheet_name = 'login'
# api:pre_url
global_file = os.path.join(base_dir, "config", "global.cfg")
# print(global_file)

online_file = os.path.join(base_dir, "config", "online.cfg")
# print(online_file)

test_file = os.path.join(base_dir, "config", "test.cfg")
# print(test_file)

# 连接数据库
mysql_file = os.path.join(base_dir, "config", "mysql.cfg")
# print(mysql_file)

# global_file = os.path.join(base_dir,"config\global.cfg")#这样的写法也能正确找到文件
# print(global_file)
log_dir = os.path.join(base_dir, "log")
# print(log_dir)
report_dir = os.path.join(base_dir, "reports")
# print(report_dir)
case_dir = os.path.join(base_dir, "testcases")
# print(case_dir)
