# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-10-26 15:55
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commucation', '0005_comment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='date_publish',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='发布时间'),
        ),
    ]
