# -*- coding:utf-8 -*-
'''
@Time    : 2018/8/4 20:02
@Author  : Fate
@File    : userModel.py 用户数据模板
'''

from app.extensions import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 用户名
    u_name = db.Column(db.String(32), unique=True)
    # 密码
    u_password = db.Column(db.String(256))
    # 邮箱
    u_email = db.Column(db.String(64), unique=True)
    # 是否激活
    is_active = db.Column(db.Boolean, default=False)
    # token
    u_token = db.Column(db.String(256))
