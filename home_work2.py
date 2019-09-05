# -*- coding:utf-8 _*-
""" 
@author:mongo
@time: 2018/12/17 
@email:3126972006@qq.com
@function： 
"""


# 2）编写程序实现:
# n=5，输出：
#   *
#  ***
# *****
#  ***
#   *
# n=6，输出：
#   *
#  ***
# *****
# *****
#  ***
#   *
# n为任意大于1的正整数。

# 行数 = 输入的数
# 星号的个数
# 星号+空格 = 输入的数
# 前面空格个数= 后面空格个数，（输入的数-星号个数）// 2 = 单边空格个数

def print_img(n):
    # 前半部分
    for i in range(1, n + 1, 2):
        img = ' ' * ((n - i) // 2) + "*" * i
        print(img)

    if n % 2 == 0:  # 偶数行
        s = n - 1
    else:
        s = n - 2  # 奇数行

    # 后半部分
    for i in range(s, 0, -2):
        img = ' ' * ((n - i) // 2) + "*" * i
        print(img)


print_img(7)
