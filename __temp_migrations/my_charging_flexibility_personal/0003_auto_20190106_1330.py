# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-01-06 12:30
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('my_charging_flexibility_personal', '0002_player_crt_attention'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='crt_wohnort',
            field=otree.db.models.IntegerField(choices=[[1, 'Städtischer Raum'], [2, 'Ländlicher Raum'], [3, 'Vorstadt']], null=True, verbose_name='Wo wohnen Sie?'),
        ),
    ]
