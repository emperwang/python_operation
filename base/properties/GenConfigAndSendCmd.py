#!/usr/bin/python3
# coding=utf-8
import sys
import os
cur = os.getcwd()
sys.path.append(cur)

from PropertiesParse import properties
# analyse file, get config
pro = properties("file.properties")

# verification
# pro.parse()
# pro.travelProperties()

# get conig
url = pro.getkey("sparkUrl")
port1 = pro.getkey("spark.driver.port1")
port2 = pro.getkey("spark.driver.port2")
port3 = pro.getkey("spark.driver.port3")

ports = {port1, port2, port3}
ips = []
for u in url.split(","):
    for pt in ports:
        ips.append(u.split(":")[0]+":"+pt)
# get final url
print(ips)
# 调用shell 脚本  并传递参数
for utmp in ips:
    os.system("./paraseArg.sh " + utmp)



