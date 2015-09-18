# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('front_page', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='date',
        ),
        migrations.AddField(
            model_name='blog',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='modified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
