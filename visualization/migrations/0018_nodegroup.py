# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-30 16:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualization', '0017_auto_20170518_1807'),
    ]

    operations = [
        migrations.CreateModel(
            name='NodeGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True)),
                ('expression', models.TextField()),
            ],
        ),
    ]
