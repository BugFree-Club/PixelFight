# !/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'Zhiquan Wang'
__date__ = '2018/7/20 22:08'

from pfgrid import *
from pfmessage import *


class PixelMap(object):
    def __init__(self, _h, _w):
        self.__height = _h
        self.__width = _w
        self.__grid_map = [[None] * self.__width for i in range(self.__height)]

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    @property
    def grid_map(self):
        return self.__grid_map

    def __dict__(self):
        return {JsonAttribute.pfm_height: self.__height,
                JsonAttribute.pfm_width: self.__width,
                JsonAttribute.pfm_grid_map: self.__grid_map}

    def dump_json(self):
        return json.dumps(self.__dict__())

    def parse_json(self, _s):
        tmp_dict = json.loads(_s)
        self.__height = tmp_dict[JsonAttribute.pfm_height]
        self.__width = tmp_dict[JsonAttribute.pfm_width]
        self.__grid_map = tmp_dict[JsonAttribute.pfm_grid_map]
