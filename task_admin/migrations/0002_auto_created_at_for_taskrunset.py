# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 13:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_admin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskrunset',
            name='created_at',
            field=models.DateTimeField(auto_created=True),
        ),
    ]