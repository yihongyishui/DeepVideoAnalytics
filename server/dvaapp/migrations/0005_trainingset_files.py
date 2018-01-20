# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-20 21:08
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dvaapp', '0004_remove_trainingset_built_ts'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainingset',
            name='files',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
    ]
