#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: bustta
# @Date:   2015-02-01 23:35:06
# @Last Modified by:   bustta
# @Last Modified time: 2015-02-10 22:51:00
from PGDataDriver import PGDataDriver


class NotificationRepo(PGDataDriver):

    def __init__(self):
        super(NotificationRepo, self).__init__()
        self.open_pg_connection()
        self._cur = self.get_pg_cursor()

    def create_notification(self, notification_obj):
        # date, time, type, url, subs_id
        sql = """
            INSERT INTO subscriptions_notification
            (notified_date, notified_time, notified_type, match_url, subscription_user_id)
            VALUES ('{0}', '{1}', '{2}', '{3}', '{4}');
        """.format(
            notification_obj['date'], notification_obj['time'],
            notification_obj['type'], notification_obj['url'],
            notification_obj['subscription_id']
            )

        self.execute_and_commit(sql, self._cur)
        # self.close_pg_connection()

    # id | notified_date | notified_time | notified_type | match_url | subscription_user_id
    def get_all(self):
        sql = """
            SELECT * FROM subscriptions_notification;
        """

        rows = self.execute_and_fetchall(sql, self._cur)
        # self.close_pg_connection()
        notification_list = []
        for row in rows:
            each_subs = {
                'id': row[0],
                'date': row[1],
                'time': row[2],
                'type': row[3],
                'url': row[4],
                'user_id': row[5]
            }
            notification_list.append(each_subs)
        return notification_list

    def get_notification_by_sid_and_url(self, sid, url):
        sql = """
            SELECT id
            FROM subscriptions_notification
            WHERE subscription_user_id = '{0}'
            AND match_url = '{1}'
        """.format(sid, url)
        rows = self.execute_and_fetchall(sql, self._cur)
        notification_list = []
        for row in rows:
            notification_list.append(row[0])

        return notification_list