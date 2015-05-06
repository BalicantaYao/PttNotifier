#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: bustta
# @Date:   2014-12-28 14:46:24
# @Last Modified by:   bustta
# @Last Modified time: 2015-05-06 00:15:11
from django.conf.urls import patterns, url
from subscriptions.views import terms_and_condictions, subscription_list, subscription_create
from subscriptions.views import subscription_detail, subscription_update
from subscriptions.views import subscription_delete, subscription_delete_confirm
from subscriptions.views import get_notifications_by_id_from_client, mark_as_read_and_del_in_redis_on_click
from subscriptions.views import notification_list

urlpatterns = patterns(
    '',
    url(r'^$', 'subscriptions.views.home', name='home'),
    url(r'^contact/$', 'subscriptions.views.contact', name='contact'),
    url(r'^comments/$', 'subscriptions.views.comments', name='comments'),
    url(r'^privacy/$', 'subscriptions.views.privacy', name='privacy'),
    url(r'^terms_and_condictions/$', terms_and_condictions, name='terms_and_condictions'),
    url(r'^subscriptions/$', subscription_list, name='subscription_list'),
    url(r'^subscriptions/(?P<pk>\d+)/$', subscription_detail, name='subscription_detail'),
    url(r'^new/$', subscription_create, name='subscription_create'),
    url(r'^subscriptions/(?P<pk>\d+)/update/$', subscription_update, name='subscription_update'),
    url(r'^subscriptions/(?P<pk>\d+)/delete/$', subscription_delete, name='subscription_delete'),
    url(r'^subscriptions/(?P<pk>\d+)/confirm/$',
        subscription_delete_confirm, name='subscription_delete_confirm'),
    url(r'^rtnotifications/$',
        get_notifications_by_id_from_client, name='get_notifications_by_id_from_client'),
    url(r'^rtnotifications/update/$',
        mark_as_read_and_del_in_redis_on_click, name='mark_as_read_and_del_in_redis_on_click'),
    url(r'^notifications/$', notification_list, name='notification_list'),

)
