#!/usr/bin/python
# -*- coding: utf-8 -*
import multiprocessing


def f(conn):
    conn.send("send by child")
    print('child recv :', conn.recv())
    conn.close()

"""
父子进程通过pipe进行通信
"""
if __name__ == "__main__":
    parent_conn, child_conn = multiprocessing.Pipe()
    p = multiprocessing.Process(target=f, args=(child_conn, ))
    p.start()
    print("parent recv :", parent_conn.recv())
    parent_conn.send("send by parent")
