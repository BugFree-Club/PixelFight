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
        self.__empty_grid_time = 0  # 占领空白网格时间
        self.__player_grid_time = 0  # 占领玩家网格时间

    @property
    def max_round(self):
        return self.__max_round

    @max_round.setter
    def max_round(self, _v):
        self.__max_round = _v

    @property
    def map_height(self):
        return self.__map_height

    @map_height.setter
    def map_height(self, _h):
        self.__map_height = _h

    @property
    def map_width(self):
        return self.__map_width

    @map_width.setter
    def map_width(self, _w):
        self.__map_width = _w

    @property
    def player_num(self):
        return self.__player_num

    @player_num.setter
    def player_num(self,_v):
        self.__player_num = _v

    @property
    def empty_grid_time(self):
        return self.__empty_grid_time

    @empty_grid_time.setter
    def empty_grid_time(self,_v):
        self.__empty_grid_time = _v
