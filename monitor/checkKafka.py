#!/usr/bin/python
# coding=utf-8

import os
import argparse

BASE = os.getcwd()

def __paramparaser():
    parser = argparse.ArgumentParser(description='kafka cluster check.')
    parser.add_argument("-c", "--cmd", action='store', dest='cmd', required=True, help='cmd to exec')
    parser.add_argument("-i", "--host", action='store', dest='host', required=True, help="host to check")
    return parser.parse_args()


def main():
    parser = __paramparaser()
    params = dict(cmd=parser.cmd, host=parser.host)
    print(params)


if __name__ == '__main__':
    main()