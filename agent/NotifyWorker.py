#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: bustta
# @Date:   2015-01-26 23:00:17
# @Last Modified by:   bustta
# @Last Modified time: 2015-01-30 00:01:19
from SubscriptionRepo import SubscriptionRepo
from BaseAgent import BaseAgent

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
