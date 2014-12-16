from django.contrib import admin
from .models import Subscrption


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'keywords')

admin.site.register(Subscrption, SubscriptionAdmin)