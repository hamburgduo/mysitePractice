#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
@author: ??
@file: forms.py
@time: 2018/9/28 17:13
@desc:
'''

from django import forms
from .models import ArticleColumn


class ArticleColumnForm(forms.ModelForm):
    class Meta:
        model = ArticleColumn
        fields = ("column",)
