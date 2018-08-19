# !/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'Zhiquan Wang'
__date__ = '2018/7/20 22:30'

from pfmap import *
from pfrule import *
from pfplayer import *
from pfmessage import *
import time
import md5manager


class PixelFightGame(object):

    def __init__(self):
        self.__game_rule = PixelFightRule()
        self.__round_counter = 0
        self.__game_ratio = 0
        self.__player_info_list = []
        self.__pixel_map = PixelMap(map_height=self.__game_rule.map_height, map_width=self.__game_rule.map_width)
        self.__is_pause = False
        self.__is_ready = False

    # 开始比赛,每回合轮流向玩家发送地图信息,并接收玩家攻击坐标
    def launch(self):
        print('System Waiting')
        while self.__is_ready is False:
            pass
        print('Game Launched')
        max_round = self.__game_rule.max_round
        for tmp_i in range(self.__game_rule.max_round):
            self.__round_counter = tmp_i
            for tmp_player in self.__player_info_list:
                while self.__is_pause:
                    pass
                tmp_game_info = GameInfo(pf_map=self.__pixel_map, pf_round=self.__round_counter)
                tmp_player.socket_info.sendall(tmp_game_info.dump_json().encode('utf-8'))
                self.__is_pause = True

    @property
    def max_round(self):
        return self.__game_rule.max_round

    @property
    def round_counter(self):
        return self.__round_counter

    @round_counter.setter
    def round_counter(self, _c):
        self.__round_counter = _c

    @property
    def player_info_list(self):
        return self.__player_info_list

    @property
    def pixel_map(self):
        return self.__pixel_map

    @property
    def game_rule(self):
        return self.__game_rule

    @property
    def is_pause(self):
        return self.__is_pause

    @is_pause.setter
    def is_pause(self, _flag):
        self.__is_pause = _flag

    def load_game_rule(self):
        pass

    # 生成玩家ID
    def gen_player_id(self, _uname, _socket_info):
        if len(self.__player_info_list) >= self.__game_rule.player_num:
            return '0'
        tmp_id = md5manager.create_md5((_uname, _socket_info.getpeername(), time.time()))
        tmp_p = PixelFightPlayer(usr_name=_uname, login_id=tmp_id, socket=_socket_info)
        self.add_player(tmp_p)
        # self.launch()
        return tmp_id

    def add_player(self, _p):
        if len(self.__player_info_list) < self.game_rule.player_num:
            self.__player_info_list.append(_p)
            if len(self.__player_info_list) == self.game_rule.player_num:
                self.__is_ready = True
        return

    def attack_grid(self, _x, _y, _player_id):
        pass
