# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-17 16:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20171217_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='country',
            field=models.CharField(max_length=255),
        ),
    ]
