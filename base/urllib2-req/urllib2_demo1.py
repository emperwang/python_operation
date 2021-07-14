#!/usr/bin/python
# coding=UTF-8
import urllib
import urllib2
import json

'''
需求: 调用各个接口获取数据 并组装成json格式  最后填写到redis中
'''
header = {"Content-Type": "application/json",
          "X-Auth-Token": "ZXlKa1pXWmxjaUk2Wm1Gc2MyVXNJblZ6WlhKZmFXUWlPaUprTkdRd04yRmxORGt5TURaaVpXVTBaRFJsT1RrMU5XUTRZek16WlRZM015SXNJbUZzWnlJNklraFRNalUySWl3aWRIbHdJam9pU2xkVUlpd2ljM0JsSWpwbVlXeHpaU3dpYzNWaVgzTnBaMjRpT2lKalpHUm1OREJqWkMxaU0yVTFMVFEyWXpndFlqUTFOeTFtTXpJek4yWmtOakJrTVRJaWZRLmV5SnBZWFFpT2pFMU9EVXlPRGN6T1RrdU1Dd2ljbTlzWlNJNkltRmtiV2x1SWl3aVpYaHdJam94TlRnMU16Y3pOems1TGpCOS5GWUZNUWhTVmpoUi1oaTVjazRLcVRaX1ZoWnlmVUFUb1BCWFRzcjk2VDNR"}
def getToken():
    data = json.dumps({"username": "internal_am", "password": "UXFxMTIzNDU2"})
    # data = json.dumps({"username":"admin","password":"UXFxMTIzNDU2"})
    req = urllib2.Request("http://10.163.161.188:5000/eoca/v1.0/token", data, {'Content-Type': 'application/json'})
    f = urllib2.urlopen(req)
    result = f.read()
    dic = json.loads(f)
    token = dic['token']
    return token

def getVnfInfo():
    url = "http://10.163.161.188:8085/eoca/v1.0/wf/info/vnf/id_in_m/E105"
    req = urllib2.Request(url, headers=header)
    f = urllib2.urlopen(req)
    result = f.read()
    dic = json.loads(result)
    print(result)
    return dic


def getVendor():
    vendUrl = "http://10.163.161.188:8085/eoca/v1.0/wf/conf/vendor"
    req = urllib2.Request(vendUrl, headers=header)
    f = urllib2.urlopen(req)
    result = f.read()
    print(result)
    dic = json.loads(result)
    return dic

def getRegionPath():
    regionheader = {"X-Auth-Token": "ZXlKaGJHY2lPaUpJVXpJMU5pSXNJblZ6WlhKZmFXUWlPaUkwTVRSbU5EVTFOekpqWTJaa05ERXhObU5qTmpjMll6ZG1NalkzTWpSbE15SXNJblI1Y0NJNklrcFhWQ0lzSW5Od1pTSTZkSEoxWlN3aVpHVm1aWElpT21aaGJITmxmUS5leUpwWVhRaU9qRTFPRFV5TWpjMk1qRXVNQ3dpY205c1pTSTZJaUlzSW1WNGNDSTZNVFU0TlRNeE5EQXlNUzR3ZlEuVHVNblJ2V0hjcllrUVFyT0pXb2x1UFl6SWxuQU0tOXNjNFRFRjk5OVNUTQ=="}
    getRegionurl = "http://10.163.161.188:5000/eoca/v1.0/region_path/info"
    param = {'region_path': '/0HN/3vim~nokia'}
    getRegionurl2 = getRegionurl + "?" + urllib.urlencode(param)
    req = urllib2.Request(getRegionurl2, headers=regionheader)
    f = urllib2.urlopen(req)
    result = f.read()
    provs = str(json.loads(result)["province_abbr_list"])
    if provs.count(",") > 0:
        provs = provs[1:len(provs)-1].replace(",",";")
    print("provs = {}".format(provs))
    return provs


def getVnfType():
    vnfTypeUrl = "http://10.163.161.188:8085/eoca/v1.0/wf/conf/vnfspecialty_by_vnftype?vnf_type=PGWC"
    req = urllib2.Request(vnfTypeUrl, headers=header)
    f = urllib2.urlopen(req)
    result = f.read()
    print(result)
    dic = json.loads(result[1:len(result)-1])
    return dic["specialty_id"]


if __name__ == "__main__":
    getToken()