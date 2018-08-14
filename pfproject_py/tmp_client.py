# !/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'Zhiquan Wang'
__date__ = '2018/7/24 21:56'

import socket
import threading
from pfmessage import *
from pfclient import *

def test(i):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 7878))
    tmp_req = LoginRequest(uname='zhiquan')
    s.send(tmp_req.dump_json().encode('utf-8'))
    while True:
        data = s.recv(1024).decode('utf-8')
        print("Client Receive:" + data + ":End")


if __name__ == '__main__':
   tmp_client = PixelFightClient().launch_socket()
