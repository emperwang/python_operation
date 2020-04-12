#!/bin/bin/python
# -*- coding:utf-8 -*-

import sys


def getComParn():
    """
    通过sys模块获取命令行参数
    """
    if len(sys.argv) <= 1:
        print('usage: {} parm1 parm2 .'.format(sys.argv[0]))
        return;
    for i in sys.argv:
        print("{}th param is :{}".format(i, sys.argv[1]))


if __name__ == '__main__':
    getComParn()
