# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-01-07 20:57
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('my_charging_flex_treatment_final', '0003_auto_20190104_1951'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='alte_punkte',
            field=otree.db.models.IntegerField(null=True),
        ),
    ]
