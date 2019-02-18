from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import itertools


author = 'Martin Wolff'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'my_charging_flex_einleitung_final'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):

    def creating_session(self):

        treatment_groups = itertools.cycle(['control', 'dss', 'nudge'])
        for player in self.get_players():
            player.participant.vars['role'] = next(treatment_groups)
            player.treatment_group = player.participant.vars['role']


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    crt_vorteile = models.StringField(
        choices=['Verbesserte Stabilität des Stromnetzes', 'Verringerte Ladezeiten', 'Verringerter Planungsaufwand'],
        label='Was ist ein Vorteil intelligenten Ladens?',
        widget=widgets.RadioSelect
    )

    crt_nachteile = models.StringField(
        choices=['Erhöhte Ladekosten', 'Verringerter Anteil erneuerbarer Energien', 'Einschränkung in der Mobilitätsflexibilität'],
        label='Was ist ein Nachteil intelligenten Ladens?',
        widget=widgets.RadioSelect
    )

    crt_abfahrt = models.StringField(
        choices=['Der Ladevorgang wird fortgesetzt', 'Der Ladevorgang wird abgebrochen'],
        label='Was passiert, wenn die vom Experiment realisierte Abfahrtszeit erreicht wird, während der Ladevorgang noch läuft?',
        widget=widgets.RadioSelect
    )


    crt_ladeflex = models.StringField(
        choices=['Sie erhalten Punkte in Höhe der Ladeflexibilität', 'Nichts', 'Ihnen werden Punkte in Höhe der Ladeflexibilität abgezogen'],
        label='Was passiert, wenn die geladenen Kilometer am nächsten Tag ausreichen?',
        widget=widgets.RadioSelect
    )

    crt_unzureichend = models.StringField(
        choices=['Nichts', 'Sie erhalten Punkte in Höhe der Ladeflexibilität', 'Ihnen werden Punkte in Höhe der Ladeflexibilität abgezogen'],
        label='Was passiert, wenn die geladenen Kilometer am nächsten Tag nicht ausreichen?',
        widget=widgets.RadioSelect
    )

    treatment_group = models.StringField()


