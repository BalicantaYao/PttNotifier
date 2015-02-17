from __future__ import absolute_import

from .models import Subscrption
from celery import shared_task

from .agent.Base import BaseAgent


@shared_task
def scanBoard():
    # Find All Subscription
    subscriptions = Subscrption.objects.all()

    for item in subscriptions:
        print (item.board)

    return subscriptions.count()
