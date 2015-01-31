#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: bustta
# @Date:   2015-01-22 23:22:07
# @Last Modified by:   bustta
# @Last Modified time: 2015-02-01 02:03:39
from PGDataDriver import PGDataDriver


class SubscriptionRepo(PGDataDriver):

    def __init__(self):
        super(SubscriptionRepo, self).__init__()

    def get_all_user_subscription(self):
        self.open_pg_connection()
        cur = self.get_pg_cursor()

        sql = """
          SELECT u.email, s.keywords
          FROM subscriptions_subscrption s, auth_user u
          WHERE s.user_id = u.id"""

        rows = self.execute_and_fetchall(sql, cur)
        self.close_pg_connection()

        subscription_list = []
        for row in rows:
            subs_obj = {'user_mail': row[0], 'kw_list': row[1].split(',')}
            subscription_list.append(subs_obj)

        return subscription_list

    def update_notify_date(self, subscription_id):
        pass