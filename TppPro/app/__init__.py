# -*- coding:utf-8 -*-
'''
@Time    : 2018/8/4 19:08
@Author  : Fate
@File    : __init__.py app 初始化文件
'''
from flask import Flask
from app.config import config
from app.extensions import config_extensions
from app.views import config_blueprint
# from app.errors import config_errorhandler
import app.apis


def create_app(config_name):
    # 创建应用实例
    app = Flask(__name__)

    # 加载配置
    app.config.from_object(config.get(config_name))
    print(config.get(config_name), '======')

    # 额外初始化
    config.get(config_name).init_app(app)

    # 加载扩展
    config_extensions(app)

    # 蓝本注册
    config_blueprint(app)

    # 错误定制
    # config_errorhandler(app)

    # 返回一个app
    return app
