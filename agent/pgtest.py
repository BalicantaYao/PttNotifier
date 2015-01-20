from PGDataDriver import *

conn = open_pg_connection()
cur = get_pg_cursor(conn)

sql = """
  SELECT u.email, s.keywords
  FROM subscriptions_subscrption s, auth_user u
  WHERE s.user_id = u.id"""

rows = execute_and_fetchall(sql, cur)

for row in rows:
    print("User: {0}, keywords: {1}".format(row[0], row[1]))

close_pg_connection(conn)
