# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-10-26 15:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commucation', '0003_comment_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='pid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='commucation.Comment', verbose_name='父级评论'),
        ),
    ]
