#!/usr/bin/python
# coding=utf-8

import socket
import re

import multiprocessing  # 多进程处理模块

# root directory
ROOT_DIR = "/opt/simulator/httpFileServer/filesData"


# 利用多进程来处理 http的请求，利用socket进行接收
class HTTPServer(object):
    """
    使用socket进行监听http请求, 并发送文件. 利用多进程来进行处理
    http server
    """
    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def start(self):
        """

        :return:
        """
        self.server_socket.listen(128)
        while True:
            client_socket, client_address = self.server_socket.accept()
            print("[%s, %s]!"%(client_address, client_socket))
            handle_client_process = multiprocessing.Process(target= self.handle_client, args=(client_socket, ))
            handle_client_process.start()
            client_socket.close()

    def handle_client(self, client_socket):
        """
        :param client_socket:
        :return:
        """
        # get the request from client
        request_data = client_socket.recv(1024)
        print("request data :", request_data)
        request_lines = request_data.splitlines()
        # parse request message
        request_start_line = request_lines[0]

        # extract the file name from url
        request_uri = re.match(r"\w+ +(/[^ ]*)", request_start_line.decode("utf-8")).group(1)
        print("request_uri = "+request_uri)
        uri_paths = request_uri.split("/")
        file_name = uri_paths[-1]
        print("file_name :"+file_name)

        # open the file and read content
        subpath=''
        try:
            if 'vimCm' in request_uri:
                subpath = 'vimCm'
            elif 'vimPm' in request_uri:
                subpath = 'vimPm'
            elif 'pimPm' in request_uri:
                subpath = 'pimPm'
            file_fullpath = ROOT_DIR + "/"+subpath+"/" +file_name
            print("open file {}:".format(file_fullpath))
            file = open(file_fullpath, "rb")
        except IOError:
            response_start_line = "HTTP/1.1 404 Not Found\r\n"
            response_headers = "Server: Simple http file server\r\n"
            response_body = "The file is not found!"
        else:
            file_data = file.read()
            file.close()
            # construct response data
            response_start_line = "HTTP/1.1 200 OK\r\n"
            response_headers = "Server:simple http file server\r\n"
            response_body = file_data
        response = response_start_line+response_headers + "\r\n"+response_body
        client_socket.send(bytes(response))
        client_socket.close()

    def bind(self, port):
        """

        :param port:
        :return:
        """
        self.server_socket.bind(("", port))


if __name__ == '__main__':
    server = HTTPServer()
    server.bind(8000)
    print("listen on 8000")
    server.start()
