#!/bin/env python
# coding:utf-8

import os
import argparse
import sys
import logging
import time
import socket
import subprocess
import json

def getparam():
    paas = argparse.ArgumentParser(description="get {} param.".format(sys.argv[0]))
    paas.add_argument("-gip", "--ossgwIp", action='store', required=True, dest='ossgwip', help="ossgw ip")
    paas.add_argument("-sip", "--smIp", action='store', required=True, dest="smip", help="sm ip")
    paas.add_argument("-thre", "--threshold", action='store', required=True, dest="thres", help="lag threshold")
    return paas.parse_args()


class checkLagObj(object):
    def __init__(self, gip, sip, thres):
        self.gip = gip
        self.sip = sip
        self.threshold = thres
        self.datepat = "%Y-%m-%d"
        self.timepat = "%Y-%m-%d %H:%M:%S"
        self.scriptname = sys.argv[0]
        self.hostname = socket.gethostname()
        self.logname = self.scriptname + '-' + time.strftime(self.datepat, time.localtime()) + ".log"
        self.cmdpath = "/opt/kafka-2.11/bin/kafka-consumer-groups.sh"
        self.Logpath = os.getcwd()
        self.Flagpath = os.getcwd()
        self.Statepath = "/opt/ericsson/nfvo/fcaps/config/common/nfvo-state"
        self.logger = getlogger(level=logging.INFO, log_file=os.path.join(self.Logpath, self.logname))

    def debug(self):
        self._log("logname = {}".format(self.logname))

    def _getossids(self):
        ll = list()
        ll.extend(("GDOSS", "JTOSS"))
        return ll

    def _checkifmaster(self):
        with open(self.Statepath, "r") as state:
            res = state.readline()
            if res == "MASTER":
                self._log("current is master")
            else:
                self._log("current isn't master, exist.")
                exit(1)


    def ifcheck(self):
        hh = self.hostname[-1]
        tt = time.localtime().tm_min
        self._log("hh = {}, res = {}".format(hh, (int(hh) % 3)))
        self._log("tt = {}, res = {}".format(tt, (int(tt) % 3)))
        if int(hh) % 3 == int(tt) % 3:
            return True
        else:
            return False


    def checkLag(self):
        if self.ifcheck():
            self._log("mod not equal.")
            return
        str = self.cmdpath + "  --bootstrap-server 10.163.249.146:9092  --describe --group alarm_consumer_{} "
        ids = self._getossids()
        if len(ids) > 0:
            for id in ids:
                fcmd = str.format(id) + "| awk '{print $5}' | grep -v 'LAG' | awk '{sum += $1} END {print sum}'"
                self._log("final cmd :{}".format(fcmd))
                ss = subprocess.Popen(fcmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                err = ss.stderr.readline()
                if len(err) > 0:
                    self._log("query {} group error:{}".format(id, err))
                    continue
                res = ss.stdout.readline()
                self._log("lag = {}".format(res))
                if int(res) > self.threshold:
                    self.sendAlarm(id)
                else:
                    self.sendClearAlarm(id)
        else:
            self._log("invalid ossid, get ossid:{}".format(str(ids)))

    # 发送告警
    def sendAlarm(self, ossid):
        if self._ifsendedalarm(ossid):
            self._log("{} already send alarm.".format(ossid))
            return
        alarm = self._genalarm(ossid)
        self._log("{} begin to send alarm. content is  :{}".format(ossid, alarm))
        # create file
        fp = os.path.join(self.Flagpath, ossid +"_pileup")
        if not os.path.isdir(self.Flagpath):
            os.makedirs(self.Flagpath)
        if not os.path.isfile(fp):
            fd = open(fp, mode="w")
            fd.close()

    # 发送清楚告警
    def sendClearAlarm(self, ossid):
        if not self._ifneedclear(ossid):
            self._log("{} needn't to send clear.".format(ossid))
            return
        clear = self._genclear(ossid)
        self._log("{} begin to send clear, content:{}".format(ossid, clear))
        fp = os.path.join(self.Flagpath, ossid + "_pileup")
        os.remove(fp)

    # true 已经发送过，否则没有发送过
    def _ifsendedalarm(self, ossid):
        fp = os.path.join(self.Flagpath, ossid +"_pileup")
        self._log("alarm : {}".format(fp))
        if os.path.exists(fp):
            return True
        else:
            return False

    # true 表示可以发送清楚告警
    def _ifneedclear(self, ossid):
        fp = os.path.join(self.Flagpath, ossid + "_pileup")
        self._log("clear : {}".format(fp))
        if os.path.exists(fp):
            return True
        else:
            return False

    def _genalarm(self, ossid):
        res = dict()
        res['key'] = 'NFVO_OSSmsgPileup'
        res['level'] = 'L1'
        res['object'] = ossid
        res['content'] = 'kafka topic:alarm_consumer_{}，超过积压阈值:{}'.format(ossid, self.threshold)
        res['hostname'] = self.hostname
        res['eventTime'] = time.strftime(self.timepat, time.localtime())
        return json.dumps(res).replace(r'"', r'\"')

    def _genclear(self, ossid):
        res = dict()
        res['key'] = 'NFVO_OSSmsgPileup'
        res['object'] = ossid
        res['hostname'] = self.hostname
        res['eventTime'] = time.strftime(self.timepat, time.localtime())
        res['cleared'] = True
        return json.dumps(res).replace(r'"', r'\"')


    def _log(self, msg):
        self.logger.info(msg)


def getlogger(level, log_file, logger_name='default.log'):
    logger = logging.getLogger(logger_name)
    logger.setLevel(level)
    fh = logging.FileHandler(filename=log_file, encoding="utf-8")
    fh.setLevel(level)
    fmt = logging.Formatter("%(asctime)s %(filename)s [line:%(lineno)d] %(name)s %(levelname)s %(message)s")
    fh.setFormatter(fmt)
    logger.addHandler(fh)
    return logger



if __name__ == "__main__":
    # pams = getparam()
    # print(pams)
    job = checkLagObj("20202", "101010", 20)
    job.debug()
    job.checkLag()
