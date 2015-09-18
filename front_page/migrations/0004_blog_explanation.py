# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('front_page', '0003_auto_20150907_0758'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='explanation',
            field=models.TextField(max_length=10000, blank=True),
        ),
    ]
