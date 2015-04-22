#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import datetime
import redis
import json

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
        is_not_has_new_topic = len(all_entries) <= 0
        if is_not_has_new_topic:
            continue

        # TODO: Muliti keyword
        matched_articles = []
        for article in all_entries:
            article_topic = article['topic']

            if subscription.keywords in article_topic:

                matched_article = article

                # Check is ever sent
                isSent = Notification.objects.filter(subscription_user=subscription,
                                                     match_url=matched_article['url']).exists()
                if isSent:
                    continue

                matched_article['keyword'] = subscription.keywords
                matched_articles.append(matched_article)

                now = datetime.datetime.now()
                new_notification = Notification.objects.create(subscription_user=subscription,
                                                               article_topic=article_topic,
                                                               # notified_time=now.strftime("%H:%M:%S"),
                                                               notified_type='email',
                                                               match_url=matched_article['url'],
                                                               article_author=matched_article['author'])
                publish_to_redis(new_notification)

        if len(matched_articles) > 0:
            user_mathced_list = user_mail_with_matched_articles.get(user_email, list())
            user_mathced_list += matched_articles
            user_mail_with_matched_articles[user_email] = user_mathced_list

    for user_email in user_mail_with_matched_articles.keys():
        match_info_list = user_mail_with_matched_articles[user_email]
        mail_content = []
        subject = "Buzz3.co 送上您關注的 Ptt 消息"

        for info in match_info_list:
            item = {
                'topic': info['topic'],
                'author': info['author'],
                'url': info['url']
            }
            mail_content.append(item)

        if len(mail_content) > 0:
            notification = NotificationItem('email', user_email, subject, mail_content)
            notification.notify_user()

    return subscriptions.count()


def publish_to_redis(notification):

    redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

    # Notication Channel Name, e.g. notifications.1
    redis_client.publish(
        'notifications.%s' % notification.subscription_user.user.id,
        json.dumps(
            dict(
                url=notification.match_url,
                topic=notification.article_topic
            )
        )
    )

    # Add Notification to Redis
    redis_client.hset(notification.subscription_user.user.id,
                      notification.match_url, notification.article_topic)
