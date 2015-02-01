from django.contrib import admin
from .models import Subscrption
from .models import Notification


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'keywords')


class NotificationAdmin(admin.ModelAdmin):
    list_display = (
        'subscription_user',
        'notified_date',
        'notified_time',
        'notified_type',
        'match_url'
        )

admin.site.register(Subscrption, SubscriptionAdmin)

admin.site.register(Notification, NotificationAdmin)