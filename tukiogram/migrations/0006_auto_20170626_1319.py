# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-26 10:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tukiogram', '0005_auto_20170319_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tukio',
            name='location_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]