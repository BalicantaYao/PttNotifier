# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0004_remove_subscrption_notifieddate'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoardScanning',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('board_name', models.CharField(max_length=255)),
                ('page_number_of_last_scan', models.IntegerField()),
                ('last_scan_pages_count', models.IntegerField()),
            ],
            options=None,
            bases=None,
            # managers=None,
        ),
    ]
