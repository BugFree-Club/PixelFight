# !/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'Zhiquan Wang'
__date__ = '2018/7/20 22:28'

from networkservice import *
from pfgame import *
from pfmessage import *


class PixelFightSystem(object):
    def __init__(self, *, ip=None, port=None):
        self.__networkSev = NetworkService(ip, port)
        self.__game = PixelFightGame()

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

    def __address_msg(self, _c_socket_info):
        client_socket = _c_socket_info[0]
        try:
            # Receive Client Message
            while True:
                data = client_socket.recv(2048)
                if not data:
                    break
                client_msg = data.decode('utf-8')
                server_reply = self.__address_request(client_msg, client_socket)
                print(u'Client Message : ' + client_msg)
                client_socket.sendall(server_reply.encode('utf-8'))
            client_socket.close()
        except Exception:
            print('Error:Class:PixelFightSystem:address_msg')
            client_socket.close()

    def __address_request(self, _msg, _s):
        tmp_type = get_msg_type(_msg)
        if tmp_type == MessageType.login_request:
            tmp_obj = LoginRequest(json_info=_msg)
            tmp_id = self.__game.gen_player_id(tmp_obj.usr_name, _s)
            return LoginReply(id=tmp_id).dump_json()
        else:
            return "Unknown Message"

    def manage_cmd(self):
        while True:
            cmd = input('>>')
            if cmd == 'start':
                self.__game.launch()
