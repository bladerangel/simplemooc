# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-07 20:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20170304_1434'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='test',
            field=models.CharField(max_length=50, null=True, verbose_name='aew'),
        ),
    ]
