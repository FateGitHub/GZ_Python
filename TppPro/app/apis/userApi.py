# -*- coding:utf-8 -*-
'''
@Time    : 2018/8/6 19:28
@Author  : Fate
@File    : userApi.py
'''
import hashlib
import uuid
from flask_restful import Resource, reqparse, fields, marshal_with
from app.extensions import db, cache
from app.email import async_send_mail_util

# 注册参数
from app.models import User

user_region_parser = reqparse.RequestParser()
user_region_parser.add_argument('username', type=str, required=True, help='请输入用户名')
user_region_parser.add_argument('password', type=str, required=True, help='请输入密码')
user_region_parser.add_argument('email', type=str, required=True, help='请输入邮箱')


# 密码加密
def generate_password(password):
    hash = hashlib.md5()
    hash.update(password.encode('utf-8'))
    return hash.hexdigest()


# 返回字段
user_fields = {
    "u_name": fields.String,
    "u_email": fields.String,
    "u_token": fields.String
}

result_fields = {
    "returnCode": fields.String,
    "returnValue": fields.Nested(user_fields),
    "msg": fields.String
}


class UserResource(Resource):
    # 查找
    def get(self):
        return {'msg': 'OK'}

    # 注册
    @marshal_with(result_fields)
    def post(self):
        # 获取注册用户信息
        agrs = user_region_parser.parse_args()
        u_name = agrs.get('username')
        u_password = agrs.get('password')
        u_password = generate_password(u_password)
        u_email = agrs.get('email')
        u_token = uuid.uuid4()
        print(u_name, u_password, u_token)
        # 插入
        try:
            user = User(u_name=u_name, u_password=u_password,
                        u_email=u_email, u_token=u_token)

            db.session.add(user)
            db.session.commit()
        except Exception as e:
            print(e)

            return {"returnCode": "406", "msg": "用户注册失败"}

        # 设置缓存
        cache.set(u_token, user.id, timeout=60 * 60)
        async_send_mail_util(subject='用户账号激活', recipients=[u_email], emailTmp='userRegion', username=u_name,
                             active_url="http://localhost:5000/activation/?u_token=" + str(u_token))

        # 返回
        return {"returnCode": "201", "msg": "用户注册成功", "returnValue": user}

    # 修改
    def patch(self):
        pass
