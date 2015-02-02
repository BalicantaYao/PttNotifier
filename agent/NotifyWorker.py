#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: bustta
# @Date:   2015-01-26 23:00:17
# @Last Modified by:   bustta
# @Last Modified time: 2015-02-03 00:51:49
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
# List<Dictionary<string, List<MatchInfo>>>
# [
#     {'bustta80980@gmail.com':
#         [
#             {'url': 'https://www.ptt.cc/bbs/BuyTogether/M.1422893377.A.354.html',
#                 'topic': '[綜合] 科皙佳身體乳洗髮沐浴組188-全家店到店',
#                 'kw_list': ['科皙佳'], 'author': 'Date2329', 'date': ' 2/03'},
#             {'url': 'https://www.ptt.cc/bbs/BuyTogether/M.1422893518.A.323.html',
#                 'topic': '[綜合] 科皙佳身體乳+洗沐組-頂溪/永和/EZ',
#                 'kw_list': ['科皙佳'], 'author': 'shenwhei', 'date': ' 2/03'}
#         ]
#     }
# ]


for send_target in match_list:
    for key in send_target.keys():
        user_mail = key
        match_info_list = send_target[user_mail]

        if len(match_info_list) > 0:
            mail_content = ''
            subject = "關鍵字配對成功：{0}".format(', '.join(match_info_list[0]['kw_list']))

            for each_match_subscription in match_info_list:
                mail_content += "作者： {0}\n文章：{1}\n\n".format(
                    each_match_subscription['author'],
                    each_match_subscription['url'])


            notification = Notification('email', user_mail, subject, mail_content)
            notification.notify_user()


