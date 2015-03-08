# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0005_boardscanning'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('board_eng_name', models.CharField(max_length=255)),
                ('board_cht_name', models.CharField(max_length=255)),
                ('is_18_forbidden', models.BooleanField(default=False)),
                ('status', models.IntegerField()),
            ],
            options=None,
            bases=None,
            # managers=None,
        ),
        migrations.CreateModel(
            name='BoardCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('category_eng_name', models.CharField(max_length=255)),
                ('category_cht_name', models.CharField(max_length=255)),
            ],
            options=None,
            bases=None,
            # managers=None,
        ),
        migrations.AddField(
            model_name='board',
            name='category',
            field=models.ForeignKey(to='subscriptions.BoardCategory'),
            preserve_default=True,
        ),
    ]
