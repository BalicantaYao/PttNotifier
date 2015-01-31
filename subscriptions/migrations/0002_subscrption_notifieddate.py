# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscrption',
            name='notifiedDate',
            field=models.DateField(default=datetime.datetime(2015, 1, 31, 17, 56, 44, 408452, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
