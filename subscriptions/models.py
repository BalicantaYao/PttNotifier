from django.db import models

# Create your models here.


class Subscrption(models.Model):
    """model of subscription"""
    user = models.ForeignKey('User')
    keywords = models.CharField(max_length=255)

    def __str__(self):
        return self.email


class User(models.Model):
    """model of user"""
    email = models.CharField(max_length=255)
    ptt_id = models.CharField(max_length=255)
    fb_name = models.CharField(max_length=255)
    fb_id = models.CharField(max_length=255)

    def __str__(self):
        return self.email
