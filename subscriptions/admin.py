from django.contrib import admin
from .models import Subscrption, Notification, BoardScanning


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


class BoardScanningAdmin(admin.ModelAdmin):
    list_display = (
        'board_name',
        'page_number_of_last_scan',
        'last_scan_pages_count'
    )

admin.site.register(Subscrption, SubscriptionAdmin)

admin.site.register(Notification, NotificationAdmin)

admin.site.register(BoardScanning, BoardScanningAdmin)
