#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/28 1:38 PM
# @Author  : Nikky
# @Site    : 
# @File    : book.py
from wtforms import Form, StringField, IntegerField
from wtforms.validators import DataRequired, NumberRange


class SearchForm(Form):
    q = StringField(validators=[
        DataRequired(message="q为必填参数"),
    ])
    page = IntegerField(validators=[
        NumberRange(min=1, max=999, message='page范围0-999之间')
    ], default=1)
