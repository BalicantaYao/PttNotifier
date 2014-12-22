from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.


class Subscrption(models.Model):
    """model of subscription"""
    user = models.ForeignKey(User)
    keywords = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('subscription_detail', kwargs={'pk': self.pk})
