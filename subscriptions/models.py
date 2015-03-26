from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class BoardCategory(models.Model):
    category_cht_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_cht_name


class Board(models.Model):
    board_eng_name = models.CharField(max_length=255)
    board_cht_name = models.CharField(max_length=255)
    category = models.ForeignKey(BoardCategory)
    is_18_forbidden = models.BooleanField(default=False)
    status = models.IntegerField()

    def __str__(self):
        return self.board_eng_name


class Subscrption(models.Model):
    """model of subscription"""
    user = models.ForeignKey(User)
    keywords = models.CharField(max_length=255)
    board = models.ForeignKey(Board)
    # notifiedDate = models.DateField()

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('subscription_detail', kwargs={'pk': self.pk})


class Notification(models.Model):
    """model for Notification"""
    subscription_user = models.ForeignKey(Subscrption)
    notified_date = models.DateField()
    notified_time = models.TimeField()
    notified_type = models.CharField(max_length=12)
    match_url = models.CharField(max_length=255)


class BoardScanning(models.Model):
    board_name = models.CharField(max_length=255)
    page_number_of_last_scan = models.IntegerField()
    last_scan_pages_count = models.IntegerField()
