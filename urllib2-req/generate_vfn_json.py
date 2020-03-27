#!/usr/bin/python
# coding = UTF-8

import urllib
import urllib2
import json
import time
import argparse
import subprocess
import os

"""
通过接口获取数据, 并写入到redis中
"""

class gen_json:
    def __init__(self, VNFInstanceId, eocaip, rip, uid):
        self.authHead = "X-Auth-Token"
        self.tokenName = "token"
        self.expireName = "expires_at"
        self.VNFInstanceId = VNFInstanceId
        self.eocaIp = eocaip
        self.token = dict()
        self.tokParm = {'username': 'internal_am', 'password': 'UXFxMTIzNDU2'}
        self.head = {'Content-Type': 'application/json'}
        self.vnfinfo = dict()
        self.vendor = list()
        self.vid = "vendor_id"
        self.vname = "vendor_name"
        self.redisip = rip
        self.rmuid = uid

    # 获取token
    def getToken(self):
        tokenurl = "http://{}:5000/eoca/v1.0/token".format(self.eocaIp)
        if self.head.has_key(self.authHead):
            del self.head[self.authHead]
        req = urllib2.Request(tokenurl, json.dumps(self.tokParm), headers=self.head)
        try:
            f = urllib2.urlopen(req)
            self.token = json.loads(f.read())
        except urllib2.HTTPError as ex:
            print("get Token error:%s" % ex)
            exit(1)

    ## 对时间进行判断
    def checkExpired(self):
        pattern = "%Y-%m-%dT%H:%M:%S"
        return ((time.mktime(time.strptime(self.token[self.expireName], pattern)) - time.time())>0)

    ## 获取vnf的信息，具体信息可以看需求txt
    def getVfnInfo(self):
        infourl = "http://{}:8085/eoca/v1.0/wf/info/vnf/id_in_m/{}".format(self.eocaIp, self.VNFInstanceId)
        # print(infourl)
        if not self.checkExpired():
            self.getToken()
        self.head[self.authHead] = self.token[self.tokenName]
        req = urllib2.Request(infourl,headers=self.head)
        try:
            f = urllib2.urlopen(req)
            self.vnfinfo = json.loads(f.read())
        except BaseException as ex:
            print("getVnfInfo error :%s" % ex)
            exit(1)

    # 获取vendor 信息
    def getVendor(self):
        vendorUrl = "http://{}:8085/eoca/v1.0/wf/conf/vendor".format(self.eocaIp)
        if not self.checkExpired():
            self.getToken()
        self.head[self.authHead] = self.token[self.tokenName]
        req = urllib2.Request(vendorUrl, headers=self.head)
        try:
            f = urllib2.urlopen(req)
            self.vendor = json.loads(f.read())
        except BaseException as ex:
            print("getVendor error :%s" % ex)
            exit(1)

    # 获取regionpath信息
    def getRegionPath(self):
        regionUrl = "http://{}:5000/eoca/v1.0/region_path/info".format(self.eocaIp)
        regionHead = {self.authHead: self.token[self.tokenName]}
        param = {"region_path": self.vnfinfo['region_path']}
        finUrl = regionUrl+"?"+urllib.urlencode(param)
        req = urllib2.Request(finUrl, headers=regionHead)
        try:
            f = urllib2.urlopen(req)
            provs = str(json.loads(f.read())['province_abbr_list'])
            if provs.count(",") > 0:
                provs = provs[1:len(provs) - 1].replace(",", ";")
            # print("provs = {}".format(provs))
            return provs
        except BaseException as ex:
            print("getRegionPath error :%s" % ex)
            exit(1)

    # 获取vnftype
    def getVnfType(self):
        typeUrl = "http://{}:8085/eoca/v1.0/wf/conf/vnfspecialty_by_vnftype".format(self.eocaIp)
        finurl = typeUrl + "?vnf_type=" + self.vnfinfo['vnf_type']
        if not self.checkExpired():
            self.getToken()
        self.head[self.authHead] = self.token[self.tokenName]
        req = urllib2.Request(finurl, headers=self.head)
        try:
            f = urllib2.urlopen(req)
            result = f.read()
            dic = json.loads(result[1:len(result) - 1])
            # print(dic["specialty_id"])
            return dic["specialty_id"]
        except BaseException as ex:
            print("getVnfType error :%s" % ex)
            exit(1)

    ## 数据处理, 获取json中一个list中所有dict数据的id
    def getVmids(self):
        ids = list()
        vmlist = self.vnfinfo['vm_list']
        # print(vmlist)
        for i in vmlist:
            ids.append(i['id'])
        return ids

    # 根据vendor id 获取vendorname
    def getVendorName(self):
        self.getVendor()
        for i in self.vendor:
            if i[self.vid] == self.vnfinfo['vendor']:
                return i[self.vname]


    # 生成json数据
    def getJson(self):
        self.getToken()
        self.getVfnInfo()
        dicFm = dict()
        dicFm['regionPath'] = self.vnfinfo['region_path']
        dicFm['vnfType'] = self.vnfinfo['vnf_type']
        dicFm['specialty'] = self.getVnfType()
        dicFm['province'] = self.getRegionPath()
        dicFm['vimId'] = self.vnfinfo['vim_id']
        dicFm['vendor'] = self.vnfinfo['vendor']
        dicFm['vmIdList'] = self.getVmids()
        dicFm['vendorName'] = self.getVendorName()
        dicFm['vnfmVnfInstanceId'] = self.vnfinfo['vnfm_vnf_instance_id']
        dicFm['productName'] = self.vnfinfo['product_name']
        dicFm['vnfName'] = self.vnfinfo['vnf_name']
        fjson = json.dumps(dicFm)
        return fjson

    # 插入reids的操作
    def _insertOperator(self, key, field, val):
        dstr = "/opt/redis-5.0.0/6379/redis-cli"
        cmd = dstr+" -h {} -p 6379 -c hset {} {} {}".format(self.redisip, key, field,  val)
        # print("cmd = {}".format(cmd))
        rr = subprocess.Popen(cmd, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, close_fds=True)
        errMsg = rr.stderr.readline()
        if len(errMsg) > 0:
            print("insert {} error".format(key))
        # out = rr.stdout.readline()

    # 具体要插入的数据
    def insertData(self):
        key1 = "fm:resource:vnf:vnfinstanceid_info"
        key2 = "fm:resource:vnf:vnfinstanceid_rmuid"
        key3 = "fm:resource:vnf:rmuid_vnfinstanceid"
        self._insertOperator(key1, self.VNFInstanceId, self.getJson())
        self._insertOperator(key2, self.VNFInstanceId, self.rmuid)
        self._insertOperator(key3, self.rmuid, self.VNFInstanceId)
        print("insert complete!")

def getIp():
    ip = os.popen("cat /opt/redis-5.0.0/6379/redis.conf | grep -v '^#' | grep bind | awk '{print $2}'").readline()
    return ip.strip()

def getInput():
    args = argparse.ArgumentParser(description="generate fm redis info.")
    args.add_argument("-uid", action='store', dest='rmUID', required=True, help="objectID")
    args.add_argument("-vid", action='store', dest='VNFId', required=True, help="VNFInstanceId")
    args.add_argument("-vip", action='store', dest='vip', required=True, help="f5 vip, for connect eoca")
    args.add_argument('-rip', action='store', dest='rip',default=getIp(), required=False, help="One of redis cluster instance ip.")
    return args.parse_args()


def main():
    # example:  python genj.py -uid uuuu 0vid "E105" -vip "10.163.161.188" -rip "10.163.249.146"
    arguments = getInput()
    fun = gen_json(arguments.VNFId, arguments.vip, arguments.rip, arguments.rmUID)
    fun.insertData()

    """
    print("rmUID = {}".format(arguments.rmUID))
    print("rip={}".format(arguments.rip))
    print("vnfid={}".format(arguments.VNFId))
    print("vip={}".format(arguments.vip))
    jj = fun.getJson()
    print(jj)

    fun.getToken()
    print(fun.token)
    print(fun.checkExpired())
    fun.getVfnInfo()
    print(fun.vnfinfo)
    fun.getVendor()
    print(fun.vendor)
    fun.getRegionPath()
    fun.getVnfType()
    jj = fun.getJson()
    print(jj)
    """

if __name__ == "__main__":
    main()