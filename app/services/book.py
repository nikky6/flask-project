#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/27 11:24 PM
# @Author  : Nikky
# @Site    : 
# @File    : book.py
from app.spider.book import Book
from flask import jsonify, Blueprint
from flask import request
from app.validators.book import SearchForm
from . import book
from app.models.book import BookModel


@book.route('/book/search')
def hell():
    '''
    isbn
    http://127.0.0.1:5001/book/search?q=9787501524044&page=1
    http://127.0.0.1:5001/book/search?q=%E8%81%8A%E6%96%8B&page=1
    :param name:
    :return:
    '''
    search_form = SearchForm(request.args)
    check_form = search_form.validate()
    if not check_form:
        return jsonify(
            search_form.errors
        )
    q = search_form.q.data
    result = Book.search_by_keyword(q, search_form.page.data)
    return jsonify(result)
