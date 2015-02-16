#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: bustta
# @Date:   2015-01-22 23:22:07
# @Last Modified by:   bustta
# @Last Modified time: 2015-02-10 22:45:43
from agent.DataDriver.PGDataDriver import PGDataDriver


class SubscriptionRepo():

    def __init__(self):
        super(SubscriptionRepo, self).__init__()
        self.pg_driver = PGDataDriver()

    def get_all_user_subscription(self):
        self.pg_driver.open_pg_connection()
        cur = self.pg_driver.get_pg_cursor()

        sql = """
          SELECT u.email, s.keywords, s.id
          FROM subscriptions_subscrption s, auth_user u
          WHERE s.user_id = u.id"""

        rows = self.pg_driver.execute_and_fetchall(sql, cur)
        self.pg_driver.close_pg_connection()

        subscription_list = []
        for row in rows:
            subs_obj = {'user_mail': row[0], 'kw_list': row[1].split(','), 'subscription_id': row[2]}
            subscription_list.append(subs_obj)

        return subscription_list
