# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-06 10:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctors',
            old_name='timings',
            new_name='e_timings',
        ),
        migrations.AddField(
            model_name='doctors',
            name='s_timings',
            field=models.CharField(default='10:00', max_length=50),
            preserve_default=False,
        ),
    ]
