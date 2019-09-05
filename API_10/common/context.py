# -*- coding:utf-8 _*-
#Author:xuehua
#Email:564033627@qq.com
#Date:2019/9/5
# Function： 正则表达式
import re
from common import contants, config
import configparser


class Context:
    loan_id = None


# 注意：这里写的是一个replace函数，参数没有self,
# 只有：位置参数、默认参数、动态参数(*args)->传参存储到元组、关键字参数(**kwargs)->传参后存储到字典

def replace(data):
    p = '#(.*?)#'  # 正则表达式
    while re.search(p, data):
        print(data)
        m = re.search(p, data)  # 从任意位置开始找，找第一个就返回Match object, 如果没有找None
        g = m.group(1)  # 拿到参数化的key
        # 根据key获取配置文件对应的值
        try:
            v = config.ReadConfig(contants.global_file).get("data", g)
            print(v)
        except configparser.NoOptionError as e:  # 如果配置文件找不到的话，就去Context里面找
            if hasattr(Context, g):  # 如果Context中有属性g，则执行下面代码
                v = getattr(Context, g)  # 获取类属性g的值
                print(v)
            else:
                print("找不到参数化的值!")
                raise e
        # 将对应的值替换到data中
        #注意：替换的时候，一定是字符串替换，不支持数字类型
        data = re.sub(p, v, data, count=1)
    return data