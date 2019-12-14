#!/usr/bin/python3
# coding=utf-8

import os
import argparse

"""
解析参数的函数
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
