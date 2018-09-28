#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
@author: ??
@file: urls.py
@time: 2018/9/28 17:23
@desc:
'''
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^article-column/$', views.article_column, name='article_column'),
]
