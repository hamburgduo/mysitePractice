#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
@author: ??
@file: urls.py
@time: 2018/8/20 21:08
@desc:
'''
from django.conf.urls import url
from . import views
from django.conf import settings

urlpatterns = [
    url(r'^login/$', views.user_login, name='user_login'),
]
