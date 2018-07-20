# !/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'Zhiquan Wang'
__date__ = '2018/7/20 22:33'

class PixelFightRule(object):

    def __init__(self):
        self.__max_round = 0
        self.__map_height = 0
        self.__map_width = 0
        self.__player_num = 0
        self.__empty_grid_time = 0 # 占领空白网格时间
        self.__player_grid_time = 0 # 占领玩家网格时间