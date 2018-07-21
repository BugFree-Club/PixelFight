# !/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'Zhiquan Wang'
__date__ = '2018/7/21 22:07'

import socket
import threading


class NetworkService(object):
    def __init__(self, _ip, _p):
        self.__host_ip = _ip
        self.__port = _p
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__socket.bind((self.__host_ip, self.__port))
        self.__max_connect_num = 512

    def launch_server(self):
        try:
            self.__socket.listen(self.__max_connect_num)
            while True:
                client_socket_info = self.__socket.accept()
                address_thread = threading.Thread(target=self.__address_request, args=(client_socket_info,))
                address_thread.start()
        except Exception:
            print('Launch Server System Failed')

    def __address_request(self, _c_socket_info):
        client_socket = _c_socket_info[0]
        try:
            # Receive Client Message
            while True:
                data = client_socket.recv(2048)
                if not data:
                    break
                client_msg = Message.Request(data.decode('utf-8'))
                server_reply = self.__ref_ser_manager.address_request(client_msg, _c_socket_info)
                client_socket.sendall(server_reply.get_message().encode('utf-8'))
            client_socket.close()
        except Exception:
            logging.exception('Class:ServerNetwork:address_request')
            client_socket.close()
