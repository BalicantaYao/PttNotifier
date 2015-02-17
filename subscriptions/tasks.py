from __future__ import absolute_import

from .models import Subscrption, Board, BoardCategory
from celery import shared_task

@shared_task
def scanBoard():
    # Find All Subscription
    subscriptions = Subscrption.objects.all()

    for item in subscriptions:
        print (item.board)

    return subscriptions.count()
