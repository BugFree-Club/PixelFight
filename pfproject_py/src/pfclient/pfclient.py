# !/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'Zhiquan Wang'
__date__ = '2018/7/24 22:09'

import socket


class PixelFightClient(object):
    def __init__(self, *, ip=None, port=None):
        self.__server_ip = ip
        self.__server_port = port
        self.__client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.__client_socket.connect((self.__server_ip, self.__server_port))

    def send(self, msg=None):
        self.__client_socket.send(msg)
