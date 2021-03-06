# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 23:35
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('visualization', '0004_merge_20170224_2250'),
    ]

    operations = [
        migrations.AddField(
            model_name='desk',
            name='position',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='desk', to='visualization.Position'),
        ),
        migrations.AddField(
            model_name='position',
            name='angle',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(359), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='position',
            name='x',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=5),
        ),
        migrations.AddField(
            model_name='position',
            name='y',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=5),
        ),
    ]
