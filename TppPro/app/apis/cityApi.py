# -*- coding:utf-8 -*-
'''
@Time    : 2018/8/4 20:09
@Author  : Fate
@File    : cityApi.py
'''
from app.extensions import api
from app.models.CityModel import Letter, City
from flask_restful import Resource, fields, marshal_with, reqparse, marshal

# 城市
city_fields = {
    "id": fields.Integer,
    "regionName": fields.String,
    "pinYin": fields.String,
    "cityCode": fields.Integer
}
# 字母
letter_fields = {
    "A": fields.List(fields.Nested(city_fields)),
}
# 结果
result_fields = {
    "returnCode": fields.String,
    "returnValue": fields.Nested(letter_fields)
}


'''
{
  "returnCode": "0",
  "returnValue": {
    "A": [
      {
        "id": 3643,
        "parentId": 0,
        "regionName": "阿坝",
        "cityCode": 513200,
        "pinYin": "ABA"
      },
      {
        "id": 3090,
         "parentId": 0,
       "regionName": "阿克苏",
        "cityCode": 652901,
        "pinYin": "AKESU"
      }]
    }
}

'''


class CityResource(Resource):
    @marshal_with(result_fields)
    def get(self):
        returnValue = {}
        letters = Letter.query.all()
        for letter in letters:
            print(letter)
            city = City.query.filter_by(letter_id=letter.id)
            returnValue[letter.letter] = city
        # return result_fields
        return {'returnCode': "0", "returnValue": returnValue}

    def post(self):
        # 定义字母字段
        letter_fields_dynamic = {}
        returnValue = {}
        letters = Letter.query.all()
        for letter in letters:
            print(letter.id)
            city = City.query.filter_by(letter_id=letter.id)

            letter_fields_dynamic[letter.letter] = fields.List(fields.Nested(city_fields))
            returnValue[letter.letter] = city

        result_fields_dynamic = {
            "returnCode": fields.String,
            'returnValue': fields.Nested(letter_fields_dynamic)
        }

        result = marshal({'returnCode': "0", "returnValue": returnValue}, result_fields_dynamic)
        return result


print(api, '==================')
