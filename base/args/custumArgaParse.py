#!/usr/bin/python3
# coding=utf-8

import os
import argparse

"""
解析参数的函数
name/flags: 参数的名字
action: 遇到参数时的动作，默认值为 store
narsg: 参数的个数，可以是具体的数组，或者是 "+" 或 "*"。其中 + 表示1或多个参数，  *表示0或多个参数
const action 和 nargs: 需要的常量值
default: 不指定参数时的默认值
type: 参数的类型
choices: 参数允许的值
required: 可选，参数是否是必需的
help: 参数帮助信息
metavar: 在usage说明中参数名字
dest: 解析后的参数名称

"""
def __argparse():
    parse = argparse.ArgumentParser(description='A cmd param client')
    parse.add_argument('--host', action='store',  dest='host', required=True, help='connect host')
    parse.add_argument('-u', '--user', action='store', dest='user', required=True, help='user for login')
    parse.add_argument('-p', '--password', action='store', required=True, dest='password', help='password to use')
    parse.add_argument('-P', '--port', action='store', nargs=1, required=True, dest='port', help='custom port')
    parse.add_argument('-v', '--version', action='version', version='%(prog)s 0.1')
    return parse.parse_args()


def main():
    paser = __argparse()
    conn_args = dict(host=paser.host, user=paser.user, password=paser.password, port=paser.port)
    print(conn_args)


if __name__ == '__main__':
    main()
