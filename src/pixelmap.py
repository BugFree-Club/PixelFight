# !/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'Zhiquan Wang'
__date__ = '2018/7/20 22:08'

from grid import *


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
