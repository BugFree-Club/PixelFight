# !/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'Zhiquan Wang'
__date__ = '2018/7/24 21:56'


from pfsystem import *

if __name__ == '__main__':
    tmp_sys = PixelFightSystem(ip='127.0.0.1', port=7878)
    tmp_sys.launch_socket()
