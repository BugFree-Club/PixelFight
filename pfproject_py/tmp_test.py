# _*_coding: utf-8 _*_
import numpy as np

__author__ = 'Zhiquan Wang'
__date__ = '2018/7/24 '

import sys
import matplotlib
import matplotlib.pyplot as plt
from pfrule import PixelFightRule
from pfgrid import *
import time
import pfmap
import pfgame
import pfmessage


def scatter_plot():
    """
    scatter plot
    """
    # 打开交互模式
    plt.ion()

    # 循环
    for index in range(50):
        # 清除原有图像
        # plt.cla()

        # 设定标题等
        plt.title("动态散点图")
        plt.grid(True)

        # 生成测试数据
        point_count = 5
        x_index = np.random.random(point_count)
        y_index = np.random.random(point_count)

        # 设置相关参数
        color_list = np.random.random(point_count)

        # 画散点图
        plt.scatter(x_index, y_index, s=1000, c=color_list, marker="s")

        # 暂停
        plt.pause(0.2)

    # 关闭交互模式
    plt.ioff()

    # 显示图形
    plt.show()
    return


if __name__ == '__main__':
    scatter_plot()

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
