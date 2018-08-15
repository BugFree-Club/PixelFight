# !/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'Zhiquan Wang'
__date__ = '2018/7/21 22:12'

import json
import pfmap

class LoginRequest(object):
    def __init__(self, *, uname=None, json_info=None):
        if json_info is None:
            self.__msg_type = MessageType.login_request
            self.__usr_name = uname
        else:
            self.parse_json(json_info)

    @property
    def usr_name(self):
        return self.__usr_name

    @usr_name.setter
    def usr_name(self, _uname):
        self.__usr_name = _uname

    @property
    def msg_type(self):
        return self.__msg_type

    def __dict__(self):
        return {JsonAttribute.msg_type: self.__msg_type, JsonAttribute.lr_usr_name: self.__usr_name}

    def dump_json(self):
        return json.dumps(self.__dict__())

    def parse_json(self, _s):
        tmp_dic = json.loads(_s)
        self.__msg_type = tmp_dic[JsonAttribute.msg_type]
        self.__usr_name = tmp_dic[JsonAttribute.lr_usr_name]


class LoginReply(object):
    def __init__(self, *, id=None, json_info=None):
        if json_info is None:
            self.__msg_type = MessageType.login_reply
            self.__login_id = id
        else:
            self.parse_json(json_info)

    @property
    def login_id(self):
        return self.__login_id

    @login_id.setter
    def login_id(self, _id):
        self.__login_id = _id

    def __dict__(self):
        return {JsonAttribute.msg_type: self.__msg_type, JsonAttribute.lre_login_id: self.__login_id}

    def dump_json(self):
        return json.dumps(self.__dict__())

    def parse_json(self, _s):
        tmp_dic = json.loads(_s)
        self.__msg_type = tmp_dic[JsonAttribute.msg_type]
        self.__login_id = tmp_dic[JsonAttribute.lre_login_id]


class AttackRequest(object):
    def __init__(self, *, x=None, y=None, json_info=None):
        if json_info is None:
            self.__msg_type = MessageType.attack_request
            self.__target_x = x
            self.__target_y = y
            self.__player_id = None
        else:
            self.parse_json(json_info)

    @property
    def x(self):
        return self.__target_x

    @property
    def y(self):
        return self.__target_y

    @property
    def player_id(self):
        return self.__player_id

    def __dict__(self):
        return {JsonAttribute.msg_type: self.__msg_type,
                JsonAttribute.ar_player_id: self.__player_id,
                JsonAttribute.ar_target_x: self.__target_x,
                JsonAttribute.ar_target_y: self.__target_y}

    def dump_json(self):
        return json.dumps(self.__dict__())

    def parse_json(self, _s):
        tmp_dic = json.loads(_s)
        self.__msg_type = tmp_dic[JsonAttribute.msg_type]
        self.__target_x = tmp_dic[JsonAttribute.ar_target_x]
        self.__target_y = tmp_dic[JsonAttribute.ar_target_y]


class AttackReply(object):
    def __init__(self, *, is_suc=True, json_info=None):
        if json_info is None:
            self.__msg_type = MessageType.attack_reply
            self.__is_suc = is_suc
        else:
            self.parse_json(json_info)

    @property
    def is_suc(self):
        return self.__is_suc

    def __dict__(self):
        return {JsonAttribute.msg_type: self.__msg_type,
                JsonAttribute.ap_is_suc: self.__is_suc}

    def dump_json(self):
        return json.dumps(self.__dict__())

    def parse_json(self, _s):
        tmp_dic = json.loads(_s)
        self.__msg_type = tmp_dic[JsonAttribute.msg_type]
        self.__is_suc = tmp_dic[JsonAttribute.ap_is_suc]


class GameInfo(object):
    def __init__(self, *, pf_map=pfmap.PixelMap(), pf_round=None, json_info=None):
        if json_info is None:
            self.__msg_type = MessageType.game_info
            self.__map_info = pf_map
            self.__round = pf_round
        else:
            self.parse_json(json_info)

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


def get_msg_type(_s):
    return json.loads(_s)[JsonAttribute.msg_type]


class MessageType(object):
    login_request = u'LoginRequest'
    login_reply = u'LoginReply'
    attack_request = u'AttackRequest'
    attack_reply = u'AttackReply'
    game_info = u'GameInfo'


class JsonAttribute(object):
    msg_type = 'msg_type'
    # LoginRequest
    lr_usr_name = u'usr_name'

    # LoginReply
    lre_login_id = u'login_id'

    # AttackRequest
    ar_player_id = u'player_id'
    ar_target_x = u'target_x'
    ar_target_y = u'target_y'

    # AttackReply
    ap_is_suc = u'is_suc'

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

    # pfMap
    pfm_height = u'height'
    pfm_width = u'width'
    pfm_grid_map = u'grid_map'
