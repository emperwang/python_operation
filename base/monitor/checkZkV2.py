#!/usr/bin/python
# coding=utf-8
import argparse
import os
import sys

BASE = os.getcwd()

def __paramget():
    parser = argparse.ArgumentParser(description='zookeeper check script.')
    parser.add_argument('-c', '--cmd', action='store', dest='cmd', required=False, help='cmd to exec.')
    parser.add_argument('-i', '--host', action='store', dest='host', required=True, help='hosts to check.(ip,ip2)')
    parser.add_argument('-u', '--user', action='store', dest='user', required=True, default='root', help='user to login')
    return  parser.parse_args()


def __getcmdpath():
    cmdpath = os.popen("find /opt -name 'zkServer.sh'")
    rr = cmdpath.readlines()
    if len(rr) == 0:
        print("cann't find cmd zkServer.sh")
        sys.exit(1)
    elif len(rr) > 1:
        print("find cmd more than one.")
        sys.exit(1)
    else:
        print("cmd", rr[0])
        return rr[0].replace("\n", "")


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
    if parser.cmd is not None and "zkServer" in parser.cmd:
        cmds = dict(cmd=parser.cmd, hosts=parser.host, user=parser.user)
    else:
        cpath = __getcmdpath()
        cmds = dict(cmd=cpath, hosts=parser.host, user=parser.user)
    print(cmds)
    numhosts = 0
    succhost = 0
    if "," in cmds['hosts']:
        for h in cmds['hosts'].split(","):
            numhosts += 1
            if check(h, cmds['user'], cmds['cmd']):
                succhost += 1
    else:
        if check(cmds['hosts'], cmds['user'], cmds['cmd']):
            succhost += 1
    if succhost > numhosts/2:
        print("zk cluster running")
    else:
        print("zk cluster error.")
        sys.exit(1)

# python checkZk.py -i 10.163.249.146,10.163.249.147,10.163.249.148 -u root -c /opt/software/zookeeper-3.4.14/bin/zkServer.sh
#  2>/dev/null

if __name__ == '__main__':
    main()