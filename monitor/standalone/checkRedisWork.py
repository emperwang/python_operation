#!/usr/bin/python
# coding=utf-8
import os
import sys
import argparse
import time

BASE = os.getcwd()

def __parseParam():
    parse = argparse.ArgumentParser(description='redis cluster check')
    parse.add_argument('-c', '--cmd', action='store', dest='cmd', required=False, help='cmd to exec.')
    parse.add_argument('-i', '--host', action='store', dest='host', required=True, help='host to check.')
    parse.add_argument('-p', '--port', action='store', dest='port', required=True, help='redis cluster port')
    return parse.parse_args()


def __checkworking(parms):
    key = time.strftime('%Y%M%d%H%m%S', time.localtime())
    gg = "get "+key
    ss = "source /etc/profile; {}  --cluster call {}:{}  set {} {}  EX 5000".format(parms['cmd'], parms['host'], parms['port'],
                                                                                    key, key)
    gg = "source /etc/profile; {}  --cluster call {}:{}  get {}".format(parms['cmd'], parms['host'], parms['port'],key)
    print("key:", key)
    os.popen(ss)
    res = os.popen(gg).readlines()
    for rr in res:
        if key in rr:
            print(0)
            return
    print(1)
    sys.exit(1)


def main():
    paser = __parseParam()
    parms = dict(cmd=paser.cmd, host=paser.host, port=paser.port)
    print(parms)
    __checkworking(parms)

if __name__ == '__main__':
    main()