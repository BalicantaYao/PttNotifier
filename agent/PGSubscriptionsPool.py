#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: bustta
# @Date:   2015-01-22 23:22:07
# @Last Modified by:   bustta
# @Last Modified time: 2015-01-22 23:29:38
from PGDataDriver import *

def get_all_user_subscription():
    conn = open_pg_connection()
    cur = get_pg_cursor(conn)

    sql = """
      SELECT u.email, s.keywords
      FROM subscriptions_subscrption s, auth_user u
      WHERE s.user_id = u.id"""

    rows = execute_and_fetchall(sql, cur)
    close_pg_connection(conn)

    subscription_list = []
    for row in rows:
        subs_obj = {'user_mail': row[0], 'kw_list': row[1].split(',')}
        subscription_list.append(subs_obj)

    print(subscription_list)
