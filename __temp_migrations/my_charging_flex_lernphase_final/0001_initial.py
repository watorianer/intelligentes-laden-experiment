# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-12-28 16:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import otree.db.models
import otree_save_the_change.mixins


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('otree', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_subsession', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_charging_flex_lernphase_final_group', to='otree.Session')),
            ],
            options={
                'db_table': 'my_charging_flex_lernphase_final_group',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_group', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_payoff', otree.db.models.CurrencyField(default=0, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_gbat_arrived', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)),
                ('_gbat_grouped', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)),
                ('mindestreichweite_sofort', otree.db.models.FloatField(null=True, verbose_name='Bitte geben Sie Ihre Mindestreichweite sofort an')),
                ('mindestreichweite_spaeter', otree.db.models.FloatField(null=True, verbose_name='Bitte geben Sie Ihre Mindestreichweite später an')),
                ('gewuenschte_abfahrt', otree.db.models.FloatField(null=True, verbose_name='Bitte geben Sie an bis wann die Mindestreichweite später geladen sein soll')),
                ('ladeflexibilitaet', otree.db.models.FloatField(null=True)),
                ('geladene_kilometer1', otree.db.models.FloatField(null=True)),
                ('geladene_kilometer2', otree.db.models.FloatField(null=True)),
                ('geladene_kilometer3', otree.db.models.FloatField(null=True)),
                ('treatment_group', otree.db.models.StringField(max_length=10000, null=True)),
                ('minutes1', otree.db.models.IntegerField(null=True)),
                ('hours1', otree.db.models.IntegerField(null=True)),
                ('minutes2', otree.db.models.IntegerField(null=True)),
                ('hours2', otree.db.models.IntegerField(null=True)),
                ('minutes3', otree.db.models.IntegerField(null=True)),
                ('hours3', otree.db.models.IntegerField(null=True)),
                ('gewuenschte_abfahrt_minutes', otree.db.models.IntegerField(null=True)),
                ('gewuenschte_abfahrt_hours', otree.db.models.IntegerField(null=True)),
                ('punkte1', otree.db.models.IntegerField(null=True)),
                ('punkte2', otree.db.models.IntegerField(null=True)),
                ('punkte3', otree.db.models.IntegerField(null=True)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='my_charging_flex_lernphase_final.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_charging_flex_lernphase_final_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_charging_flex_lernphase_final_player', to='otree.Session')),
            ],
            options={
                'db_table': 'my_charging_flex_lernphase_final_player',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='my_charging_flex_lernphase_final_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'my_charging_flex_lernphase_final_subsession',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.AddField(
            model_name='player',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_charging_flex_lernphase_final.Subsession'),
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_charging_flex_lernphase_final.Subsession'),
        ),
    ]
