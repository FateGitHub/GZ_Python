# -*- coding:utf-8 -*-
'''
@Time    : 2018/8/5 19:04
@Author  : Fate
@File    : CityModel.py 城市数据模型
'''

from app.extensions import db


# 字母模型
class Letter(db.Model):
    __tablename__ = 'letters'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    letter = db.Column(db.String(2))


# 城市数据模型
'''
  {
        "id": 3643,
        "parentId": 0,
        "regionName": "阿坝",
        "cityCode": 513200,
        "pinYin": "ABA"
      }
'''


class City(db.Model):
    __tablename__ = 'cities'
    id = db.Column(db.Integer, primary_key=True)
    regionName = db.Column(db.String(32), nullable=False)
    cityCode = db.Column(db.Integer, nullable=False)
    pinYin = db.Column(db.String(32), nullable=False)
    # 一对多
    letter_id = db.Column(db.Integer, db.ForeignKey(Letter.id))
