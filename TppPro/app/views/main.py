# -*- coding:utf-8 -*-
'''
@Time    : 2018/8/4 19:36
@Author  : Fate
@File    : main.py app主视图
'''
from flask import Blueprint, render_template
from app.models.userModel import User
from app.models.CityModel import Letter,City
from app.email import async_send_mail_util

# 创建视图对象
main = Blueprint('main', __name__)


# 首页
@main.route('/index/')
def index():
    async_send_mail_util(subject='用户账号激活', recipients=['1446723956@qq.com'], emailTmp='userRegion')

    return render_template('base.html')
