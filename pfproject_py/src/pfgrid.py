# !/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'Zhiquan Wang'
__date__ = '2018/7/20 22:01'


class PixelGrid(object):

    def __init__(self, _t, _a, _v):
        self.__type = _t
        self.__attribution = _a
        self.__value = _v

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, _t):
        self.__type = _t

    @property
    def attribution(self):
        return self.__attribution

    @attribution.setter
    def attribution(self, _a):
        self.__attribution = _a

    @property
    def value(self, _v):
        self.__value = _v
