# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0003_notification'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscrption',
            name='notifiedDate',
        ),
    ]
