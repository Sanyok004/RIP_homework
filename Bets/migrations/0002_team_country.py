# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-19 11:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='country',
            field=models.CharField(default='', max_length=30),
        ),
    ]
