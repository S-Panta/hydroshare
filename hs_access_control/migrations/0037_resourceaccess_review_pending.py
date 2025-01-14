# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-10-21 14:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hs_access_control', '0036_auto_20220510_1213'),
    ]

    operations = [
        migrations.AddField(
            model_name='resourceaccess',
            name='review_pending',
            field=models.BooleanField(default=False, help_text='whether resource is under metadata review'),
        ),
        migrations.RunSQL("ALTER TABLE hs_access_control_resourceaccess ALTER COLUMN review_pending SET DEFAULT FALSE;"),
    ]
