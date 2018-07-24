# _*_coding: utf-8 _*_
__author__ = 'Zhiquan Wang'
__date__ = '2018/7/24 '

import os
from pfrule import *
if __name__ == '__main__':
    pass
    # cur_path = os.path.abspath('.')
    # cur_path = os.path.join(cur_path,'test.json')
    # cur_path = os.path.abspath('.').join('test.json')
    # with open(cur_path,'w') as f:
    #        f.wri
    tmp_rule = PixelFightRule(2,2,2,2,2,12)
    print(tmp_rule.dump_json())
    tmp_rule.load('/tmp/pycharm_project_363/test/test.json')
    print(tmp_rule.dump_json())


