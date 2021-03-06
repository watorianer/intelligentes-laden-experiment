# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-02-06 14:25
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('my_charging_flexibility_personal', '0006_auto_20190111_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='crt_einkommen',
            field=otree.db.models.IntegerField(choices=[[1, 'Bis unter 1000 €'], [2, '1000 € bis unter 2000 €'], [3, '2000 € bis unter 3000 €'], [4, '3000 € bis unter 4000 €'], [5, '4000 € bis unter 5000 €'], [6, '5000 € bis unter 6000 €'], [7, 'nu'], [8, 'Keine Angabe']], null=True, verbose_name='Wie hoch war Ihr monatliches Einkommen im Jahr 2017 Brutto?'),
        ),
    ]
