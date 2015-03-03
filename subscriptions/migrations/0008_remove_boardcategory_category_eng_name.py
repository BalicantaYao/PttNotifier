# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0007_subscrption_board'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boardcategory',
            name='category_eng_name',
        ),
    ]
