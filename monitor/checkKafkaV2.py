#!/usr/bin/python
# coding=utf-8

import os
import argparse
import sys

BASE = os.getcwd()
"""
 检测kafka，自动查找命令，找不到则返回false
"""
def __paramparaser():
    parser = argparse.ArgumentParser(description='kafka cluster check.')
    parser.add_argument("-c", "--cmd", action='store', dest='cmd', required=False, help='kafka-topics.sh cmd path')
    parser.add_argument('-p', '--port', dest='port', default=9092, type=int, help='kakfa port')
    parser.add_argument("-i", "--host", action='store', dest='host', required=True, help="host which kafka is running")
    parser.add_argument('-u', '--user', action='store', dest='user', default='root', required=True, help='user to login')
    return parser.parse_args()


def __getcmdpath():
    cmdpath = os.popen("find /opt -name 'kafka-topics.sh'")
    rr = cmdpath.readlines()
    if len(rr) == 0:
        print("cann't find cmd kakfa-topics.sh ")
        sys.exit(1)
    elif len(rr) > 1:
        print("find cmd more than one.")
        sys.exit(1)
    else:
        print("cmd", rr[0])
        return rr[0].replace("\n", "")


class checkKafka():
    def __init__(self, hosts, cmd, port, user):
        self.hosts = []
        self.user = user
        if "," in hosts:
            self.hosts = hosts.split(",")
        else:
            self.hosts.append(hosts)
        self.cmd = cmd
        self.port = port

    def __chechThread(self):
        rt = []
        for h in self.hosts:
            fcmd = "ssh "+self.user+"@"+h+"  'source /etc/profile;jps -l | grep -v grep | grep kafka'"
            results = os.popen(fcmd)
            lines = results.readlines()
            err = 0
            if "kafka.Kafka" in str(lines):
                rt.append(h+" kafka is running.")
            else:
                err += 1
        print(rt)
        if err >= len(self.hosts):
            print("Kafka cluser is not running....")
            sys.exit(22)

    def __checkwork(self):
        host = self.hosts[0]
        pcmd = "ssh "+self.user+"@"+host+" 'source /etc/profile; "+self.cmd+" --bootstrap-server "+host+":"+str(self.port)+"" \
                " --describe --topic __consumer_offsets'"
        print("pcmd", pcmd)
        pret = os.popen(pcmd)
        lines = pret.readlines()
        # find exception
        for lin in lines:
           # print("find exception:", lin)
            if "error" in lin or "Error" in lin or "Exception" in lin or "exception" in lin:
                print("cmd is right, or kafka cluster is error.")
                sys.exit(23)

        # find losts
        losts = 0
        if len(lines) > 1:
            for line in lines[1:]:
              #  print("analyse line:", line)
              #  print(int(line.split("\t")[3].split(":")[1]))
                if int(line.split("\t")[3].split(":")[1]) == -1:
                       losts += 1
                if losts > 1:
                    print("kafka cluster lost leader.")
                    sys.exit(25)
        else:
            print("kafka cluster error.")
            sys.exit(24)


    def check(self):
        self.__chechThread()
        self.__checkwork()
        print("cluster is ok.")


def main():
    parser = __paramparaser()
    if parser.cmd is not None and "kafka-topics" in parser.cmd:
        params = dict(cmd=parser.cmd, host=parser.host, port=parser.port, user=parser.user)
    else:
        cpath = __getcmdpath()
        params = dict(cmd=cpath, host=parser.host, port=parser.port, user=parser.user)
    print(params)
    ck = checkKafka(params['host'], params['cmd'], params['port'], params['user'])
    ck.check()

# python checkKafka.py -c /mnt/kafka_2.11-2.2.0/bin/kafka-topics.sh -i name1,node1,node2 -u root -p 9092

if __name__ == '__main__':
    main()