# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-04-08 17:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0008_auto_20190409_0042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sidebar',
            name='status',
            field=models.PositiveIntegerField(choices=[(1, '展示'), (0, '隐藏')], default=1, verbose_name='状态'),
        ),
    ]
