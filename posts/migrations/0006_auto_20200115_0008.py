# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-01-15 00:08
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20200114_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 1, 15, 0, 8, 31, 841388, tzinfo=utc), null=True),
        ),
    ]
