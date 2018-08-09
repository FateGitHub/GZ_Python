# -*- coding:utf-8 -*-
'''
@Time    : 2018/8/4 19:05
@Author  : Fate
@File    : __init__.py.py
'''
from .main import main

DEFAULT_BLUEPRINT = (
    (main, ''),
)


def config_blueprint(app):
    for blueprint, prefix in DEFAULT_BLUEPRINT:
        # 注册蓝本
        app.register_blueprint(blueprint, url_prefix=prefix)
