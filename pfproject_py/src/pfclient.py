# !/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'Zhiquan Wang'
__date__ = '2018/7/24 22:09'

import socket
import pfmap
from pfmessage import *

class PixelFightClient(object):
    def __init__(self, *, usr_name='DefaultUser', ip=None, port=None):
        self.__server_ip = ip
        self.__server_port = port
        self.__client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__usr_name = usr_name
        self.__login_id = None
        self.__pfmap = None

    def connect(self):
        self.__client_socket.connect((self.__server_ip, self.__server_port))

    def request(self, msg=None):
        self.__client_socket.send(msg)
        data = self.__client_socket.recv(1024).decode('utf-8')
        return data

    def login_request(self):
        log_req = LoginRequest(uname=self.__usr_name).dump_json().encode('utf-8')
        reply_msg = self.request(log_req)
        if reply_msg == MessageType.login_reply:
            log_rep = LoginReply(json_info=reply_msg)
            self.__login_id = log_req
        else:
            print("Error:pfclient.login_request")