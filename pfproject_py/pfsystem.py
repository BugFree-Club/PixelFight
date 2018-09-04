# !/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'Zhiquan Wang'
__date__ = '2018/7/20 22:28'

import threading
from networkservice import *
from pfgame import *
from pfmessage import *


class PixelFightSystem(object):
    def __init__(self, *, ip=None, port=None):
        self.__networkSev = NetworkService(ip, port)
        self.__game = PixelFightGame()

    def launch(self):
        network_thread = threading.Thread(target=self.launch_socket)
        network_thread.start()
        self.__game.launch()

    # 开启服务器端监听
    # 每当收到建立新的连接,开启一个线程处理
    def launch_socket(self):
        try:
            self.__networkSev.listen()
            print('Start Listening')
            while True:
                client_socket_info = self.__networkSev.socket.accept()
                address_thread = threading.Thread(target=self.__address_msg, args=(client_socket_info,))
                address_thread.start()
        except Exception:
            print('Launch Server System Failed')

    # 连接处理线程,保持接受状态,每当收到新的请求,处理并返回结果
    def __address_msg(self, _c_socket_info):
        client_socket = _c_socket_info[0]
        # try:
            # Receive Client Message
        while True:
            data = client_socket.recv(2048)
            if not data:
                continue
            client_msg = data.decode('utf-8')
            self.__address_request(client_msg, client_socket)
       # except Exception as e:
       #     print('Error:Class:PixelFightSystem:address_msg :' + str(e))
       #     client_socket.close()

    # 请求处理函数,识别请求类别并提供服务
    def __address_request(self, _msg, _s):
        tmp_type = get_msg_type(_msg)
        print(u'Server Receive:' + _msg + ':End')
        if tmp_type == MessageType.login_request:
            tmp_obj = LoginRequest(json_info=_msg)
            tmp_id = self.__game.gen_player_id(tmp_obj.usr_name, _s)
            tmp_rep = LoginReply(id=tmp_id).dump_json()
            _s.sendall(tmp_rep.encode('utf-8'))
            print(u'Server Reply:' + tmp_rep + ':End')
            if len(self.__game.player_info_list) == self.__game.game_rule.player_num:
                self.__game.is_ready = True
        elif tmp_type == MessageType.attack_request:
            tmp_obj = AttackRequest(json_info=_msg)
            self.__game.attack_grid(tmp_obj.x, tmp_obj.y, tmp_obj.player_id)
            print("Player :" + tmp_obj.player_id + "Attack : " + str(tmp_obj.x) + " - " + str(tmp_obj.y))
            self.__game.is_pause = False

