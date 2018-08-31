# !/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'Zhiquan Wang'
__date__ = '2018/8/27 17:21'

import random


def attack(game_info):
    print(game_info.per_pos)
    x_offset = random.randint(-1, 1)
    y_offset = random.randint(-1, 1)
    if x_offset != 0 and y_offset != 0:
        if random.randint(-1, 1) < 0:
            x_offset = 0
        else:
            y_offset = 0

    attack_pos = [game_info.per_pos[0] + x_offset, game_info.per_pos[1] + y_offset]
    # beign
    # your codes here

    # end
    return attack_pos
