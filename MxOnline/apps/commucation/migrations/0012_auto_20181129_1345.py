# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-11-29 13:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commucation', '0011_auto_20181129_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.CharField(blank=True, max_length=810, null=True, verbose_name='文章内容'),
        ),
    ]
