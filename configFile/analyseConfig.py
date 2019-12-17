#!/usr/bin/python
# coding=utf-8
import configparser
import os

BASE = os.getcwd().replace("\\", "/")
name = BASE + "/config.cfg"


def main():
    pase = configparser.ConfigParser(allow_no_value=True)
    print("path", name)
    pase.read(name, encoding="UTF-8")
    # 获取一个section中的所有 option 中的 key
    options = pase.options("client")
    print("options :", options)
    # 获取所有的section
    secs = pase.sections()
    print("sections:", secs)
    # 获取所有
    itms = pase.items("client")
    print("itms :", itms)

    # 判断是否有section
    hasClient = pase.has_section("client")
    print("hasClient :", hasClient)

    # 判断是否有 option
    hasUser = pase.has_option(section="client", option="user")
    print("hasUser :", hasUser)
    # 添加一个section
    pase.add_section("slave")
    # 这是一个值
    pase.set("slave", "id", "1")

    # 删除一个option
    #pase.remove_option("client", "port")
    # 删除一个section
    #pase.remove_section("client")

    # 获取值
    port = pase.get("client", "port")
    ib = pase.getboolean("client", "isMaster")
    fs = pase.getfloat("client", "floats")
    isInt = pase.getint("client", "int")
    print("port:", port, "ib:", ib, "fs:", fs, "inInt:", isInt)
    # 保存到文件
    pase.write(open(BASE+"/config2.conf", mode="w+"))


if __name__ == '__main__':
    main()