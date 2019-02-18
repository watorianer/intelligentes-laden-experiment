from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
# from otree_tools.models.fields import RadioGridField


author = 'Martin Wolff'

doc = """
Your app description
"""


ROWS_CRT_RISK = (
    (1, ''),
)

# VALUES_CRT_RISK = (
#     (1, 'Gar nicht risikobereit'),
#     (2, 'Weitgehend nicht risikobereit'),
#     (3, 'Eher nicht risikobereit'),
#     (4, 'Weder noch'),
#     (5, 'Eher riskobereit'),
#     (6, 'Weitgehend risikobereit'),
#     (7, 'Extrem risikobereit'),
# )
#
# ROWS_TPB_EINSTELLUNG = (
#     (1, 'Für mich persönlich ist die Bereitstellung von Flexibilität'),
#     (2, 'Für mich persönlich ist die Bereitstellung von Flexibilität'),
#     (3, 'Für mich persönlich ist die Bereitstellung von Flexibilität'),
#     (4, 'Für mich persönlich ist die Bereitstellung von Flexibilität'),
#     (5, 'Für mich persönlich ist die Bereitstellung von Flexibilität'),
# )
#
# VALUES_TPB_EINSTELLUNG = (
#     (1, 'Extrem unvorteilhaft'),
#     (2, 'Weitgehend unvorteilhaft'),
#     (3, 'Eher unvorteilhaft'),
#     (4, 'Weder noch'),
#     (5, 'Eher vorteilhaft'),
#     (6, 'Weitgehend vorteilhaft'),
#     (7, 'Extrem vorteilhaft'),
# )



class Constants(BaseConstants):
    name_in_url = 'my_charging_flexibility_personal'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    crt_epkw = models.IntegerField(label='Besitzen oder fahren Sie regelmäßig einen E-PKW?',
                                   choices=[[1, 'Ja'],
                                            [2, 'Nein']],
                                   widget=widgets.RadioSelect)

    crt_bev_exp = models.IntegerField(label='Bitte schätzen Sie, wie viele Kilometer Sie bisher mit E-PKWs gefahren sind.')

    crt_conv_exp = models.IntegerField(label='Bitte schätzen Sie, wieviele Kilometer Sie bisher mit einem konventionellen PKW gefahren sind.')

    crt_zweitwagen = models.IntegerField(label='Auf wie viele PKWs (inklusive E-PKWs) kann Ihr Haushalt insgesamt zurückgreifen?',
                                         choices=[[1, 'Keinen PKW'],
                                                  [2, 'Einen PKW'],
                                                  [3, 'Zwei PKWs'],
                                                  [4, 'Drei PKWs'],
                                                  [5, 'Mehr als drei PKWs'],
                                                  [6, 'Keine Angabe']],
                                         widget=widgets.RadioSelect)

    crt_flex_nutzung = models.IntegerField(label='Haben Sie in der Vergangenheit bereits intelligentes Laden verwendet?',
                                           choices=[[1, 'Ja'],
                                                    [2, 'Nein']],
                                           widget=widgets.RadioSelect)

    crt_flex_anzahl = models.IntegerField(
        label='Bitte schätzen Sie, wie oft Sie bisher intelligentes Laden genutzt haben. Falls Sie bisher noch nie intelligentes Laden genutzt haben tragen Sie bitte eine 0 ein.')

    crt_flex_absicht = models.IntegerField(label='Haben Sie die Absicht in Zukunft intelligentes Laden zu nutzen?',
                                           choices=[[1, 'Ja'],
                                                    [2, 'Nein']],
                                           widget=widgets.RadioSelect)

    crt_risiko = models.IntegerField(label='Sind Sie im Allgemeinen ein risikobereiter Mensch oder versuchen Sie Risiken zu vermeiden?',
                                     choices=[[1, 'Gar nicht risikobereit'],
                                              [2, ''],
                                              [3, ''],
                                              [4, ''],
                                              [5, ''],
                                              [6, ''],
                                              [7, 'Sehr risikobereit']],
                                     widget=widgets.RadioSelectHorizontal)

    # crt_risiko = RadioGridField(rows=ROWS_CRT_RISK, values=VALUES_CRT_RISK, require_all_fields=True,
    #                             verbose_name='Wie schätzen Sie sich persönlich ein: Sind Sie im Allgemeinen ein risikobereiter Mensch oder versuchen Sie Risiken zu vermeiden?')

    crt_age = models.IntegerField(label='Wie alt sind Sie?')

    crt_gender = models.IntegerField(label='Welchem Geschlecht fühlen Sie sich zugehörig?',
                                     choices=[[1, 'Männlich'],
                                              [2, 'Weiblich'],
                                              [3, 'Keine Angabe']],
                                     widget=widgets.RadioSelect)

    crt_bildung = models.IntegerField(label='Was ist Ihr höchster Bildungsabschluss?',
                                      choices=[[1, 'Kein Schulabschluss'],
                                               [2, 'Grund-/Hauptschulabschluss'],
                                               [3, 'Realschule (Mittlere Reife)'],
                                               [4, 'Gymnasium (Abitur)'],
                                               [5, 'Abgeschlossene Ausbildung'],
                                               [6, 'Fachhochschulabschluss'],
                                               [7, 'Hochschule (Bachelor)'],
                                               [8, 'Hochschule (Master/Diplom)'],
                                               [9, 'Hochschule (Promotion)']],
                                      widget=widgets.RadioSelect)

    crt_wohnort = models.IntegerField(label='Wo wohnen Sie?', choices=[[1, 'Städtischer Raum'],
                                                                       [2, 'Ländlicher Raum'],
                                                                       [3, 'Vorstadt']],
                                      widget=widgets.RadioSelect)

    crt_einkommen = models.IntegerField(label='Wie hoch war Ihr monatliches Einkommen im Jahr 2017 Brutto?',
                                        choices=[[1, 'Bis unter 1000 €'],
                                                 [2, '1000 € bis unter 2000 €'],
                                                 [3, '2000 € bis unter 3000 €'],
                                                 [4, '3000 € bis unter 4000 €'],
                                                 [5, '4000 € bis unter 5000 €'],
                                                 [6, '5000 € bis unter 6000 €'],
                                                 [7, 'nu'],
                                                 [8, 'Keine Angabe']],
                                        widget=widgets.RadioSelect)

    crt_kommentar = models.LongStringField(label='Mit einem Klick auf "Weiter" schließen Sie das Experiment ab und kehren zu Amazon zurück. Falls Sie davor noch einen Kommentar zu diesem Experiment abgeben möchten, können Sie dies im folgenden Feld tun.',
                                           blank=True)

    crt_tpb_einstellung1 = models.IntegerField(label='Für mich persönlich ist die Bereitstellung von Flexibilität',
                                               choices=[[1, 'Extrem unvorteilhaft'],
                                                        [2, ''],
                                                        [3, ''],
                                                        [4, ''],
                                                        [5, ''],
                                                        [6, ''],
                                                        [7, 'Extrem vorteilhaft']],
                                               widget=widgets.RadioSelectHorizontal)

    crt_tpb_einstellung2 = models.IntegerField(label='Für mich persönlich ist die Bereitstellung von Flexibilität',
                                               choices=[[1, 'Extrem unerwünscht'],
                                                        [2, ''],
                                                        [3, ''],
                                                        [4, ''],
                                                        [5, ''],
                                                        [6, ''],
                                                        [7, 'Extrem erwünscht']],
                                               widget=widgets.RadioSelectHorizontal)

    crt_tpb_einstellung3 = models.IntegerField(label='Für mich persönlich ist die Bereitstellung von Flexibilität',
                                               choices=[[1, 'Extrem unangenehm'],
                                                        [2, ''],
                                                        [3, ''],
                                                        [4, ''],
                                                        [5, ''],
                                                        [6, ''],
                                                        [7, 'Extrem angenehm']],
                                               widget=widgets.RadioSelectHorizontal)

    crt_tpb_einstellung4 = models.IntegerField(label='Für mich persönlich ist die Bereitstellung von Flexibilität',
                                               choices=[[1, 'Extrem negativ'],
                                                        [2, ''],
                                                        [3, ''],
                                                        [4, ''],
                                                        [5, ''],
                                                        [6, ''],
                                                        [7, 'Extrem positiv']],
                                               widget=widgets.RadioSelectHorizontal)

    crt_tpb_einstellung5 = models.IntegerField(label='Für mich persönlich ist die Bereitstellung von Flexibilität',
                                               choices=[[1, 'Extrem unwahrscheinlich'],
                                                        [2, ''],
                                                        [3, ''],
                                                        [4, ''],
                                                        [5, ''],
                                                        [6, ''],
                                                        [7, 'Extrem wahrscheinlich']],
                                               widget=widgets.RadioSelectHorizontal)

    crt_tpb_normen1 = models.IntegerField(label='Die meisten Menschen, die mir wichtig sind, denken ich sollte flexibel laden',
                                               choices=[[1, 'Ich stimme überhaupt nicht zu'],
                                                        [2, ''],
                                                        [3, ''],
                                                        [4, ''],
                                                        [5, ''],
                                                        [6, ''],
                                                        [7, 'Ich stimme vollkommen zu']],
                                               widget=widgets.RadioSelectHorizontal)

    crt_tpb_normen2 = models.IntegerField(
        label='Wenn ich flexibel laden würden, würden die meisten Menschen, die mir wichtig sind ebenfalls flexibel laden',
        choices=[[1, 'Ich stimme überhaupt nicht zu'],
                 [2, ''],
                 [3, ''],
                 [4, ''],
                 [5, ''],
                 [6, ''],
                 [7, 'Ich stimme vollkommen zu']],
        widget=widgets.RadioSelectHorizontal)

    crt_tpb_normen3 = models.IntegerField(
        label='Menschen, deren Meinung ich schätze, würden es gut finden, wenn ich flexibel laden würde',
        choices=[[1, 'Ich stimme überhaupt nicht zu'],
                 [2, ''],
                 [3, ''],
                 [4, ''],
                 [5, ''],
                 [6, ''],
                 [7, 'Ich stimme vollkommen zu']],
        widget=widgets.RadioSelectHorizontal)

    crt_tpb_normen4 = models.IntegerField(
        label='Die meisten Menschen, die mir ähnlich sind laden flexibel',
        choices=[[1, 'Ich stimme überhaupt nicht zu'],
                 [2, ''],
                 [3, ''],
                 [4, ''],
                 [5, ''],
                 [6, ''],
                 [7, 'Ich stimme vollkommen zu']],
        widget=widgets.RadioSelectHorizontal)

    crt_tpb_normen5 = models.IntegerField(
        label='Meine Freunde fänden es gut, wenn ich flexibel lade',
        choices=[[1, 'Ich stimme überhaupt nicht zu'],
                 [2, ''],
                 [3, ''],
                 [4, ''],
                 [5, ''],
                 [6, ''],
                 [7, 'Ich stimme vollkommen zu']],
        widget=widgets.RadioSelectHorizontal)

    crt_tpb_kontrolle1 = models.IntegerField(
        label='Ich bin mir sicher, dass ich in der Lage bin ein System zum flexiblen Laden zu benutzen',
        choices=[[1, 'Ich stimme überhaupt nicht zu'],
                 [2, ''],
                 [3, ''],
                 [4, ''],
                 [5, ''],
                 [6, ''],
                 [7, 'Ich stimme vollkommen zu']],
        widget=widgets.RadioSelectHorizontal)

    crt_tpb_kontrolle2 = models.IntegerField(
        label='Ich bin mir sicher, dass ich, wenn ich es wollte, ein System zum flexiblen Laden verwenden kann',
        choices=[[1, 'Ich stimme überhaupt nicht zu'],
                 [2, ''],
                 [3, ''],
                 [4, ''],
                 [5, ''],
                 [6, ''],
                 [7, 'Ich stimme vollkommen zu']],
        widget=widgets.RadioSelectHorizontal)

    crt_tpb_kontrolle3 = models.IntegerField(
        label='Die Nutzung eines Systems zum flexiblen Laden ist einfach für mich',
        choices=[[1, 'Ich stimme überhaupt nicht zu'],
                 [2, ''],
                 [3, ''],
                 [4, ''],
                 [5, ''],
                 [6, ''],
                 [7, 'Ich stimme vollkommen zu']],
        widget=widgets.RadioSelectHorizontal)

    crt_tpb_kontrolle4 = models.IntegerField(
        label='Ob ich ein System zum flexiblen Laden benutze hängt nur von mir ab',
        choices=[[1, 'Ich stimme überhaupt nicht zu'],
                 [2, ''],
                 [3, ''],
                 [4, ''],
                 [5, ''],
                 [6, ''],
                 [7, 'Ich stimme vollkommen zu']],
        widget=widgets.RadioSelectHorizontal)

    crt_tpb_kontrolle5 = models.IntegerField(
        label='Ich kann die Entscheidung ein System zum flexiblen Laden zu verwenden nicht selbstständig kontrollieren',
        choices=[[1, 'Ich stimme überhaupt nicht zu'],
                 [2, ''],
                 [3, ''],
                 [4, ''],
                 [5, ''],
                 [6, ''],
                 [7, 'Ich stimme vollkommen zu']],
        widget=widgets.RadioSelectHorizontal)

    crt_tpb_absicht1 = models.IntegerField(
        label='Ich bin willens flexibles Laden zu verwenden',
        choices=[[1, 'Ich stimme überhaupt nicht zu'],
                 [2, ''],
                 [3, ''],
                 [4, ''],
                 [5, ''],
                 [6, ''],
                 [7, 'Ich stimme vollkommen zu']],
        widget=widgets.RadioSelectHorizontal)

    crt_tpb_absicht2 = models.IntegerField(
        label='Ich beabsichtige flexibles Laden zu verwenden',
        choices=[[1, 'Ich stimme überhaupt nicht zu'],
                 [2, ''],
                 [3, ''],
                 [4, ''],
                 [5, ''],
                 [6, ''],
                 [7, 'Ich stimme vollkommen zu']],
        widget=widgets.RadioSelectHorizontal)

    crt_tpb_absicht3 = models.IntegerField(
        label='Ich plane flexibles Laden zu verwenden',
        choices=[[1, 'Ich stimme überhaupt nicht zu'],
                 [2, ''],
                 [3, ''],
                 [4, ''],
                 [5, ''],
                 [6, ''],
                 [7, 'Ich stimme vollkommen zu']],
        widget=widgets.RadioSelectHorizontal)

    crt_attention = models.IntegerField(
        label='Bitte wählen Sie bei dieser Frage "Ich stimme vollkommen zu" aus',
        choices=[[1, 'Ich stimme überhaupt nicht zu'],
                 [2, ''],
                 [3, ''],
                 [4, ''],
                 [5, ''],
                 [6, ''],
                 [7, 'Ich stimme vollkommen zu']],
        widget=widgets.RadioSelectHorizontal
    )