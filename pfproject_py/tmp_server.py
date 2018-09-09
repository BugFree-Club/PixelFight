# !/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'Zhiquan Wang'
__date__ = '2018/7/24 21:56'


from pfsystem import *

if __name__ == '__main__':
    tmp_sys = PixelFightSystem(ip='192.168.43.9', port=7707)
    tmp_sys.launch()
