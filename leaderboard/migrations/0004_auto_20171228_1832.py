# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-28 13:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboard', '0003_auto_20171228_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scorecard',
            name='creator',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
