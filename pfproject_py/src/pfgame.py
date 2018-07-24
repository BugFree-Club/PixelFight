# !/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'Zhiquan Wang'
__date__ = '2018/7/20 22:30'

from pfmap import *
from pfrule import *


class PixelFightGame(object):

    def __init__(self):
        self.__game_rule = PixelFightRule()
        self.__round_counter = 0
        self.__player_info_list = []
        self.__pixel_map = PixelMap(self.__game_rule.map_height, self.__game_rule.map_width)

    def launch_game(self):
        pass

    def load_game_rule(self):
        pass

    def gen_player_id(self, _socket_info):
        pass

    def attack_grid(self, _x, _y, _player_info):
        pass
