#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: bustta
# @Date:   2014-12-28 14:46:24
# @Last Modified by:   bustta
# @Last Modified time: 2014-12-30 00:05:43
from django.conf.urls import patterns, url
from subscriptions.views import home, contact, privacy, subscription_list, subscription_create, subscription_detail, subscription_update, subscription_delete, subscription_delete_confirm


urlpatterns = patterns('',
    url(r'^$', home, name='home'),
    url(r'^contact/$', contact, name='contact'),
    url(r'^privacy/$', privacy, name='privacy'),
    url(r'^subscription/$', subscription_list, name='subscription_list'),
    url(r'^subscription/(?P<pk>\d+)/$', subscription_detail, name='subscription_detail'),
    url(r'^new/$', subscription_create, name='subscription_create'),
    url(r'^subscription/(?P<pk>\d+)/update/$', subscription_update, name='subscription_update'),
    url(r'^subscription/(?P<pk>\d+)/delete/$', subscription_delete, name='subscription_delete'),
    url(r'^subscription/(?P<pk>\d+)/confirm/$', subscription_delete_confirm, name='subscription_delete_confirm'),

)