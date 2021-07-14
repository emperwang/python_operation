#!/usr/bin/python
# encoding: utf-8

from multiprocessing import Process, Queue
import time
# 多进程间的通信

def p_put(q, *arg):
    q.put(arg)
    print("has put %s" % arg)

def p_get(q, *arg):
    print("%s wait to get ...." % arg)
    print(q.get())
    print("%s got it " % arg)


if __name__ == '__main__':
    q = Queue()
    p1 = Process(target=p_put, args=(q, "p1", ))
    p2 = Process(target=p_get, args=(q, "p2", ))
    p1.start()
    time.sleep(2)
    p2.start()
