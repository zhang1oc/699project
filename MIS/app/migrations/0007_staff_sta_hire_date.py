# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-23 02:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20170822_1414'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='sta_hire_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
