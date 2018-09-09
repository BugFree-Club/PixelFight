# !/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'Zhiquan Wang'
__date__ = '2018/8/15 10:44'


class MessageType(object):
    login_request = u'LoginRequest'
    login_reply = u'LoginReply'
    attack_request = u'AttackRequest'
    attack_reply = u'AttackReply'
    game_info = u'GameInfo'


class JsonAttribute(object):
    msg_type = u'msg_type'
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
    gi_per_pos = u'per_pos'

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

    # pfGrid
    pfg_type = u'type'
    pfg_attribution = u'attribution'
    pfg_value = u'value'
