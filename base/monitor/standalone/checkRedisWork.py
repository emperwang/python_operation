#!/usr/bin/python
# coding=utf-8
import os
import sys
import argparse
import time

BASE = os.getcwd()

def __parseParam():
    parse = argparse.ArgumentParser(description='redis cluster check')
    ip = os.popen("cat /opt/redis-5.0.0/6379/redis.conf | grep bind | grep -v '^#'  | awk '{print $2}'").readlines()
    print(ip[1])
    parse.add_argument('-c', '--cmd', action='store', dest='cmd', default='/opt/redis-5.0.0/6379/redis-cli', required=False, help='cmd to exec.')
    parse.add_argument('-i', '--host', action='store', dest='host', default=ip[1], required=False, help='host to check.')
    parse.add_argument('-p', '--port', action='store', dest='port', default=6379, required=False, help='redis cluster port')
    return parse.parse_args()


def __checkworking(parms):
    key = time.strftime('%Y%M%d%H%m%S', time.localtime())
    gg = "get "+key
    ss = "source /etc/profile; {}  --cluster call {}:{}  set {} {}  EX 5000  2>/dev/null".format(parms['cmd'], parms['host'], parms['port'],
                                                                                    key, key)
    gg = "source /etc/profile; {}  --cluster call {}:{}  get {}  2>/dev/null".format(parms['cmd'], parms['host'], parms['port'],key)
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