# !/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'Zhiquan Wang'
__date__ = '2018/8/3 20:23'


class PixelFightPlayer(object):
    def __init__(self, *, usr_name=None, login_id=None, socket=None):
        self.__usr_name = usr_name
        self.__login_id = login_id
        self.__last_attack_grid = [0, 0]
        self.__socket_info = socket

    @property
    def usr_name(self):
        return self.__usr_name

    @usr_name.setter
    def usr_name(self, _u):
        self.__usr_name = _u

    @property
    def login_id(self):
        return self.__login_id

    @property
    def socket_info(self):
        return self.__socket_info

    @property
    def last_attack_grid(self):
        return self.__last_attack_grid

    @last_attack_grid.setter
    def last_attack_grid(self, _vec):
        self.__last_attack_grid = _vec
