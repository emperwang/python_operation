#!/usr/bin/python
# coding=utf-8
import os
import argparse
import sys

BASE = os.getcwd()

def __argparse():
    parse = argparse.ArgumentParser("check leader")
    parse.add_argument("-c", "--cmd", action='store', dest='cmd', required=True, help='kafka-topics.sh path')
    parse.add_argument('-p', '--port', action='store', dest='port', default=9092, required=False, help='kafka listening port')
    parse.add_argument('-i', '--host', action='store', dest='ip', required=True, help='kafka listening ip')
    return parse.parse_args()


def main():
    pms = __argparse()
    cmds = dict(cmd=pms.cmd, port=pms.port, ip=pms.ip)
    fcmd = "{}  --bootstrap-server {}:{} --describe --topic __consumer_offsets".format(cmds['cmd'], cmds['ip'], cmds['port'])
    print("final cmd:", fcmd)
    rr = os.popen(fcmd)
    result = rr.readlines()
    losts = 0
    if len(result) > 0:
        for lin in result[1:]:
            print("analyse line:{}, lead:{}".format(lin, lin.split("\t")[3].split(":")[1]))
            if int(lin.split("\t")[3].split(":")[1]) == -1:
                losts += 1
    else:
        print("error")
        print(1)
    if losts > 0:
        print(1)
        sys.exit(1)
    print(0)



if __name__ == '__main__':
    main()