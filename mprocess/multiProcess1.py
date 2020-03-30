#!/usr/bin/python
# -*- coding: utf-8 -*

import multiprocessing
import time


def process_run(n):
    time.sleep(1)
    print("prcessing :", n)

# 注意这里，因为windows不能调用fork来进行进程的创建， 所有在创建进程时，必须要在 __name__=='__main__' 语句后面进行
if __name__ == '__main__':
    #p = multiprocessing.Pool(100)
    for i in range(10):
        p = multiprocessing.Process(target=process_run, args=(i,))
        p.start()
        p.join()

