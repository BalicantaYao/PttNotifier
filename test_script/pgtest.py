from agent.Repo.NotificationRepo import NotificationRepo
from agent.Repo.SubscriptionRepo import SubscriptionRepo
from agent.NotifyUtil.Notification import Notification

notification = NotificationRepo()
nlist = notification.get_all()
print(nlist)

subscription = SubscriptionRepo()
slist = subscription.get_all_user_subscription()
print(slist)


notification = Notification('email', "bustta80980@gmail.com", "PGTest", "Helo, this is agent.")
notification.notify_user()