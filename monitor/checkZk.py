#!/usr/bin/python
# coding=utf-8
import argparse
import os

BASE = os.getcwd()

def __paramget():
    parser = argparse.ArgumentParser(description='zookeeper check script.')
    parser.add_argument('-c', '--cmd', action='store', dest='cmd', required=True, help='cmd to exec.')
    parser.add_argument('-i', '--host', action='store', dest='host', required=True, help='hosts to check.(ip,ip2)')
    return  parser.parse_args()

def check(ip, usr, cmd):
    print("checking host:", ip)
    c = "ssh "+usr+"@"+ip+ "  'source /etc/profile;"+cmd+"  status'"
    result = os.popen(c)
    lines = result.readlines()
    resStr = str(lines)
    if "follower" in resStr or "leader" in resStr or "observer" in resStr:
        print(ip, resStr)
        return True

def main():
    parser = __paramget()
    cmds = dict(cmd=parser.cmd, hosts=parser.host)
    numhosts = 0
    succhost = 0
    if "," in cmds['hosts']:
        for h in cmds['hosts'].split(","):
            numhosts += 1
            if check(h, "root", cmds['cmd']):
                succhost += 1
    else:
        if check(cmds['hosts'], "root", cmds['cmd']):
            succhost += 1
    if succhost > numhosts/2 :
        print("zk cluster running")

# python checkZk.py -c /mnt/zookeeper-3.4.5-cdh5.12.0/bin/zkServer.sh  -i name1,node1,node2 2>/dev/null

if __name__ == '__main__':
    main()