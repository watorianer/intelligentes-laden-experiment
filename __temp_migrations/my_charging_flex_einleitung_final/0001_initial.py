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
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_charging_flex_einleitung_final_group', to='otree.Session')),
            ],
            options={
                'db_table': 'my_charging_flex_einleitung_final_group',
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
                ('crt_vorteile', otree.db.models.StringField(choices=[('Verbesserte Stabilität des Stromnetzes', 'Verbesserte Stabilität des Stromnetzes'), ('Verringerte Ladezeiten', 'Verringerte Ladezeiten'), ('Verringerter Planungsaufwand', 'Verringerter Planungsaufwand')], max_length=10000, null=True, verbose_name='Was ist ein Vorteil intelligenten Ladens?')),
                ('crt_nachteile', otree.db.models.StringField(choices=[('Erhöhte Ladekosten', 'Erhöhte Ladekosten'), ('Verringerter Anteil erneuerbarer Energien', 'Verringerter Anteil erneuerbarer Energien'), ('Verringerte Flexibilität (im Mobilitätsverhalten)', 'Verringerte Flexibilität (im Mobilitätsverhalten)')], max_length=10000, null=True, verbose_name='Was ist ein Nachteil intelligenten Ladens?')),
                ('crt_abfahrt', otree.db.models.StringField(choices=[('Der Ladevorgang wird fortgesetzt', 'Der Ladevorgang wird fortgesetzt'), ('Der Ladevorgang wird abgebrochen', 'Der Ladevorgang wird abgebrochen')], max_length=10000, null=True, verbose_name='Was passiert, wenn die vom Experiment realisierte Abfahrtszeit erreicht wird, während der Ladevorgang noch läuft?')),
                ('crt_ladeflex', otree.db.models.StringField(choices=[('Sie erhalten Punkte', 'Sie erhalten Punkte'), ('Nichts', 'Nichts'), ('Ihnen werden Punkte abgezogen', 'Ihnen werden Punkte abgezogen')], max_length=10000, null=True, verbose_name='Was passiert, wenn die geladenen Kilometer am nächsten Tag ausreichen?')),
                ('crt_unzureichend', otree.db.models.StringField(choices=[('Nichts', 'Nichts'), ('Sie erhalten Punkte', 'Sie erhalten Punkte'), ('Ihnen werden Punkte abgezogen', 'Ihnen werden Punkte abgezogen')], max_length=10000, null=True, verbose_name='Was passiert, wenn die geladenen Kilometer am nächsten Tag nicht ausreichen?')),
                ('treatment_group', otree.db.models.StringField(max_length=10000, null=True)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='my_charging_flex_einleitung_final.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_charging_flex_einleitung_final_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_charging_flex_einleitung_final_player', to='otree.Session')),
            ],
            options={
                'db_table': 'my_charging_flex_einleitung_final_player',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='my_charging_flex_einleitung_final_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'my_charging_flex_einleitung_final_subsession',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.AddField(
            model_name='player',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_charging_flex_einleitung_final.Subsession'),
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_charging_flex_einleitung_final.Subsession'),
        ),
    ]
