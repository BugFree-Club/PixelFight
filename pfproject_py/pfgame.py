# !/usr/bin/env python3
# -*- coding:utf-8 -*-
import random

__author__ = 'Zhiquan Wang'
__date__ = '2018/7/20 22:30'

from pfmap import *
from pfrule import *
from pfplayer import *
from pfmessage import *
import time
import md5manager
from pfvisionmanager import *


class PixelFightGame(object):

    def __init__(self):
        self.__game_rule = PixelFightRule(_mw=30, _mh=30)
        self.__round_counter = 0
        self.__game_ratio = 0
        self.__player_info_list = []
        self.__pixel_map = PixelMap(map_height=self.__game_rule.map_height, map_width=self.__game_rule.map_width)
        self.__per_pos_list = []
        self.__vision_manager = None
        self.__is_pause = False
        self.__is_ready = False

    # 开始比赛,每回合轮流向玩家发送地图信息,并接收玩家攻击坐标
    def launch(self):
        print('System Waiting')
        while self.__is_ready is False:
            pass

        self.init_map()
        self.init_birthplace()
        print('Game Launched')
        self.__vision_manager = VisionManager(player_info_list=self.__player_info_list,
                                              game_rule=self.__game_rule)
        self.__vision_manager.activate()
        self.__vision_manager.update(self.pixel_map)
        for tmp_i in range(self.__game_rule.max_round):
            self.__round_counter = tmp_i
            for tmp_player in self.__player_info_list:
                while self.__is_pause:
                    pass
                tmp_game_info = GameInfo(pf_map=self.__pixel_map,
                                         per_pos=tmp_player.last_attack_grid,
                                         pf_round=self.__round_counter)
                print(tmp_game_info.dump_json())
                self.__vision_manager.update(self.__pixel_map)
                tmp_player.socket_info.sendall(tmp_game_info.dump_json().encode('utf-8'))
                self.__is_pause = True

    # 生成玩家ID
    def gen_player_id(self, _uname, _socket_info):
        if len(self.__player_info_list) >= self.__game_rule.player_num:
            return '0'
        tmp_id = md5manager.create_md5((_uname, _socket_info.getpeername(), time.time()))
        tmp_p = PixelFightPlayer(usr_name=_uname, login_id=tmp_id, socket=_socket_info)
        self.add_player(tmp_p)
        # self.launch()
        return tmp_id

    # 添加玩家
    def add_player(self, _p):
        if len(self.__player_info_list) < self.game_rule.player_num:
            self.__player_info_list.append(_p)
        return

    # 初始化地图
    def init_map(self):
        tmp_grid = PixelGrid(value=self.__game_rule.empty_grid_time)
        [[self.__pixel_map.set_grid([x, y], tmp_grid) for x in range(0, self.__game_rule.map_width)] for y in
         range(0, self.__game_rule.map_height)]

    # 初始化玩家出生地
    def init_birthplace(self):
        for tmp_player in self.__player_info_list:
            tmp_vec = [random.randint(0, self.__game_rule.map_width - 1),
                       random.randint(0, self.__game_rule.map_height - 1)]
            tmp_grid = PixelGrid(ptype=GridTag.type_land,
                                 attribution=tmp_player.login_id,
                                 value=self.game_rule.player_grid_time)
            tmp_player.last_attack_grid = tmp_vec
            self.pixel_map.set_grid(tmp_vec, tmp_grid)

    # 攻击网格
    def attack_grid(self, _x, _y, _player_id):
        print(_x,_y)
        tmp_grid = self.__pixel_map.grid_map[_x][_y]
        # 判断攻击网格是否合法
        if self.attack_illegal(_x, _y, _player_id) is False:
            for tmp_player in self.__player_info_list:
                if tmp_player.login_id == _player_id:
                    self.attack_illegal(tmp_player.last_attack_grid[0], tmp_player.last_attack_grid[1], _player_id)
                    return
            return
        # 攻击己方网格时:加固
        if tmp_grid.attribution == _player_id:
            tmp_grid.value += 1
            self.__pixel_map.grid_map[_x][_y] = tmp_grid
            return
        # 攻击非己方网格时:使其生命值减一
        tmp_grid.value -= 1
        if tmp_grid.value <= 0:
            tmp_grid.attribution = _player_id
            tmp_grid.value = self.game_rule.player_grid_time
        self.__pixel_map.grid_map[_x][_y] = tmp_grid

    def attack_illegal(self, _x, _y, _player_id):
        tmp_grid = self.__pixel_map.grid_map[_x][_y]
        if tmp_grid.attribution == _player_id:
            return True
        dirs = [[-1, 0], [0, 1], [0, 1], [-1, 0]]
        for tmp_dir in dirs:
            tmp_target = [_x + tmp_dir[0], _y + tmp_dir[1]]
            if tmp_target[0] < 0 or tmp_target[1] < 0:
                continue
            if self.__pixel_map.grid_map[tmp_target[0]][tmp_target[1]].attribution == _player_id:
                return True

        return False

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

    @property
    def is_ready(self):
        return self.__is_ready

    @is_ready.setter
    def is_ready(self, _flag):
        self.__is_ready = _flag

    def load_game_rule(self):
        pass
