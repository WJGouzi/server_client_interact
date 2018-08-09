#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author name__ = 'gouzi'
__create time__ = '2018/8/9'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
             ┏┓   ┏┓
            ┏┛┻━━━┛┻━━━┓
            ┃    ☃    ┃
            ┃  ┳┛  ┗┳  ┃
            ┃    ┻     ┃
            ┗━┓      ┏━┛
              ┃      ┗━━━━━━━┓
              ┃   神兽保佑    ┣┓
              ┃    永无BUG！ ┏┛
              ┗┓┓┏━━┳━┓ ┏━━━┛
               ┃┫┫    ┃┫┫
               ┗┻┛    ┗┻┛
"""
from django.shortcuts import render

def homepage(req):
    print('前端Get请求', req.GET)
    print('前端Post请求', req.POST)
    print('文件File发送', req.FILES)
    # 循环去文件
    for item in req.FILES:
        print(item)
        obj = req.FILES.get(item, None)
        f = open(obj.name, 'wb')
        for data_line in obj.chunks():
            f.write(data_line)
        f.close()


    return render(req, "homepage.html")