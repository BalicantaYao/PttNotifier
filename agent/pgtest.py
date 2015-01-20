import os
import psycopg2
from PGDataDriver import *


conn = open_pg_connection()
cur = get_pg_cursor(conn)

sql = """
SELECT email
FROM auth_user
"""
rows = execute_and_fetchall(sql, cur)

all_user_mails = []
for row in rows:
    if len(row[0]) > 0:
        all_user_mails.append(row[0])

for item in all_user_mails:
    sql = """
      SELECT s.keywords
      FROM subscriptions_subscrption s, auth_user u
      WHERE s.user_id = u.id and u.email='{0}'
    """.format(item)

    rows = execute_and_fetchall(sql, cur)
    print("User: ", item)
    for row in rows:
        print("keywords: ", row[0])

close_pg_connection(conn)
