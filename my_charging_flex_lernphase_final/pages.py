from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Lernphase(Page):
    form_model = 'player'
    form_fields = ['mindestreichweite_sofort',
                   'mindestreichweite_spaeter',
                   'gewuenschte_abfahrt']

    def before_next_page(self):

        self.player.charge_up1()

        self.player.charge_up2()

        self.player.charge_up3()

        # self.player.set_mindestreichweiten()

        self.player.set_ladeflexibilitaet()

        self.player.set_payoff1()

        self.player.set_payoff2()

        self.player.set_payoff3()

        self.player.calculate_hours1()

        self.player.calculate_minutes1()

        self.player.calculate_hours2()

        self.player.calculate_minutes2()

        self.player.calculate_hours3()

        self.player.calculate_minutes3()

        self.player.calculate_gewuenschte_abfahrt_hours()

        self.player.calculate_gewuenscht_abfahrt_minutes()

class HinweisNächstePhase(Page):

    def is_displayed(self):
        return self.round_number == 1

    def before_next_page(self):
        self.player.reset_payoff()


class Ergebnisse(Page):
    pass


page_sequence = [
    Lernphase,
    Ergebnisse,
    HinweisNächstePhase
]
