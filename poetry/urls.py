# -*- encoding: utf-8 -*-
"""
@File    : urls.py
@Time    : 2024/8/29 16:10
@Author  : nanjiang.xie
@Email   : xie672088678@163.com
@Software: PyCharm
"""
from django.urls import path
from .views import poem_list, poem_create, poem_update, poem_delete

urlpatterns = [
    path('', poem_list, name='poem_list'),
    path('poem/create/', poem_create, name='poem_create'),
    path('poem/update/<int:poem_id>/', poem_update, name='poem_update'),
    path('poem/delete/<int:poem_id>/', poem_delete, name='poem_delete'),
]
