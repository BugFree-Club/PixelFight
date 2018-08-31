# !/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'Zhiquan Wang'
__date__ = '2018/8/26 15:37'

import matplotlib.colors
import matplotlib.pyplot as plt
import random



class VisionManager(object):

    def __init__(self, *, player_info_list, game_rule):
        self.__grid_height = game_rule.map_height
        self.__grid_width = game_rule.map_width
        self.__cube_size = 80
        self.__title = u'Pixel-Fight-Map'
        self.__color_list = [
            matplotlib.colors.to_hex([random.random(), random.random(), random.random()])
            for _ in range(len(player_info_list))]
        self.__player_info_list = player_info_list

    def activate(self):
        plt.ion()

    def deactivate(self):
        plt.ioff()

    def update(self, game_map):
        plt.cla()
        plt.title(self.__title)
        plt.xlim(0, self.__grid_width)
        plt.ylim(0, self.__grid_height)
        ax = plt.gca()
        ax.set_yticks([i for i in range(0, 30)])
        ax.set_xticks([i for i in range(0, 30)])

        plt.grid(True)
        counter = 0
        for tmp_player in self.__player_info_list:
            tmp_data = self.parse_data(tmp_player.login_id, game_map)
            plt.scatter(tmp_data[0], tmp_data[1],
                        s=self.__cube_size,
                        c=self.__color_list[counter],
                        marker="s")
            counter += 1

        plt.pause(0.1)
        # label=tmp_player.usr_name)
        # plot_list.append(tmp_plot)

    def parse_data(self, player_id, game_map):
        x_data = []
        y_data = []
        for tmp_y in range(game_map.width):
            for tmp_x in range(game_map.height):
                if game_map.grid_map[tmp_x][tmp_y].attribution == player_id:
                    x_data.append(tmp_y)
                    y_data.append(tmp_x)
        return [x_data, y_data]

    @property
    def cube_size(self):
        return self.__cube_size

    @cube_size.setter
    def cube_size(self, _size):
        self.__cube_size = _size
