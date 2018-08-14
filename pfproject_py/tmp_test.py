# _*_coding: utf-8 _*_
__author__ = 'Zhiquan Wang'
__date__ = '2018/7/24 '

import sys
from pfrule import PixelFightRule
from pfgrid import *
import time

if __name__ == '__main__':
    # tmp_rule = PixelFightRule(2, 2, 2, 2, 2, 12)
    # print(tmp_rule.dump_json())
    # tmp_rule.load('/tmp/pycharm_project_363/test/test.json')
    # print(tmp_rule.dump_json())
    tmp_grid1 = PixelGrid(1, 1, 1)
    tmp_grid2 = PixelGrid(2, 2, 2)
    tmp_grid3 = PixelGrid(1, 1, 1)
    tmp_list = []
    tmp_list.append(tmp_grid1)
    tmp_list.append(tmp_grid2)
    tmp_list.append(tmp_grid3)
    print(len(tmp_list))
    tmp_list.remove(tmp_grid1)
    print(len(tmp_list))
