# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# create data : 2018/03/26
# author : Simin.Zhan


from hashlib import md5
import logging


def create_md5(_content):
    md5_obj = md5()
    if isinstance(_content, tuple):
        for _c in _content:
            md5_obj.update(str(_c).encode('utf-8'))
    elif isinstance(_content, str):
        md5_obj.update(_content.encode('utf-8'))
    md5_obj.update('pf_salt.'.encode('utf-8'))
    return md5_obj.hexdigest()
