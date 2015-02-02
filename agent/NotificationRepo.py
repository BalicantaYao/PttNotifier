#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: bustta
# @Date:   2015-02-01 23:35:06
# @Last Modified by:   bustta
# @Last Modified time: 2015-02-02 23:20:54
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
            notification_obj['subs_id']
            )

        self.execute_and_commit(sql, self._cur)
        self.close_pg_connection()
