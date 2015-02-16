# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0002_subscrption_notifieddate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=True, auto_created=True, verbose_name='ID')),
                ('notified_date', models.DateField()),
                ('notified_time', models.TimeField()),
                ('notified_type', models.CharField(max_length=12)),
                ('match_url', models.CharField(max_length=255)),
                ('subscription_user', models.ForeignKey(to='subscriptions.Subscrption')),
            ],
            options=None,
            bases=None,
            # managers=None,
        ),
    ]
