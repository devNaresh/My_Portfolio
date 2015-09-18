# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('front_page', '0002_auto_20150903_1318'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catagory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['title']},
        ),
        migrations.AddField(
            model_name='blog',
            name='catagory',
            field=models.ForeignKey(to='front_page.Catagory', null=True),
        ),
    ]
