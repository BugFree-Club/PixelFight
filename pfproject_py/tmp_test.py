# _*_coding: utf-8 _*_

__author__ = 'Zhiquan Wang'
__date__ = '2018/7/24 '

import sys
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from pfrule import PixelFightRule
from pfgrid import *
import time
import pfmap
import pfgame
import pfmessage
import random
import pfrule

def scatter_plot():
    """
    scatter plot
    """
    # 打开交互模式
    plt.ion()

    point_count = 5
    # 清除原有图像
    plt.cla()

    # 设定标题等
    plt.title("Pixel-Fight-Map")
    plt.xlim(0, 30)
    plt.ylim(0, 30)
    ax = plt.gca()
    ax.set_yticks([i for i in range(0, 30)])
    ax.set_xticks([i for i in range(0, 30)])
    plt.grid(True)

    # 生成测试数据

    x_index = [1.5, 22.5, 5.5, 4.5, 9.5]
    y_index = [1.5, 2.5, 2.5, 5.5, 5.5]

    # 设置相关参数
    color_list = [random.random() for _ in range(5)]
    print(color_list)

    # 画散点图
    plt.scatter(x_index, y_index, s=80, c=[0.3, 0.6, 0.3], marker="s", label='123')
    matplotlib.pyplot.gcf().set_size_inches(5, 5)
    # 暂停
    plt.pause(1)

    # 关闭交互模式
    plt.ioff()

    # 显示图形
    plt.show()
    return


if __name__ == '__main__':
    tmp_rule = pfrule.PixelFightRule()
    tmp_rule.output('standard-rule.txt')
    # tmp_map = pfmap.PixelMap(map_width=30, map_height=30)
    #
    # for i in range(5):
    #     tmp_map.grid_map[i][0].value += 1
    #
    #     tmp_map.grid_map[2][0].value = 4
    #
    # for i in range(5):
    #     print(tmp_map.grid_map[i][0].value)
    # for i in range(5):
    #     print(tmp_map.grid_map[i][1].value)
    # for i in range(5):
    #     print(tmp_map.grid_map[0][i].value)


    # scatter_plot()
# [print(i) for i in range(10)]
#  tmp_map = pfmap.PixelMap(map_width=10,map_height=10)
#  print(tmp_map.dump_json())
#  tmp_msg = pfmessage.GameInfo(pf_map=tmp_map)
#  print(tmp_msg.dump_json())

# tmp_game = pfgame.PixelFightGame()
# tmp_game.add_player('123')
# tmp_game.launch()
# tmp_rule = PixelFightRule(2, 2, 2, 2, 2, 12)
# print(tmp_rule.dump_json())
# tmp_rule.load('/tmp/pycharm_project_363/test/test.json')
# print(tmp_rule.dump_json())
# tmp_grid1 = PixelGrid(1, 1, 1)
# tmp_grid2 = PixelGrid(2, 2, 2)
# tmp_grid3 = PixelGrid(1, 1, 1)
# tmp_list = []
# tmp_list.append(tmp_grid1)
# tmp_list.append(tmp_grid2)
# tmp_list.append(tmp_grid3)
# print(len(tmp_list))
# tmp_list.remove(tmp_grid1)
# print(len(tmp_list))
