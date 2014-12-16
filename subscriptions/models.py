from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Subscrption(models.Model):
    """model of subscription"""
    user = models.ForeignKey(User)
    keywords = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username

