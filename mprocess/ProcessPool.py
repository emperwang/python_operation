#!/usr/bin/python
# coding: utf-8

import multiprocessing
import time
import os

# 进程池的使用

def foo(n):
    time.sleep(1)
    print("In process", n, os.getpid())
    return n

def bar(*args):
    print(">> done", args, os.getpid())


if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=3)
    print("主进程 :", os.getpid())
    for i in range(10):
        # pool.apply(func=foo, args=(i, ))
        pool.apply_async(func=foo, args=(i, ), callback=bar)    # 异步调用，以及回调函数
    print("end")
    pool.close()
    pool.join()