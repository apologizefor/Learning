# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-11-24 11:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commucation', '0007_keywords'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='tag',
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='commucation.Tag', verbose_name='标签'),
        ),
    ]
