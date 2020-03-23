#!/usr/bin/python
# coding=utf-8

import socket


def client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 9999
    client.connect((host, port))
    msg = client.recv(1024)
    client.close()
    print("receive msg :{}".format(msg))


if __name__ == '__main__':
    client()
