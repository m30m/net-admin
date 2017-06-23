# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-23 22:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualization', '0024_zone_and_desk_sizes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contestant',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='zone',
            name='desk_height',
            field=models.FloatField(default=20),
        ),
        migrations.AlterField(
            model_name='zone',
            name='desk_width',
            field=models.FloatField(default=40),
        ),
    ]