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
from django.contrib.auth import views as auth_views
from django.conf import settings

urlpatterns = [
    url(r'^login/$', views.user_login, name='user_login'),
    url(r'^new-login/$', auth_views.login, {'template_name': 'account/login.html'}),
    url(r'^logout/$', auth_views.logout, {'template_name': 'account/logout.html'}, name='user_logout'),
    url(r'^register/$', views.register, name='user_register'),
    url(r'^password-change/$', auth_views.password_change,
        {'template_name': 'account/password_change_form.html','post_change_redirect': '/account/password-change-done'},
        name='password_change'),
    url(r'^password-change-done/$', auth_views.password_change_done,
        {'template_name': 'account/password_change_done.html'}, name='password_change_done'),
]
