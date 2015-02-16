#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: bustta
# @Date:   2015-01-26 23:00:17
# @Last Modified by:   bustta
# @Last Modified time: 2015-02-10 23:03:27
import datetime

from Repo.SubscriptionRepo import SubscriptionRepo
from Base.BaseAgent import BaseAgent
from NotifyUtil.Notification import Notification
from Repo.NotificationRepo import NotificationRepo
from LogUtil.LogUtil import LogUtil


def scan_and_notify():
    is_this_minute_exe = False
    util = LogUtil()
    # agent = BaseAgent('BuyTogether')
    agent = BaseAgent('Beauty')
    while True:
        now_min = datetime.datetime.now().minute
        if now_min % 2 == 0 and not is_this_minute_exe:
            is_this_minute_exe = True
            util.logger("ExecuteAt: {0}".format(datetime.datetime.now()))

            dao = SubscriptionRepo()
            subs = dao.get_all_user_subscription()
            all_entries = agent.get_entries_after_last_fetch()
            if len(all_entries) <= 0:
                continue

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
                        match_obj['subscription_id'] = target['subscription_id']
                        match_list_for_each_person.append(match_obj)

                if len(match_list_for_each_person) > 0:
                    match_set = {}
                    match_set[target['user_mail']] = match_list_for_each_person
                    match_list.append(match_set)

            # print("\nmatch: {0}\n".format(match_list))

            for send_target in match_list:
                for key in send_target.keys():
                    user_mail = key
                    match_info_list = send_target[user_mail]

                    if len(match_info_list) > 0:
                        notification_list = []
                        mail_content = ''
                        subject = "關鍵字配對成功：{0}".format(', '.join(match_info_list[0]['kw_list']))
                        notification_repo = NotificationRepo()
                        for each_match_subscription in match_info_list:
                            # check mail in pg; if existed, continue
                            nlist = notification_repo.get_notification_by_sid_and_url(
                                each_match_subscription['subscription_id'],
                                each_match_subscription['url']
                            )
                            if len(nlist) > 0:
                                # print(nlist)
                                continue

                            now = datetime.datetime.now()
                            notification_obj = {
                                'subscription_id': each_match_subscription['subscription_id'],
                                'date': now.strftime("%Y-%m-%d"),
                                'time': now.strftime("%H:%M:%S"),
                                'type': 'email',
                                'url': each_match_subscription['url']
                            }
                            notification_repo.insert(notification_obj)
                            notification_list.append(notification_obj)
                            util.logger(notification_obj)

                            mail_content += "作者： {0}\n文章：{1}\n\n".format(
                                each_match_subscription['author'],
                                each_match_subscription['url'])

                        # aggregate match articles in one mail to the same person
                        if len(mail_content) > 0:
                            notification = Notification('email', user_mail, subject, mail_content)
                            notification.notify_user()

        elif now_min % 2 != 0:
                is_this_minute_exe = False


if __name__ == '__main__':
    scan_and_notify()
