from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class Einleitung(Page):
    pass


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Verständnis(Page):
    form_model = 'player'
    form_fields = ['crt_vorteile',
                   'crt_nachteile',
                   'crt_abfahrt',
                   'crt_ladeflex',
                   'crt_unzureichend']


    def crt_vorteile_choices(self):
        choices = ['Verbesserte Stabilität des Stromnetzes', 'Verringerte Ladezeiten',
                   'Verringerter Planungsaufwand']
        random.shuffle(choices)
        return choices

    def crt_vorteile_error_message(self, value):
        if value == 'Verringerte Ladezeiten':
            return 'Diese Antwort ist leider falsch. Bei Einsatz intelligenten Ladens erhöht sich normalerweise die Ladezeit. Dafür verbessert sich jedoch die Stabilität des Stromnetzes, der Anteil erneuerbarer Energien beim Laden der Batterie ist höher und die Batterie kann billiger aufladen werden'
        elif value == 'Verringerter Planungsaufwand':
            return 'Diese Antwort ist leider falsch. Da sich die Zeit, die zum Aufladen der Batterie benötigt wird erhöht, muss ein Nutzer genauer planen wann er ein Auto für die nächste Fahrt benötigt. Normalerweise erhöht sich also der Planungsaufwand des Nutzers'


    def crt_nachteile_choices(self):
        choices = ['Erhöhte Ladekosten', 'Verringerter Anteil erneuerbarer Energien', 'Einschränkung in der Mobilitätsflexibilität']
        random.shuffle(choices)
        return choices

    def crt_nachteile_error_message(self, value):
        if value == 'Erhöhte Ladekosten':
            return 'Diese Antwort ist leider falsch. Beim Einsatz von intelligenten Laden wird die Batterie des E-PKWs genau dann besonders stark geladen, wenn viel Strom im Stromnetz verfügbar ist. Ist viel Strom verfügbar, sinken die Kosten dafür pro Einheit. Insgesamt sollten sich also die Kosten für den Ladevorgang verringern'
        if value == 'Verringerter Anteil erneuerbarer Energien':
            return 'Diese Antwort ist leider falsch. Wissenschaftliche Studien haben gezeigt, dass sich beim Einsatz von intelligenten Laden der Anteil erneuerbarer Energien beim Ladevorgang erhöht'


    def crt_abfahrt_choices(self):
        choices = ['Der Ladevorgang wird fortgesetzt', 'Der Ladevorgang wird abgebrochen']
        random.shuffle(choices)
        return choices

    def crt_abfahrt_error_message(self, value):
        if value == 'Der Ladevorgang wird fortgesetzt':
            return 'Diese Antwort ist leider falsch. Sollte das Experiment bestimmen, dass sie früher als von Ihnen gewünscht abfahren müssen, also die vom Experiment bestimmte Abfahrtszeit vor der von Ihnen gewünschten Abfahrtszeit liegt, wird der Ladevorgang abgebrochen sobald die vom Experiment realisierte Uhrzeit erreicht wurde'



    def crt_ladeflex_choices(self):
        choices = ['Ihnen werden Punkte in Höhe der Ladeflexibilität abgezogen', 'Nichts', 'Sie erhalten Punkte in Höhe der Ladeflexibilität']
        random.shuffle(choices)
        return choices

    def crt_ladeflex_error_message(self, value):
        if value == 'Ihnen werden Punkte in Höhe der Ladeflexibilität abgezogen':
            return 'Diese Antwort ist leider falsch. Sollten die aufgeladenen Kilometer ausreichen um die Strecke abfahren zu können erhalten Sie Punkte. Je mehr Ladeflexibilität Sie freigegeben haben, desto mehr Punkte erhalten Sie'
        if value == 'Nichts':
            return 'Diese Antwort ist leider falsch. Sollten die aufgeladenen Kilometer ausreichen um die Strecke abfahren zu können erhalten Sie Punkte. Je mehr Ladeflexibilität Sie freigegeben haben, desto mehr Punkte erhalten Sie'


    def crt_unzureichend_choices(self):
        choices = ['Nichts', 'Sie erhalten Punkte in Höhe der Ladeflexibilität', 'Ihnen werden Punkte in Höhe der Ladeflexibilität abgezogen']
        random.shuffle(choices)
        return choices

    def crt_unzureichend_error_message(self, value):
        if value == 'Sie erhalten Punkte in Höhe der Ladeflexibilität':
            return 'Diese Antwort ist leider falsch. Sollten die aufgeladenen Kilometer nicht ausreichen um die Strecke abfahren zu können werden Ihnen Punkte abgezogen. Je mehr Ladeflexibilität Sie freigegeben haben, desto mehr Punkte werden Ihnen abgezogen'
        if value == 'Nichts':
            return 'Diese Antwort ist leider falsch. Sollten die aufgeladenen Kilometer nicht ausreichen um die Strecke abfahren zu können werden Ihnen Punkte abgezogen. Je mehr Ladeflexibilität Sie freigegeben haben, desto mehr Punkte werden Ihnen abgezogen'

class Einverständnis(Page):
    pass

page_sequence = [
    Einleitung,
    Einverständnis,
    Verständnis
]
