#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/28 4:26 PM
# @Author  : Nikky
# @Site    : 
# @File    : book.py
from sqlalchemy import Column, Integer, String
from . import db


class BookModel(db.Model):

    __tablename__ = 'book'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    content = Column(String(200), nullable=False, unique=True)
    isbn = Column(String(50), nullable=False, default='')
