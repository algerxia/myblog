# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-04-03 08:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0005_auto_20190306_2234'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sidebar',
            options={'verbose_name': '侧边栏', 'verbose_name_plural': '侧边栏'},
        ),
        migrations.AlterField(
            model_name='sidebar',
            name='status',
            field=models.PositiveIntegerField(choices=[(0, '隐藏'), (1, '展示')], default=1, verbose_name='状态'),
        ),
    ]