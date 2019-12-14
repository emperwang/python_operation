#!/usr/bin/python
# coding=utf-8
import argparse
import json
import os

BASE = os.getcwd()

def __paramget():
    parser = argparse.ArgumentParser(description='zookeeper check script.')
    parser.add_argument('-c', '--cmd', action='store', dest='cmd', required=True, help='cmd to exec.')
    parser.add_argument('-i', '--host', action='store', dest='host', required=True, help='hosts to check.(ip:port,ip2:port)')
    return  parser.parse_args()

def check(ip, usr, cmd):
    print("checking host:", ip)
    c = "ssh "+usr+"@"+ip+ "  'source /etc/profile;"+cmd+"  status'"
    result = os.popen(c)
    for i in result.readlines():
        print(i)

def main():
    parser = __paramget()
    cmds = dict(cmd=parser.cmd, hosts=parser.host)
    print(cmds)
    if "," in cmds['hosts']:
        for h in cmds['hosts'].split(","):
            check(h, "root", cmds['cmd'])
    else:
        print("host:", cmds['hosts'])
        check(cmds['hosts'], "root", cmds['cmd'])


if __name__ == '__main__':
    main()