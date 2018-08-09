# -*- coding:utf-8 -*-
'''
@Time    : 2018/8/6 21:22
@Author  : Fate
@File    : activationApi.py
'''
from app.models.userModel import User
from app.extensions import cache, db
from flask_restful import Resource, fields, marshal_with, reqparse, marshal

parser = reqparse.RequestParser()
# 获取u_token
parser.add_argument("u_token", type=str)


# 用户激活
class ActivationResource(Resource):
    def get(self):
        args = parser.parse_args()
        # 获取u_token
        u_token = args.get('u_token')
        print(u_token)

        # 根据u_token查找用户
        user_id = cache.get(u_token)

        if user_id:
            # 根据id查找用户
            user = User.query.get(user_id)
            # 修改用户状态
            user.is_active = True
            # 提交
            db.session.add(user)
            db.session.commit()
            return {"msg": "ok，已成功激活"}

        return {"msg": "已过期，请重新申请激活邮件"}
