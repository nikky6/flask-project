#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/27 11:24 PM
# @Author  : Nikky
# @Site    : 
# @File    : yushu_book.py
from app.tools.request import Request
from flask import current_app


class Book:
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    @classmethod
    def search_by_isbn(cls, isbn):
        url = cls.isbn_url.format(isbn)
        result = Request.get(url)
        return result

    @classmethod
    def search_by_keyword(cls, keyword, page):
        url = cls.keyword_url.format(keyword, current_app.config['PAGE_SIZE'],
                                     (page - 1) * current_app.config['PAGE_SIZE'])
        result = Request.get(url)
        return result
