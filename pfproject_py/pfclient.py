# !/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'Zhiquan Wang'
__date__ = '2018/7/24 22:09'

import socket
import attack_method
from pfmessage import *


class PixelFightClient(object):
    def __init__(self, *, usr_name='DefaultUser', ip='127.0.0.1', port=7707):
        self.__server_ip = ip
        self.__server_port = port
        self.__client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__usr_name = usr_name
        self.__login_id = None
        self.__pfmap = None
        self.__is_busy = False
        self.__message = None
        self.__cur_pos = [0, 0]
        self.__cur_round = 0

    def __connect(self):
        self.__client_socket.connect((self.__server_ip, self.__server_port))

    def __request(self, msg=None):
        self.__is_busy = True
        self.__client_socket.sendall(msg)
        print('Client Send: ', msg)
        data = self.__client_socket.recv(1024).decode('utf-8')
        self.__is_busy = False
        return data

    # 开启客户端,连接服务器,获取登陆码
    def launch_socket(self):
        self.__connect()
        self.login_request()
        while True:
            if self.__login_id is None:
                continue
            if self.__is_busy is False:
                data = self.__client_socket.recv(1024 * 1024).decode('utf-8')
                if not data:
                    continue
                print("Client Receive:" + data + ":End")

                if get_msg_type(data) == MessageType.game_info:
                    tmp_info = GameInfo(json_info=data)
                    self.attack_request(tmp_info)

    def login_request(self):
        log_req = LoginRequest(uname=self.__usr_name).dump_json().encode('utf-8')
        reply_msg = self.__request(log_req)
        if get_msg_type(reply_msg) == MessageType.login_reply:
            log_rep = LoginReply(json_info=reply_msg)
            self.__login_id = log_rep.login_id
            print("Login Succeed")
        else:
            print("Error:pfclient.login_request")

    def attack_request(self, tmp_info):
        self.__cur_round = tmp_info.round
        tmp_pos = attack_method.attack(tmp_info)
        tmp_cmd = AttackRequest(x=tmp_pos[0], y=tmp_pos[1], player_id=self.__login_id)
        print(tmp_cmd.dump_json())
        self.__client_socket.sendall(tmp_cmd.dump_json().encode('utf-8'))


