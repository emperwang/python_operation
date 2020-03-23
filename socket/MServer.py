#!/usr/bin/python
# coding=utf-8

import socket


def server():
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 9999
    server.bind((host,port))
    server.listen(10)
    while True:
        clientSocket, addr = server.accept()
        print("get a connection from {}".format(addr))
        msg = "Thank you for a=connecting\r\n"
        clientSocket.send(msg.encode("ascii"))
        clientSocket.close()


if __name__ == '__main__':
    server()