from django.contrib import admin
from .models import Subscrption, Notification, BoardScanning, Board, BoardCategory


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'keywords')


class NotificationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'subscription_user',
        'notified_date',
        'notified_time',
        'notified_type',
        'match_url'
        )


class BoardScanningAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'board_name',
        'page_number_of_last_scan',
        'last_scan_pages_count'
    )


class BoardAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'board_eng_name',
        'board_cht_name',
        'is_18_forbidden',
        'status'
    )


class BoardCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'category_eng_name',
        'category_cht_name'
    )


admin.site.register(Subscrption, SubscriptionAdmin)
admin.site.register(Notification, NotificationAdmin)
admin.site.register(BoardScanning, BoardScanningAdmin)
admin.site.register(Board, BoardAdmin)
admin.site.register(BoardCategory, BoardCategoryAdmin)
