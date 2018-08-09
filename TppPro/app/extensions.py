# -*- coding:utf-8 -*-
'''
@Time    : 2018/8/4 19:07
@Author  : Fate
@File    : extensions.py 扩展文件
'''

from flask_mail import Mail
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
from flask_cache import Cache

# 创建扩展对象
mail = Mail()
db = SQLAlchemy()
bootstrap = Bootstrap()
api = Api()
cache = Cache(config={'CACHE_TYPE': 'redis'})


# 初始化
def config_extensions(app):
    mail.init_app(app)
    db.init_app(app)
    bootstrap.init_app(app)
    api.init_app(app)
    cache.init_app(app)


class C(Resource):
    def get(self):
        return {'msg': 'OKKKK'}


api.add_resource(C, '/ccc/')
