# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-17 02:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authDemo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='type',
            field=models.IntegerField(choices=[(1, '普通用户'), (2, 'vip'), (3, 'svip')], default=1),
        ),
    ]