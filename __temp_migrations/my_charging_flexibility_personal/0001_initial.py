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
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_charging_flexibility_personal_group', to='otree.Session')),
            ],
            options={
                'db_table': 'my_charging_flexibility_personal_group',
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
                ('crt_epkw', otree.db.models.IntegerField(choices=[[1, 'Ja'], [2, 'Nein']], null=True, verbose_name='Besitzen oder fahren Sie regelmäßig einen E-PKW?')),
                ('crt_bev_exp', otree.db.models.IntegerField(null=True, verbose_name='Bitte schätzen Sie, wie viele Kilometer Sie bisher mit E-PKWs gefahren sind.')),
                ('crt_conv_exp', otree.db.models.IntegerField(null=True, verbose_name='Bitte schätzen Sie, wieviele Kilometer Sie bisher mit einem konventionellen PKW gefahren sind.')),
                ('crt_zweitwagen', otree.db.models.IntegerField(choices=[[1, 'Keinen PKW'], [2, 'Einen PKW'], [3, 'Zwei PKWs'], [4, 'Drei PKWs'], [5, 'Mehr als drei PKWs'], [6, 'Keine Angabe']], null=True, verbose_name='Auf wie viele PKWs (inklusive E-PKWs) kann Ihr Haushalt insgesamt zurückgreifen?')),
                ('crt_flex_nutzung', otree.db.models.IntegerField(choices=[[1, 'Ja'], [2, 'Nein']], null=True, verbose_name='Haben Sie in der Vergangenheit bereits intelligentes Laden verwendet?')),
                ('crt_flex_anzahl', otree.db.models.IntegerField(null=True, verbose_name='Bitte schätzen Sie, wie oft Sie bisher intelligentes Laden genutzt haben. Falls Sie bisher noch nie intelligentes Laden genutzt haben tragen Sie bitte eine 0 ein.')),
                ('crt_flex_absicht', otree.db.models.IntegerField(choices=[[1, 'Ja'], [2, 'Nein']], null=True, verbose_name='Haben Sie die Absicht in Zukunft intelligentes Laden zu nutzen?')),
                ('crt_risiko', otree.db.models.IntegerField(choices=[[1, 'Gar nicht risikobereit'], [2, ''], [3, ''], [4, ''], [5, ''], [6, ''], [7, 'Sehr risikobereit']], null=True, verbose_name='Sind Sie im Allgemeinen ein risikobereiter Mensch oder versuchen Sie Risiken zu vermeiden?')),
                ('crt_age', otree.db.models.IntegerField(null=True, verbose_name='Wie alt sind Sie?')),
                ('crt_gender', otree.db.models.IntegerField(choices=[[1, 'Männlich'], [2, 'Weiblich'], [3, 'Keine Angabe']], null=True, verbose_name='Welchem Geschlecht fühlen Sie sich zugehörig?')),
                ('crt_bildung', otree.db.models.IntegerField(choices=[[1, 'Kein Schulabschluss'], [2, 'Grund-/Hauptschulabschluss'], [3, 'Realschule (Mittlere Reife)'], [4, 'Gymnasium (Abitur)'], [5, 'Abgeschlossene Ausbildung'], [6, 'Fachhochschulabschluss'], [7, 'Hochschule (Bachelor)'], [8, 'Hochschule (Master/Diplom)'], [9, 'Hochschule (Promotion)']], null=True, verbose_name='Was ist Ihr höchster Bildungsabschluss?')),
                ('crt_wohnort', otree.db.models.IntegerField(choices=[[1, 'Städtischer Raum'], [2, 'Ländlicher Raum']], null=True, verbose_name='Wo wohnen Sie?')),
                ('crt_einkommen', otree.db.models.IntegerField(choices=[[1, 'Bis unter 1000 €'], [2, '1000 € bis unter 2000 €'], [3, '2000 € bis unter 3000 €'], [4, '3000 € bis unter 4000 €'], [5, '4000 € bis unter 5000 €'], [6, '5000 € bis unter 6000 €'], [7, '6000 € und mehr'], [8, 'Keine Angabe']], null=True, verbose_name='Wie hoch war Ihr monatliches Einkommen im Jahr 2017 Brutto?')),
                ('crt_kommentar', otree.db.models.LongStringField(blank=True, null=True, verbose_name='Mit einem Klick auf "Weiter" schließen Sie das Experiment ab und kehren zu Amazon zurück. Falls Sie davor noch einen Kommentar zu diesem Experiment abgeben möchten, können Sie dies im folgenden Feld tun.')),
                ('crt_tpb_einstellung1', otree.db.models.IntegerField(choices=[[1, 'Extrem unvorteilhaft'], [2, ''], [3, ''], [4, ''], [5, ''], [6, ''], [7, 'Extrem vorteilhaft']], null=True, verbose_name='Für mich persönlich ist die Bereitstellung von Flexibilität')),
                ('crt_tpb_einstellung2', otree.db.models.IntegerField(choices=[[1, 'Extrem unerwünscht'], [2, ''], [3, ''], [4, ''], [5, ''], [6, ''], [7, 'Extrem erwünscht']], null=True, verbose_name='Für mich persönlich ist die Bereitstellung von Flexibilität')),
                ('crt_tpb_einstellung3', otree.db.models.IntegerField(choices=[[1, 'Extrem unangenehm'], [2, ''], [3, ''], [4, ''], [5, ''], [6, ''], [7, 'Extrem angenehm']], null=True, verbose_name='Für mich persönlich ist die Bereitstellung von Flexibilität')),
                ('crt_tpb_einstellung4', otree.db.models.IntegerField(choices=[[1, 'Extrem negativ'], [2, ''], [3, ''], [4, ''], [5, ''], [6, ''], [7, 'Extrem positiv']], null=True, verbose_name='Für mich persönlich ist die Bereitstellung von Flexibilität')),
                ('crt_tpb_einstellung5', otree.db.models.IntegerField(choices=[[1, 'Extrem unwahrscheinlich'], [2, ''], [3, ''], [4, ''], [5, ''], [6, ''], [7, 'Extrem wahrscheinlich']], null=True, verbose_name='Für mich persönlich ist die Bereitstellung von Flexibilität')),
                ('crt_tpb_normen1', otree.db.models.IntegerField(choices=[[1, 'Ich stimme überhaupt nicht zu'], [2, ''], [3, ''], [4, ''], [5, ''], [6, ''], [7, 'Ich stimme vollkommen zu']], null=True, verbose_name='Die meisten Menschen, die mir wichtig sind, denken ich sollte Flexibilität bereitstellen')),
                ('crt_tpb_normen2', otree.db.models.IntegerField(choices=[[1, 'Ich stimme überhaupt nicht zu'], [2, ''], [3, ''], [4, ''], [5, ''], [6, ''], [7, 'Ich stimme vollkommen zu']], null=True, verbose_name='Wenn ich regelmäßig Flexibilität bereitstellen würden, würden die meisten Menschen, die mir wichtig sind ebenfalls Flexibilität bereit stellen')),
                ('crt_tpb_normen3', otree.db.models.IntegerField(choices=[[1, 'Ich stimme überhaupt nicht zu'], [2, ''], [3, ''], [4, ''], [5, ''], [6, ''], [7, 'Ich stimme vollkommen zu']], null=True, verbose_name='Menschen, deren Meinung ich schätze, würden es gut finden, wenn ich Flexibilität bereitstellen würde')),
                ('crt_tpb_normen4', otree.db.models.IntegerField(choices=[[1, 'Ich stimme überhaupt nicht zu'], [2, ''], [3, ''], [4, ''], [5, ''], [6, ''], [7, 'Ich stimme vollkommen zu']], null=True, verbose_name='Die meisten Menschen, die mir ähnlich sind stellen Flexibilität bereit')),
                ('crt_tpb_normen5', otree.db.models.IntegerField(choices=[[1, 'Ich stimme überhaupt nicht zu'], [2, ''], [3, ''], [4, ''], [5, ''], [6, ''], [7, 'Ich stimme vollkommen zu']], null=True, verbose_name='Meine Freunde fänden es gut, wenn ich Flexibilität bereit stelle')),
                ('crt_tpb_kontrolle1', otree.db.models.IntegerField(choices=[[1, 'Ich stimme überhaupt nicht zu'], [2, ''], [3, ''], [4, ''], [5, ''], [6, ''], [7, 'Ich stimme vollkommen zu']], null=True, verbose_name='Ich bin mir sicher, dass ich in der Lage bin intelligentes Laden zu benutzen')),
                ('crt_tpb_kontrolle2', otree.db.models.IntegerField(choices=[[1, 'Ich stimme überhaupt nicht zu'], [2, ''], [3, ''], [4, ''], [5, ''], [6, ''], [7, 'Ich stimme vollkommen zu']], null=True, verbose_name='Ich bin mir sicher, dass ich, wenn ich es wollte, intelligentes Laden verwenden kann')),
                ('crt_tpb_kontrolle3', otree.db.models.IntegerField(choices=[[1, 'Ich stimme überhaupt nicht zu'], [2, ''], [3, ''], [4, ''], [5, ''], [6, ''], [7, 'Ich stimme vollkommen zu']], null=True, verbose_name='Die Nutzung intelligenten Ladens ist einfach für mich')),
                ('crt_tpb_kontrolle4', otree.db.models.IntegerField(choices=[[1, 'Ich stimme überhaupt nicht zu'], [2, ''], [3, ''], [4, ''], [5, ''], [6, ''], [7, 'Ich stimme vollkommen zu']], null=True, verbose_name='Ob ich intelligentes Laden benutze hängt nur von mir ab')),
                ('crt_tpb_kontrolle5', otree.db.models.IntegerField(choices=[[1, 'Ich stimme überhaupt nicht zu'], [2, ''], [3, ''], [4, ''], [5, ''], [6, ''], [7, 'Ich stimme vollkommen zu']], null=True, verbose_name='Ich kann die Entscheidung intelligentes Laden zu verwenden nicht selbstständig kontrollieren')),
                ('crt_tpb_absicht1', otree.db.models.IntegerField(choices=[[1, 'Ich stimme überhaupt nicht zu'], [2, ''], [3, ''], [4, ''], [5, ''], [6, ''], [7, 'Ich stimme vollkommen zu']], null=True, verbose_name='Ich bin willens intelligentes Laden zu verwenden')),
                ('crt_tpb_absicht2', otree.db.models.IntegerField(choices=[[1, 'Ich stimme überhaupt nicht zu'], [2, ''], [3, ''], [4, ''], [5, ''], [6, ''], [7, 'Ich stimme vollkommen zu']], null=True, verbose_name='Ich beabsichtige intelligentes Laden zu verwenden')),
                ('crt_tpb_absicht3', otree.db.models.IntegerField(choices=[[1, 'Ich stimme überhaupt nicht zu'], [2, ''], [3, ''], [4, ''], [5, ''], [6, ''], [7, 'Ich stimme vollkommen zu']], null=True, verbose_name='Ich plane intelligentes Laden zu verwenden')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='my_charging_flexibility_personal.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_charging_flexibility_personal_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_charging_flexibility_personal_player', to='otree.Session')),
            ],
            options={
                'db_table': 'my_charging_flexibility_personal_player',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='my_charging_flexibility_personal_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'my_charging_flexibility_personal_subsession',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.AddField(
            model_name='player',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_charging_flexibility_personal.Subsession'),
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_charging_flexibility_personal.Subsession'),
        ),
    ]
