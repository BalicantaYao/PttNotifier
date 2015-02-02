# from BaseAgent import BaseAgent
# agent = BaseAgent("BuyTogether")
# entries = agent.get_entries_after_last_fetch()

# print(entries)
# print("total: {0}".format(len(entries)))
from NotificationRepo import NotificationRepo

nobj = {
    'subs_id': 3,
    'date': '2015-01-02',
    'time': '11:12:13',
    'type': 'email',
    'url': 'google.com'
    }
dao = NotificationRepo()
dao.create_notification(nobj)

# from SubscriptionRepo import SubscriptionRepo

# dao = SubscriptionRepo().get_all_user_subscription()
# print(dao)

