# !/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'Zhiquan Wang'
__date__ = '2018/7/21 22:12'

import json


class LoginRequest(object):
    def __init__(self,*, _u_name,json_info = None):
        if json_info is None:
            self.__msg_type = MessageType.login_request
            self.__usr_name = _u_name
        else:
            tmp_dic = json.loads(json_info)
            self.__msg_type = tmp_dic[JsonAttribute.]


class PlayerCommand(object):
    def __init__(self, _x, _y):
        self.__msg_type = MessageType.player_command
        self.__player_id = None
        self.__target_x = _x
        self.__target_y = _y

    def __dict__(self):
        return {JsonAttribute.msg_type: self.__msg_type,
                JsonAttribute.pc_player_id: self.__player_id,
                JsonAttribute.pc_target_x: self.__target_x,
                JsonAttribute.pc_target_y: self.__target_y}

    def dump_json(self):
        return json.dumps(self.__dict__())

    def parse_json(self, _s):
        tmp_dic = json.loads(_s)
        self.__msg_type = tmp_dic[JsonAttribute.msg_type]
        self.__target_x = tmp_dic[JsonAttribute.pc_target_x]
        self.__target_y = tmp_dic[JsonAttribute.pc_target_y]

    # @property
    # def target_x(self):
    #     return self.__target_x
    #
    # @target_x.setter
    # def target_x(self, _v):
    #     self.__target_x = _v


class GameInfo(object):
    def __init__(self, _m, _r):
        self.__msg_type = MessageType.game_info
        self.__map_info = _m
        self.__round = _r

    def __dict__(self):
        return {JsonAttribute.msg_type: self.__msg_type,
                JsonAttribute.gi_map_info: self.__map_info,
                JsonAttribute.gi_round: self.__round}

    def dump_json(self):
        return json.dumps(self.__dict__())

    def parse_json(self, _s):
        tmp_dic = json.loads(_s)
        self.__msg_type = tmp_dic[JsonAttribute.msg_type]
        self.__map_info = tmp_dic[JsonAttribute.gi_map_info]
        self.__round = tmp_dic[JsonAttribute.gi_round]


def get_msg_type(self, _s):
    return json.load(_s)[JsonAttribute.msg_type]


class MessageType(object):
    login_request = u'LoginRequest'
    player_command = u'PlayerCommand'
    game_info = u'GameInfo'


class JsonAttribute(object):
    msg_type = 'msg_type'
    # LoginRequest
    lr_usr_name = u'usr_name'

    # LoginReply
    lre_loginid = u'login_id'

    # PlayCommand 
    pc_player_id = u'player_id'
    pc_target_x = u'target_x'
    pc_target_y = u'target_y'

    # GameInfo
    gi_map_info = u'map_info'
    gi_round = u'round'

    # pfRule
    pfr_max_round = u'max_round'
    pfr_map_height = u'map_height'
    pfr_map_width = u'map_width'
    pfr_player_num = u'player_num'
    pfr_empty_grid_time = u'empty_grid_time'
    pfr_player_grid_time = u'player_grid_time'
