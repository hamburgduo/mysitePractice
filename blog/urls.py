#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
@author: ??
@file: urls.py
@time: 2018/8/16 20:31
@desc:
'''
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$',views.blog_title, name='blog_title'),
    url(r'(?P<article_id>\d)/$', views.blog_article, name='blog_article'),
]