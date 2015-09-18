# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('front_page', '0004_blog_explanation'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='content',
            field=tinymce.models.HTMLField(blank=True),
        ),
    ]
