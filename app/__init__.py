#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/28 12:41 PM
# @Author  : Nikky
# @Site    : 
# @File    : __init__.py

from flask import Flask
from app.services.book import book
from app.models import db


def create_app():
    '''
    create_app
    :return:
    '''
    app = Flask(__name__)
    # config
    app.config.from_object('app.setting')
    # blueprint
    regiest_blueprint(app)
    # init_app
    db.init_app(app)
    db.create_all(app=app)
    return app


def regiest_blueprint(app):
    '''
    regiest_blueprint
    :param app:
    :return:
    '''
    app.register_blueprint(book)
