# from BaseAgent import BaseAgent
# agent = BaseAgent("BuyTogether")
# entries = agent.get_entries_after_last_fetch()

# print(entries)
# print("total: {0}".format(len(entries)))
from NotificationRepo import NotificationRepo

nobj = {
    'subscription_id': 3,
    'date': '2015-01-02',
    'time': '11:12:13',
    'type': 'email',
    'url': 'google.com'
    }
dao = NotificationRepo()
list = dao.get_notification_by_sid_and_url(7, "https://www.ptt.cc/bbs/BuyTogether/M.1423578500.A.636.html")
print(list)
dao.create_notification(nobj)
# list = dao.get_all()

# from SubscriptionRepo import SubscriptionRepo

# dao = SubscriptionRepo().get_all_user_subscription()
# print(dao)

