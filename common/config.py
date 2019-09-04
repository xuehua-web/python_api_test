# -*- coding:utf-8 _*-
# Author:xuehua
# Email:564033627@qq.com
# Date:2019/9/2
# Function： 配置文件的读取
import configparser
from common import contants


class ReadConfig:
    """
    完成配置文件的读取
    """

    def __init__(self, file_name):
        self.config = configparser.ConfigParser()
        if file_name == contants.global_file:
            self.config.read(file_name,encoding="utf-8")  # 读取文件，先读取global文件
            switch = self.config.getboolean("switch", "on")
            # print(switch)
            if switch:  # 开关打开的时候，使用online的配置
                self.config.read(contants.online_file)
            else:  # 开关关闭的时候，使用test的配置
                self.config.read(contants.test_file,encoding="utf-8")
        elif file_name == contants.mysql_file:
            self.config.read(file_name)
        else:
            print("该文件没有写处理的方法！")

    def get(self, section, option):
        return self.config.get(section, option)  # 配置文件用get方法，读取的是字符串

    def getInt(self, section, option):  # 读取一个整数
        return self.config.getint(section, option)


# read = ReadConfig()
