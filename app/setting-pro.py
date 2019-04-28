#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/28 12:39 PM
# @Author  : Nikky
# @Site    : 
# @File    : setting-pro.py

'''
常规信息配置
'''
DEBUG     = True
PAGE_SIZE = 15

'''
数据库的配置
'''
DB_HOST  = '127.0.0.1'
DB_PORT  = 3306
DB_USER  = 'root'
DB_PWD   = '123456'
DB_NAME  = 'flask'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4'.format(DB_USER, DB_PWD, DB_HOST, DB_PORT, DB_NAME)
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True

'''
缓存信息配置
'''
REDIS_HOST  = '47.100.47.188'
REDIS_PORT  = 6379
REDIS_DB    = 0
REDIS_PWD   = 'lm123456'
REDIS_EX    = 5 * 60
REDIS_EX_SHOPPING = 10 * 60