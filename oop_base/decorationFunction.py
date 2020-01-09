#!/usr/bin/python
# coding=UTF-8

import os
import functools

BASE = os.getcwd()

# 装饰函数, 打印日志
def log(func):
    @functools.wraps(func)   # 此操作能保持 log 修饰的函数的 __name__ 不会改变
    def wrapper(*args, **kw):
        print("call %s():" % func.__name__)
        return func(*args, **kw)
    return wrapper


@log
def test():
    print("print time function")
    print(test.__name__)

@log
def test2():
    print("test2")
    print(test2.__name__)


def main():
    test()
    print("------------------------------")
    test2()


if __name__ == '__main__':
    main()