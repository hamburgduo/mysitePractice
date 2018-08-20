#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
@author: ??
@file: forms.py
@time: 2018/8/20 21:12
@desc:
'''
from django import forms
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)