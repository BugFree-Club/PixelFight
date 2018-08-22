# !/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'Zhiquan Wang'
__date__ = '2018/7/20 22:01'

import taginfo


class GridTag(object):
    type_land = 'land'
    attribution_empty = 'empty'


class PixelGrid(object):

    def __init__(self, *, ptype=GridTag.type_land, attribution='empty', value=1):
        self.__type = ptype
        self.__attribution = attribution
        self.__value = value

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
    def value(self):
        return self.__value

    @value.setter
    def value(self, _v):
        self.__value = _v

    def __dict__(self):
        return {taginfo.JsonAttribute.pfg_type: self.__type,
                taginfo.JsonAttribute.pfg_attribution: self.__attribution,
                taginfo.JsonAttribute.pfg_value: self.value}
