# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-07-07 11:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0006_courseorg_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseorg',
            name='image',
            field=models.ImageField(default=0, upload_to='org/%Y/%m', verbose_name='logo'),
        ),
    ]
