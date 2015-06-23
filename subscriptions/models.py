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
    notified_date = models.DateField(auto_now_add=True, null=True)
    notified_time = models.TimeField(auto_now_add=True, null=True)
    notified_type = models.CharField(max_length=12)
    match_url = models.CharField(max_length=255)
    is_sent = models.BooleanField(default=False)
    is_read = models.BooleanField(default=False)
    article_topic = models.CharField(max_length=255, default='')
    article_author = models.CharField(max_length=50, default='')
    article_push_count = models.IntegerField(default=0)
    subscription_type = models.IntegerField(default=0)


class Article(models.Model):
    topic = models.CharField(max_length=255)
    board_name = models.CharField(max_length=255, default='')
    author = models.CharField(max_length=255)
    url = models.URLField()
    match_count = models.IntegerField(default=0)


class BoardScanning(models.Model):
    board_name = models.CharField(max_length=255)
    page_number_of_last_scan = models.IntegerField()
    last_scan_pages_count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


class MailSending(models.Model):
    mail_to = models.CharField(max_length=255)
    day_count = models.IntegerField()
    date = models.DateField()


class KeywordToken(models.Model):
    token = models.CharField(max_length=255)
    board = models.ForeignKey(Board)
    hot = models.IntegerField(default=1)
