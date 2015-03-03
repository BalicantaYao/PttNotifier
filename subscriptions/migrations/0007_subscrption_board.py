# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0006_auto_20150228_0716'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscrption',
            name='board',
            field=models.ForeignKey(default=-1, to='subscriptions.Board'),
            preserve_default=True,
        ),
    ]
