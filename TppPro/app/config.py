# -*- coding:utf-8 -*-
'''
@Time    : 2018/8/4 19:08
@Author  : Fate
@File    : config.py 配置文件
'''
import os

# 基目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# 基本配置
class Config(object):
    # 秘钥
    SECRET_KEY = os.environ.get('SECRET_KEY')

    # 数据库配置
    # 忽略警告
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 自动提交
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    # 邮箱发送
    MAIL_SERVER = 'smtp.aliyun.com'
    MAIL_USERNAME = 'fate9527@aliyun.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'Changeme_123'

    # 额外初始化
    @staticmethod
    def init_app(app):
        pass


# 开发环境配置
class DevelopmentConfig(Config):
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'DevDB.sqlite')
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@127.0.0.1:3306/flask'

# 测试环境配置
class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'TestDB.sqlite')


# 发布环境配置
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'ProDB.sqlite')


# 配置字典
config = {
    'development': DevelopmentConfig,
    'test': TestConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
