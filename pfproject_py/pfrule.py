# !/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'Zhiquan Wang'
__date__ = '2018/7/20 22:33'

import os
import json
from pfmessage import *


class PixelFightRule(object):

    def __init__(self, _mr=1000, _mh=0, _mw=0, _pn=0, _egt=0, _pgr=0):
        self.__max_round = _mr
        self.__map_height = _mh
        self.__map_width = _mw
        self.__player_num = _pn
        self.__empty_grid_time = _egt  # 占领空白网格时间
        self.__player_grid_time = _pgr  # 占领玩家网格时间

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
    def player_num(self, _v):
        self.__player_num = _v

    @property
    def empty_grid_time(self):
        return self.__empty_grid_time

    @empty_grid_time.setter
    def empty_grid_time(self, _v):
        self.__empty_grid_time = _v

    def __dict__(self):
        return {JsonAttribute.pfr_max_round: self.__max_round,
                JsonAttribute.pfr_map_height: self.__map_height,
                JsonAttribute.pfr_map_width: self.__map_width,
                JsonAttribute.pfr_player_num: self.__player_num,
                JsonAttribute.pfr_empty_grid_time: self.__empty_grid_time,
                JsonAttribute.pfr_player_grid_time: self.__player_grid_time}

    def dump_json(self):
        return json.dumps(self.__dict__(), indent=4)

    def output(self, _f_name):
        cur_path = os.path.abspath('.')
        cur_path = os.path.join(cur_path, _f_name)
        with open(cur_path, 'w') as f:
            f.write(self.dump_json())

    def load(self, _path):
        with open(_path, 'r') as f:
            context = f.read()
        tmp_dic = json.loads(context)
        self.__max_round = tmp_dic[JsonAttribute.pfr_max_round]
        self.__map_height = tmp_dic[JsonAttribute.pfr_map_height]
        self.__map_width = tmp_dic[JsonAttribute.pfr_map_width]
        self.__player_num = tmp_dic[JsonAttribute.pfr_player_num]
        self.__empty_grid_time = tmp_dic[JsonAttribute.pfr_empty_grid_time]
        self.__player_grid_time = tmp_dic[JsonAttribute.pfr_player_grid_time]
