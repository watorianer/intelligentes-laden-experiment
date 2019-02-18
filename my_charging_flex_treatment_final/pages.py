from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Treatment(Page):
    form_model = 'player'
    form_fields = ['mindestreichweite_sofort',
                   'mindestreichweite_spaeter',
                   'gewuenschte_abfahrt']

    def before_next_page(self):

        self.player.charge_up()

        self.player.set_ladeflexibilitaet()

        self.player.set_payoff()

        self.player.calculate_minutes()

        self.player.calculate_hours()

        self.player.calculate_gewuenschte_abfahrt_hours()

        self.player.calculate_gewuenscht_abfahrt_minutes()


class ZufriedenheitVorRealisation(Page):
    form_model = 'player'
    form_fields = ['crt_zufriedenheit_vor_realisation',
                   'crt_grafik_verstaendnis']

class Ergebnisse(Page):
    def before_next_page(self):
        self.player.reset_payoff()

class ZufriedenheitNachRealisation(Page):
    form_model = 'player'
    form_fields = ['crt_zufriedenheit_nach_Realisation']


page_sequence = [
    Treatment,
    ZufriedenheitVorRealisation,
    Ergebnisse,
    ZufriedenheitNachRealisation
]
