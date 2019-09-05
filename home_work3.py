# -*- coding:utf-8 _*-
""" 
@author:mongo
@time: 2018/12/17 
@email:3126972006@qq.com
@function： 
"""


# 3）传入一个Json串，返回一个字典，字典只取出Json最底层的数据，
# 中间如果有字符串也要进行处理，请以下面的数据为例，请用递归方法实现
# Json：{"a":"aa","b":['{"c":"cc","d":"dd"}',{"f":{"e":"ee"}}]}
# 输出：
# Dic:{'a':'aa','c':'cc','d':'dd','e':'ee'}

def str_2_dict(j):  # j是一个Json串
    new = {}  # 只存放底层的数据
    if type(j) == str:  # 如果是字符串
        j = eval(j)

    if type(j) == list:  # 判断如果是列表
        for item in j:
            d = str_2_dict(item)
            new.update(d)

    if type(j) == dict:  # 判断如果是字典
        for k, v in j.items():
            if type(v) == list or type(v) == dict:
                d = str_2_dict(v)
                new.update(d)
            else:
                new[k] = v

    return new  # 返回一个字典


if __name__ == '__main__':
    j = '{"a":"aa","b":[\'{"c":"cc","d":"dd"}\',{"f":{"e":"ee"}}]}'
    f = '{"e":123,"ee":{"eee":"diceng"}}'
    new = str_2_dict(f)
    print(new)
