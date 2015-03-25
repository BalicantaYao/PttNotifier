#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import datetime
import logging

from .models import Subscrption, Notification
from celery import shared_task

from .agent.Base.BaseAgent import BaseAgent
from .agent.NotifyUtil.Notification import NotificationItem


@shared_task
def scanBoard():
    # Find All Subscription
    subscriptions = Subscrption.objects.all()
    user_mail_with_matched_articles = {}
    agent_pool = {}
    for subscription in subscriptions:
        board_name = subscription.board.board_eng_name
        user_email = subscription.user.email

        # Flyweight pattern
        agent = agent_pool.get(board_name, BaseAgent(board_name))
        agent_pool[board_name] = agent

        all_entries = agent.get_entries_after_last_fetch()
        if len(all_entries) <= 0:
            continue

        # TODO: Muliti keyword
        matched_articles = []
        logging.info(all_entries)
        for article in all_entries:
            article_topic = article['topic']

            if subscription.keywords in article_topic:

                matched_article = article

                # Check is ever sent
                isSent = Notification.objects.filter(subscription_user=subscription,
                                                     match_url=matched_article['url']).exists()
                if(isSent):
                    continue

                matched_article['keyword'] = subscription.keywords
                matched_articles.append(matched_article)

                now = datetime.datetime.now()
                Notification.objects.create(subscription_user=subscription,
                                            notified_date=now.strftime("%Y-%m-%d"),
                                            notified_time=now.strftime("%H:%M:%S"),
                                            notified_type='email', match_url=matched_article['url'])

        if len(matched_articles) > 0:
            user_mathced_list = user_mail_with_matched_articles.get(user_email, list())
            user_mathced_list += matched_articles
            user_mail_with_matched_articles[user_email] = user_mathced_list

    for user_email in user_mail_with_matched_articles.keys():
        match_info_list = user_mail_with_matched_articles[user_email]
        mail_content = ""
        subject = "Buzz3.co 送上您關注的 Ptt 消息"

        for info in match_info_list:
            mail_content += "作者： {0}\n文章：{1}\n\n".format(info['author'], info['url'])

        if len(mail_content) > 0:
            notification = NotificationItem('email', user_email, subject, mail_content)
            notification.notify_user()

    return subscriptions.count()
