# -*- coding:utf-8 _*-
""" 
@author:mongo
@time: 2018/12/17 
@email:3126972006@qq.com
@function： 
"""

# 1）、搜索引擎中会对用户输入的数据进行处理，第一步就是词法分析，
# 分离字符串中的数字、中文、拼音、符号。
# 比如这个字符串：
# 我的是名字是ths,今年18岁。
# 语法分析后得到结果如下：
# 数字：18
# 中文：我的名字是 今年 岁
# 拼音：ths
# 符号：，。
# 请编写程序实现该词法分析功能。
# s = '我的是名字是ths,今年18岁'
# input()

import re
import string

p = '\d'

print(string.digits)
print(string.ascii_letters)
print(string.punctuation)
print('a'.isspace())


def find_by(s):
    pattern = {"数字": "\d", "拼音": "[a-zA-Z]", "汉字": "[\u4e00-\u9fff]"}
    for k, v in pattern.items():
        ss = re.findall(v, s)
        print(k + ": " + "".join(ss))
        s = re.sub(v, '', s)

    print("符号:{0}".format(s))
    # if re.search('\d', s):
    #     digit = re.findall('\d', s)
    #     s = re.sub('\d', '', s)
    #
    # if re.search('[a-zA-Z]', s):
    #     letter = re.findall('[a-zA-Z]', s)
    #     s = re.sub('[a-zA-Z]', '', s)


def find(s):
    digit = []
    letter = []
    punctuation = []
    chinese = []
    for ss in s:
        if ss in string.digits:  # 判断是否是数字
            digit.append(ss)
        elif ss in string.ascii_letters:  # 判断是否是字母
            letter.append(ss)
        elif ss in string.punctuation or ss.isspace():  # 判断是否是符号
            punctuation.append(ss)
        else:
            chinese.append(ss)
    print("数字：{0}".format(''.join(digit)))
    print("拼音：{0}".format(''.join(letter)))
    print("符号：{0}".format(''.join(punctuation)))
    print("中文：{0}".format(''.join(chinese)))


if __name__ == '__main__':
    inp = input('请输入~~~')
    # find(inp)
    find_by(inp)
