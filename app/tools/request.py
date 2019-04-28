#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/27 11:46 AM
# @Author  : Nikky
# @Site    : 
# @File    : request.py

import requests


class Request:

    @staticmethod
    def get(url, return_json=True):
        '''
        发送get请求
        :param url:
        :param return_json:
        :return:
        '''
        r = requests.get(url)
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text

    @staticmethod
    def post(url, return_json=True):
        '''
        发送post请求
        :param url:
        :param return_json:
        :return:
        '''
        r = requests.post(url)
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text


if __name__ == '__main__':
    request = Request()
    print(request.get('http://ip.taobao.com/service/getIpInfo.php?ip=102.113.115.114'))
