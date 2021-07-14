#!/bin/env python
# coding:UTF-8

import subprocess
import os
import argparse
import sys

BASE = os.getcwd()

def __argparse():
    parse = argparse.ArgumentParser("check leader")
    parse.add_argument("-c", "--cmd", action='store', dest='cmd', default='/opt/kafka-2.11/bin/kafka-topics.sh', required=False, help='kafka-topics.sh path')
    parse.add_argument('-p', '--port', action='store', dest='port', default=9092, required=False, help='kafka listening port')
    parse.add_argument('-i', '--host', action='store', dest='ip', required=True, help='kafka listening ip')
    return parse.parse_args()

def _checkrunning():
    cmd = "service kafka status"
    st = "service kafka start"
    rr = os.popen(cmd)
    res = rr.readline()
    # print("check running:{}".format(res))
    if "no" in res:
        os.popen(st)
        print(1)
        sys.exit(1)


def main():
    pms = __argparse()
    cmds = dict(cmd=pms.cmd, port=pms.port, ip=pms.ip)
    _checkrunning()
    fcmd = "{}  --bootstrap-server {}:{} --describe --topic __consumer_offsets".format(cmds['cmd'], cmds['ip'], cmds['port'])
    #rr = os.popen(fcmd)
    #print(rr, type(rr) )
    #result = rr.readlines()
    rr = subprocess.Popen(fcmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)
    err = rr.stderr.readline()
    if (len(err) > 0):
        print(1)
        sys.exit(1)
    result = rr.stdout.readlines()
    losts = 0
    if len(result) > 0:
        for lin in result[1:]:
            if int(lin.split("\t")[3].split(":")[1]) == -1:
                losts += 1
    else:
        print(1)
    if losts > 0:
        print(1)
        sys.exit(1)
    print(0)


if __name__ == '__main__':
    main()