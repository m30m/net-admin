# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-19 14:58
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task_admin', '0017_timeout_and_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskrunset',
            name='summary',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={}),
            preserve_default=False,
        ),
    ]
