#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: bustta
# @Date:   2015-01-26 23:00:17
# @Last Modified by:   bustta
# @Last Modified time: 2015-02-01 03:02:25
from SubscriptionRepo import SubscriptionRepo
from BaseAgent import BaseAgent
from Notification import Notification

dao = SubscriptionRepo()
subs = dao.get_all_user_subscription()

agent = BaseAgent('BuyTogether')
all_entries = agent.get_entries_after_last_fetch()

match_list = []
for target in subs:
    match_list_for_each_person = []
    for item in all_entries:
        is_all_kw_match = True
        for kw in target['kw_list']:
            is_all_kw_match &= (kw in item['topic'])

        if is_all_kw_match:
            match_obj = item
            match_obj['kw_list'] = target['kw_list']
            match_list_for_each_person.append(match_obj)

    if len(match_list_for_each_person) > 0:
        match_set = {}
        match_set[target['user_mail']] = match_list_for_each_person
        match_list.append(match_set)

print("\nmatch: {0}\n".format(match_list))
for send_target in match_list:
    for key in send_target.keys():
        values = send_target[key]
        if len(values) > 0:
            mail_content = ''
            subject = "關鍵字配對成功：{0}".format(', '.join(values[0]['kw_list']))
            for each_match_subscription in values:
                mail_content += "作者： {0}\n文章：{1}\n\n".format(
                    each_match_subscription['author'],
                    each_match_subscription['url'])
            user_mail = key
            notification = Notification('email', user_mail, subject, mail_content)
            notification.notify_user()
