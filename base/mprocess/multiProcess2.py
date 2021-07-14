#!/usr/bin/python
# -*- coding: utf-8 -*

import multiprocessing
import os

def show_info(title):
    print(title)
    print("module name: ", __name__)
    # print("parent process :", os.getppid())   # windows 无此属性
    print("process id :", os.getpid())
    print("\r\n")


def f(name):
    show_info('function f')
    print("name = ", name)


if __name__ == '__main__':
    show_info("main process line")
    p = multiprocessing.Process(target=f, args=("child process", ))
    p.start()
    #p.join()