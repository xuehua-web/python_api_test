# -*- coding:utf-8 _*-
#Author:xuehua
#Email:564033627@qq.com
#Date:2019/9/5
# Function： 日志收集
import logging
from common import contants


def get_logger(name):
    # 1.新建日志收集器
    logger = logging.getLogger(name)
    logger.setLevel("DEBUG")
    # 2.设置日志输出格式
    fmt = "%(asctime)s -  %(name)s - %(levelname)s - %(message)s - [%(filename)s:%(lineno)d ]"
    formatter = logging.Formatter(fmt)
    # 3.新建输出渠道到控制台
    console_handler = logging.StreamHandler()
    console_handler.setLevel("DEBUG")
    console_handler.setFormatter(formatter)
    # 4.新建输出渠道到指定文件
    file_handler = logging.FileHandler(contants.log_dir + '\case.log', encoding="utf-8")
    file_handler.setLevel("DEBUG")
    file_handler.setFormatter(formatter)
    # 5.配合关系
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    return logger
if __name__ == '__main__':
    logger = get_logger('case')
    logger.info('测试开始啦')
    logger.error('测试报错')
    logger.debug('测试数据')
    logger.info('测试结束')