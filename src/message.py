# !/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'Zhiquan Wang'
__date__ = '2018/7/21 22:12'

import json

class PlayerCommand(object):

    def __init__(self, _x, _y):
        self.__target_x = _x
        self.__target_y = _y


class GameInfo(object):
    def __init__(self, _m, _r):
        self.__map_info = _m
        self.__round = _r
