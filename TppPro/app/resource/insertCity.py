# -*- coding:utf-8 -*-
'''
@Time    : 2018/8/5 19:07
@Author  : Fate
@File    : insertCity.py 插入数据库
'''
import json
import pymysql

mysqlConn = pymysql.connect(host='127.0.0.1',
                            user='root',
                            password="123456",
                            database='flask',
                            charset='utf8')

cursor = mysqlConn.cursor()

# 读取json数据
with open('city.json', 'r', encoding='utf-8') as f:
    city_json = json.load(f)
    print(city_json)

    city_value = city_json['returnValue']
    letters = city_value.keys()
    for letter in letters:
        print(letter)
        # 插入字母表
        # letter_sql = "INSERT INTO letters(letter) VALUES ('{}')".format(letter)
        # mysqlConn.begin()
        # cursor.execute(letter_sql)
        # mysqlConn.commit()

        city_list = city_value[letter]
        for city in city_list:

            # 查询letter_id
            cursor.execute("SELECT id FROM letters WHERE letter='{}'".format(letter))
            letter_id = cursor.fetchone()[0]
            print(letter_id)

            print(city)

            regionName = city.get("regionName")
            id = city.get("id")
            cityCode = city.get("cityCode")
            pinYin = city.get("pinYin")
            # 插入数据   需要额外关联的字母字段，字母所在表中的id
            mysqlConn.begin()
            cursor.execute(
                "INSERT INTO cities (id, regionName, cityCode, pinYin, letter_id) VALUES ({}, '{}', {}, '{}', {});".format(
                    id, regionName, cityCode, pinYin, letter_id))
            mysqlConn.commit()
