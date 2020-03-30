#!/usr/bin/python
# encoding=utf-8

import functools


# python偏函数是通过functools模块被用户调用
# 偏函数是将所要承载的函数作为partial()函数的第一个参数，源函数的各个参数
# 一次作为partial()函数后续的参数，除非使用关键字参数

# 偏函数的应用
def mod(n, m):
    return n % m


if __name__ == '__main__':
    # 偏函数mod_by_100 相当于是 提前给mod函数的参数n赋值为100
    mod_by_100 = functools.partial(mod, 100)
    print(mod(100, 7))
    print(mod_by_100(7))
