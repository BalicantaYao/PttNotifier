import os
import psycopg2

conn = psycopg2.connect(
    database=os.environ['PTTNOTIFIER_DB'],
    user=os.environ['PTTNOTIFIER_DB_DEFAULT_USER'],
    password=os.environ['PTTNOTIFIER_DB_DEFAULT_PASSWORD'],
    host="127.0.0.1", port="5432")

msg = "Opened database successfully"
print(msg)

cur = conn.cursor()

sql = """
SELECT email
FROM auth_user
"""

cur.execute(sql)
rows = cur.fetchall()
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
    
  cur.execute(sql)
  rows = cur.fetchall()
  print("User: ", item)
  for row in rows:
    print("keywords: ", row[0])

print("Operation Done.")
conn.close()
