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
        self.__pixel_map = PixelMap(self.__game_rule.map_height, self.__game_rule.map_width)

    # 开始比赛,每回合轮流向玩家发送地图信息,并接收玩家攻击坐标
    def launch(self):
        max_round = self.__game_rule.max_round
        for tmp_i in range(self.__game_rule.max_round):
            self.__round_counter = tmp_i
            for tmp_player in self.__player_info_list:
                print(tmp_player)
                tmp_game_info = GameInfo(pf_map=self.__pixel_map, pf_round=self.__round_counter)
                print('1')
                print(tmp_game_info.dump_json())
                print('2')
                #tmp_player.socket_info.sendall(tmp_game_info.dump_json().encode('utf-8'))

    def load_game_rule(self):
        pass

    # 生成玩家ID
    def gen_player_id(self, _uname, _socket_info):
        tmp_id = md5manager.create_md5((_uname, _socket_info.getpeername(), time.time()))
        tmp_p = PixelFightPlayer(usr_name=_uname, login_id=tmp_id, socket=_socket_info)
        self.__add_player(tmp_p)
        # self.launch()
        return tmp_id

    def __add_player(self, _p):
        self.__player_info_list.append(_p)

    def attack_grid(self, _x, _y, _player_id):
        pass
