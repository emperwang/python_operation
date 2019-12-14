#!/usr/bin/python
# coding=utf-8

import argparse
import os

BASE = os.getcwd()

def __paramparse():
    parse = argparse.ArgumentParser(description='redis cluster check')
    parse.add_argument('-c', '--cmd', action='store', dest='cmd', required=True, help='cmd to exec.')
    parse.add_argument('-i', '--host', action='store', dest='host', required=True, help='host to check.')
    return parse.parse_args()

def main():
    paser = __paramparse()
    parms = dict(cmd=paser.cmd, host=paser.host)
    print(parms)


if __name__ == '__main__':
    main()