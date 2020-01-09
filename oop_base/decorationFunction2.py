#!/usr/bin/python
# coding=UTF-8

import functools
import os

BASE = os.getcwd()

# 带参数的装饰函数
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print("%s, call %s" % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log("execute test1")
def test1():
    print("test1 print time")
    print(test1.__name__)


@log("execute test2")
def test2():
    print("test2 print time.")
    print(test2.__name__)


def main():
    test1()
    print("--------------------")
    test2()


if __name__ == '__main__':
    main()