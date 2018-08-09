# -*- coding:utf-8 -*-
'''
@Time    : 2018/8/4 19:07
@Author  : Fate
@File    : email.py 邮箱发送
'''
from flask import current_app, render_template
import threading
from app.extensions import mail
from flask_mail import Message


# 异步发送邮件
def async_send(app, msg):
    # 通过with 管理线程
    with app.app_context():
        mail.send(msg)


def async_send_mail_util(subject, recipients, emailTmp, **kwargs):
    # 获取当前app

    app = current_app._get_current_object()
    # print(app.config['MAIL_USERNAME'])
    msg = Message(subject=subject,
                  recipients=recipients,
                  sender=app.config['MAIL_USERNAME'])

    # 使用模板发送
    msg.html = render_template("email/" + emailTmp + '.html', **kwargs)
    mail.send(msg)
    # 创建一条线程
    # t = threading.Thread(target=async_send, args=(app, msg), name='邮箱线程')
    #
    # # 开启
    # t.start()


