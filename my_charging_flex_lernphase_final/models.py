from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'my_charging_flex_lernphase_final'
    players_per_group = None
    num_rounds = 1

    max_kilometer = 250
    ladestand = 0
    aktuell_kilometer = 0
    max_laderate = 25

    to_drive1 = 320
    to_drive2 = 54.8
    to_drive3 = 6

    abfahrt1 = 0.5
    abfahrt2 = 7.25
    abfahrt3 = 20.25

    dss = 'dss'


class Subsession(BaseSubsession):

    def creating_session(self):
        for player in self.get_players():
            player.treatment_group = player.participant.vars['role']


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    mindestreichweite_sofort = models.FloatField(
        label='Bitte geben Sie Ihre Mindestreichweite sofort an',
        widget=widgets.Slider(attrs={'step': '1'}),
        min=Constants.aktuell_kilometer,
        max=Constants.max_kilometer
    )

    mindestreichweite_spaeter = models.FloatField(
        label='Bitte geben Sie Ihre Mindestreichweite später an',
        widget=widgets.Slider(attrs={'step': '1'}),
        min=Constants.aktuell_kilometer,
        max=Constants.max_kilometer
    )

    gewuenschte_abfahrt = models.FloatField(
        label='Bitte geben Sie an bis wann die Mindestreichweite später geladen sein soll',
        widget=widgets.Slider(attrs={'step': '0.5'}),
        min=0.5,
        max=24
    )

    ladeflexibilitaet = models.FloatField()


    geladene_kilometer1 = models.FloatField()

    geladene_kilometer2 = models.FloatField()

    geladene_kilometer3 = models.FloatField()


    treatment_group = models.StringField()


    minutes1 = models.IntegerField()

    hours1 = models.IntegerField()


    minutes2 = models.IntegerField()

    hours2 = models.IntegerField()


    minutes3 = models.IntegerField()

    hours3 = models.IntegerField()


    gewuenschte_abfahrt_minutes = models.IntegerField()

    gewuenschte_abfahrt_hours = models.IntegerField()


    punkte1 = models.IntegerField()

    punkte2 = models.IntegerField()

    punkte3 = models.IntegerField()



    def charge_up1(self):
        # Erst muss ausgerechnet werden wie lange es dauert die gewünschte Mindestreichweite sofort aufzuladen. Sollte die Zeit nicht ausreichen wird die gewünschte Abfahrt genommen
        mindestreichweite_sofort_dauer = min(self.gewuenschte_abfahrt, (
                    self.mindestreichweite_sofort - Constants.aktuell_kilometer) / Constants.max_laderate)
        # dieser Block ist neu:
        if Constants.abfahrt1 >= self.gewuenschte_abfahrt:
            # Die gewünschte Abfahrt ist kleiner gleich der gezogenen Abfahrt, der Ladevorgang kann also wie geplant vorgenommen werden
            if mindestreichweite_sofort_dauer == self.gewuenschte_abfahrt:
                # Die gewünschte Mindestreichweite sofort aufzuladen dauert länger oder genauso lange wie das Auto steht. Es wird daher die gesamte Standzeit mit maximaler Laderate geladen. Die Ladeflexibilität sollte bei diesem Fall bei 0 liegen.
                self.geladene_kilometer1 = round(Constants.aktuell_kilometer + (
                            self.gewuenschte_abfahrt * Constants.max_laderate), 2)
            else:
                # Die gewünschte Mindestreichweite sofort aufzuladen nimmt nicht die gesamte Standdauer in Anspruch
                if self.mindestreichweite_sofort >= self.mindestreichweite_spaeter:
                    # Erst der einfache Fall: die geforderte Mindestreichweite sofort ist größer als die geforderte Mindestreichweite später. Es werden also einfach so viele Kilometer geladen wie in der Mindestreichweite sofort gefordert
                    self.geladene_kilometer1 = self.mindestreichweite_sofort
                else:
                    # Jetzt der etwas kompliziertere Fall: Die Mindestreichweite sofort wird aufgeladen, aber die geforderte Mindestreichweite später ist größer. Nach Erreichen der Mindestreichweite sofort wird also noch mit einer verringerten Laderate geladen.
                    gewichtungsfaktor_zaehler = (self.mindestreichweite_spaeter - self.mindestreichweite_sofort) / (
                                self.gewuenschte_abfahrt - mindestreichweite_sofort_dauer)  # wir wissen, dass die mindestreichweite später größer ist als die mindestreichweite sofort, muss daher größer 0 sein
                    # Nenner kann nicht 0 werden, da bereits festgestellt wurde, dass die Mindestreichweite sofort aufzuladen nicht die gesamte Standdauer benötigt
                    # Insgesamt (die Variable die hier mit gewichtungsfaktor_zaehler bezeichnet wird) wird hier also berechnet wie viele Kilometer pro Stunde geladen werden müssen um die Mindestreichweite später vor Ende der Standzeit zu erreichen
                    gewichtungsfaktor = gewichtungsfaktor_zaehler / Constants.max_laderate
                    # Der Gewichtungsfaktor überprüft ob die maximale Laderate ausreicht um die noch zu ladenden Kilometer aufzuladen. Ist er > 1 reicht die Zeit nicht aus. Es muss also die gesamte restliche Zeit mit maximaler Laderate geladen werden
                    if gewichtungsfaktor <= 1:
                        # Erst der einfache Fall: der gewichtungsfaktor ist kleiner oder gleich 1: damit reicht die Zeit aus um das Autoa auf die geforderte Mindestreichweite später zu laden (auch wenn es sein kann, dass der Gewichtungsfaktor genau 1 ist und somit die gesamte Zeit mit maximaler Laderate aufgeladen werden muss - die Ladeflexibilität also 0 ist)
                        self.geladene_kilometer1 = self.mindestreichweite_spaeter
                    else:
                        # Hier reicht die restliche Zeit nicht aus. Es wird daher erst berechnet wie viel Zeit nach erreichen der Mindestreichweite sofort noch übrig ist
                        restliche_zeit = self.gewuenschte_abfahrt - mindestreichweite_sofort_dauer
                        # Diese verbleibende Zeit wird mit maximaler Laderate geladen
                        self.geladene_kilometer1 = round(self.mindestreichweite_sofort + (
                                    restliche_zeit * Constants.max_laderate), 2)
        else:
            # Die gewünschte Abfahrt ist liegt nach der tatsächlichen Abfahrtszeit. Es kann also vorkommen, dass der Ladevorgang unterbrochen werden muss
            # Erst muss ausgerechnet werden wie lange es dauert die gewünschte Mindestreichweite sofort aufzuladen. Falls die Mindestreichweite sofort nicht in der tatsächlichen (hier: gezogenen) Standdauer erreicht werden kann wird dies signalisiert indem die dauer auf die (hier:gezogene) Standdauer gesetzt wird.
            mindestreichweite_sofort_dauer_drawn = min(Constants.abfahrt1, (
                        self.mindestreichweite_sofort - Constants.aktuell_kilometer) / Constants.max_laderate)
            if mindestreichweite_sofort_dauer == self.gewuenschte_abfahrt:
                # Die gewünschte Mindestreichweite kann nicht erreicht werden. Allerdings muss das Auto jetzt sogar noch früher los. Deswegen wird hier die restliche Zeit nicht über die gewünschte Abfahrtszeit bestimmt sondern über die tatsächliche, gezogene Abfahrtszeit
                self.geladene_kilometer1 = round(Constants.aktuell_kilometer + (Constants.abfahrt1 * Constants.max_laderate), 2)
            else:
                # Die Mindestreichweite sofort aufzuladen würde nicht die gesamte Standdauer in Anspruch nehmen.
                if self.mindestreichweite_sofort >= self.mindestreichweite_spaeter:
                    # Erst der einfache Fall: die gewünschte Mindestreichweite sofort ist größer als die Mindestreichweite später. Die Mindestreichweite später kann also ignoriert werden.
                    if mindestreichweite_sofort_dauer > mindestreichweite_sofort_dauer_drawn:
                        # Dauert es länger die Mindestreichweite sofort zu laden als Zeit bis zur tatsächlichen Abfahrt zur Verfügung steht, wird der Ladeprozess unterbrochen sobald die tatsächliche Abfahrtszeit erreicht ist
                        self.geladene_kilometer1 = round(Constants.aktuell_kilometer + (
                                    Constants.abfahrt1 * Constants.max_laderate), 2)
                    else:
                        # Die Mindesterichweite sofort dauer und die Mindestreichweite sofort dauer drawn sollten jetzt gleich sein
                        # Die Zeit sollte auch mit dem früheren Abfahrtstermin ausreichen die geforderte Mindestreichweite sofort zu erreichen. Zusätzlich muss nicht weiter geladen werden.
                        self.geladene_kilometer1 = self.mindestreichweite_sofort
                else:
                    # Die Mindestreichweite später kann nicht einfach ignoriert werden
                    gewichtungsfaktor_zaehler = (self.mindestreichweite_spaeter - self.mindestreichweite_sofort) / (
                                self.gewuenschte_abfahrt - mindestreichweite_sofort_dauer)
                    gewichtungsfaktor = gewichtungsfaktor_zaehler / Constants.max_laderate
                    if gewichtungsfaktor <= 1:
                        # Erst der einfachere Fall: Der Gewichtungsfaktor ist kleiner gleich 1, die restliche Zeit (gemessen an der gewünschten Abfahrtszeit) reicht also aus um die Mindestreichweite später zu laden
                        if mindestreichweite_sofort_dauer_drawn == Constants.abfahrt1:
                            # Die gezogene Abfahrtszeit liegt so, dass noch nicht einmal die Mindestreichweite sofort aufgelden werden kann. Das Auto denkt aber es hat Zeit erst die Mindestreichweite sofort zu laden und dann noch die Mindestreichweite später
                            self.geladene_kilometer1 = round(Constants.aktuell_kilometer + (
                                        Constants.abfahrt1 * Constants.max_laderate), 2)
                        else:
                            # Die gezogene Abfahrtszeit reicht aus um die gewünschte Mindestreichweite sofort aufzuladen
                            # Reicht die Zeit auch um die Mindestreichweite später aufzuladen (Gewichtungfaktor <= 1) wird angenommen, dass die gesamte Restzeit mit einer verringerten Laderate geladen wird. D.h. hier wird erst die Mindestreichweite sofort aufgeladen um dann mit verringerter Laderate die restlich Zeit aufzuladen
                            restliche_zeit = Constants.abfahrt1 - mindestreichweite_sofort_dauer_drawn
                            self.geladene_kilometer1 = round(self.mindestreichweite_sofort + (
                                        restliche_zeit * gewichtungsfaktor_zaehler), 2)
                    else:
                        # Der Gewichtungsfaktor ist > 1, also würde die urpsrüngliche Zeit nicht ausreichen um die Mindestreichweite später zu laden
                        # Hier würde auch normalerweise die gesamte Standdauer über mit der maximalen Laderate aufgeladen werden. Also muss nicht erst noch überprüft werden ob die Standdauer ausreicht um die Mindestreichweite sofort aufzuladen
                        self.geladene_kilometer1 = round(Constants.aktuell_kilometer + (
                                    Constants.abfahrt1 * Constants.max_laderate), 2)


    def charge_up2(self):
        # Erst muss ausgerechnet werden wie lange es dauert die gewünschte Mindestreichweite sofort aufzuladen. Sollte die Zeit nicht ausreichen wird die gewünschte Abfahrt genommen
        mindestreichweite_sofort_dauer = min(self.gewuenschte_abfahrt, (
                    self.mindestreichweite_sofort - Constants.aktuell_kilometer) / Constants.max_laderate)
        # dieser Block ist neu:
        if Constants.abfahrt2 >= self.gewuenschte_abfahrt:
            # Die gewünschte Abfahrt ist kleiner gleich der gezogenen Abfahrt, der Ladevorgang kann also wie geplant vorgenommen werden
            if mindestreichweite_sofort_dauer == self.gewuenschte_abfahrt:
                # Die gewünschte Mindestreichweite sofort aufzuladen dauert länger oder genauso lange wie das Auto steht. Es wird daher die gesamte Standzeit mit maximaler Laderate geladen. Die Ladeflexibilität sollte bei diesem Fall bei 0 liegen.
                self.geladene_kilometer2 = round(Constants.aktuell_kilometer + (
                            self.gewuenschte_abfahrt * Constants.max_laderate), 2)
            else:
                # Die gewünschte Mindestreichweite sofort aufzuladen nimmt nicht die gesamte Standdauer in Anspruch
                if self.mindestreichweite_sofort >= self.mindestreichweite_spaeter:
                    # Erst der einfache Fall: die geforderte Mindestreichweite sofort ist größer als die geforderte Mindestreichweite später. Es werden also einfach so viele Kilometer geladen wie in der Mindestreichweite sofort gefordert
                    self.geladene_kilometer2 = self.mindestreichweite_sofort
                else:
                    # Jetzt der etwas kompliziertere Fall: Die Mindestreichweite sofort wird aufgeladen, aber die geforderte Mindestreichweite später ist größer. Nach Erreichen der Mindestreichweite sofort wird also noch mit einer verringerten Laderate geladen.
                    gewichtungsfaktor_zaehler = (self.mindestreichweite_spaeter - self.mindestreichweite_sofort) / (
                                self.gewuenschte_abfahrt - mindestreichweite_sofort_dauer)  # wir wissen, dass die mindestreichweite später größer ist als die mindestreichweite sofort, muss daher größer 0 sein
                    # Nenner kann nicht 0 werden, da bereits festgestellt wurde, dass die Mindestreichweite sofort aufzuladen nicht die gesamte Standdauer benötigt
                    # Insgesamt (die Variable die hier mit gewichtungsfaktor_zaehler bezeichnet wird) wird hier also berechnet wie viele Kilometer pro Stunde geladen werden müssen um die Mindestreichweite später vor Ende der Standzeit zu erreichen
                    gewichtungsfaktor = gewichtungsfaktor_zaehler / Constants.max_laderate
                    # Der Gewichtungsfaktor überprüft ob die maximale Laderate ausreicht um die noch zu ladenden Kilometer aufzuladen. Ist er > 1 reicht die Zeit nicht aus. Es muss also die gesamte restliche Zeit mit maximaler Laderate geladen werden
                    if gewichtungsfaktor <= 1:
                        # Erst der einfache Fall: der gewichtungsfaktor ist kleiner oder gleich 1: damit reicht die Zeit aus um das Autoa auf die geforderte Mindestreichweite später zu laden (auch wenn es sein kann, dass der Gewichtungsfaktor genau 1 ist und somit die gesamte Zeit mit maximaler Laderate aufgeladen werden muss - die Ladeflexibilität also 0 ist)
                        self.geladene_kilometer2 = self.mindestreichweite_spaeter
                    else:
                        # Hier reicht die restliche Zeit nicht aus. Es wird daher erst berechnet wie viel Zeit nach erreichen der Mindestreichweite sofort noch übrig ist
                        restliche_zeit = self.gewuenschte_abfahrt - mindestreichweite_sofort_dauer
                        # Diese verbleibende Zeit wird mit maximaler Laderate geladen
                        self.geladene_kilometer2 = round(self.mindestreichweite_sofort + (
                                    restliche_zeit * Constants.max_laderate), 2)
        else:
            # Die gewünschte Abfahrt ist liegt nach der tatsächlichen Abfahrtszeit. Es kann also vorkommen, dass der Ladevorgang unterbrochen werden muss
            # Erst muss ausgerechnet werden wie lange es dauert die gewünschte Mindestreichweite sofort aufzuladen. Falls die Mindestreichweite sofort nicht in der tatsächlichen (hier: gezogenen) Standdauer erreicht werden kann wird dies signalisiert indem die dauer auf die (hier:gezogene) Standdauer gesetzt wird.
            mindestreichweite_sofort_dauer_drawn = min(Constants.abfahrt2, (
                        self.mindestreichweite_sofort - Constants.aktuell_kilometer) / Constants.max_laderate)
            if mindestreichweite_sofort_dauer == self.gewuenschte_abfahrt:
                # Die gewünschte Mindestreichweite kann nicht erreicht werden. Allerdings muss das Auto jetzt sogar noch früher los. Deswegen wird hier die restliche Zeit nicht über die gewünschte Abfahrtszeit bestimmt sondern über die tatsächliche, gezogene Abfahrtszeit
                self.geladene_kilometer2 = round(Constants.aktuell_kilometer + (Constants.abfahrt2 * Constants.max_laderate), 2)
            else:
                # Die Mindestreichweite sofort aufzuladen würde nicht die gesamte Standdauer in Anspruch nehmen.
                if self.mindestreichweite_sofort >= self.mindestreichweite_spaeter:
                    # Erst der einfache Fall: die gewünschte Mindestreichweite sofort ist größer als die Mindestreichweite später. Die Mindestreichweite später kann also ignoriert werden.
                    if mindestreichweite_sofort_dauer > mindestreichweite_sofort_dauer_drawn:
                        # Dauert es länger die Mindestreichweite sofort zu laden als Zeit bis zur tatsächlichen Abfahrt zur Verfügung steht, wird der Ladeprozess unterbrochen sobald die tatsächliche Abfahrtszeit erreicht ist
                        self.geladene_kilometer2 = round(Constants.aktuell_kilometer + (
                                    Constants.abfahrt2 * Constants.max_laderate), 2)
                    else:
                        # Die Mindesterichweite sofort dauer und die Mindestreichweite sofort dauer drawn sollten jetzt gleich sein
                        # Die Zeit sollte auch mit dem früheren Abfahrtstermin ausreichen die geforderte Mindestreichweite sofort zu erreichen. Zusätzlich muss nicht weiter geladen werden.
                        self.geladene_kilometer2 = self.mindestreichweite_sofort
                else:
                    # Die Mindestreichweite später kann nicht einfach ignoriert werden
                    gewichtungsfaktor_zaehler = (self.mindestreichweite_spaeter - self.mindestreichweite_sofort) / (
                                self.gewuenschte_abfahrt - mindestreichweite_sofort_dauer)
                    gewichtungsfaktor = gewichtungsfaktor_zaehler / Constants.max_laderate
                    if gewichtungsfaktor <= 1:
                        # Erst der einfachere Fall: Der Gewichtungsfaktor ist kleiner gleich 1, die restliche Zeit (gemessen an der gewünschten Abfahrtszeit) reicht also aus um die Mindestreichweite später zu laden
                        if mindestreichweite_sofort_dauer_drawn == Constants.abfahrt2:
                            # Die gezogene Abfahrtszeit liegt so, dass noch nicht einmal die Mindestreichweite sofort aufgelden werden kann. Das Auto denkt aber es hat Zeit erst die Mindestreichweite sofort zu laden und dann noch die Mindestreichweite später
                            self.geladene_kilometer2 = round(Constants.aktuell_kilometer + (
                                        Constants.abfahrt2 * Constants.max_laderate), 2)
                        else:
                            # Die gezogene Abfahrtszeit reicht aus um die gewünschte Mindestreichweite sofort aufzuladen
                            # Reicht die Zeit auch um die Mindestreichweite später aufzuladen (Gewichtungfaktor <= 1) wird angenommen, dass die gesamte Restzeit mit einer verringerten Laderate geladen wird. D.h. hier wird erst die Mindestreichweite sofort aufgeladen um dann mit verringerter Laderate die restlich Zeit aufzuladen
                            restliche_zeit = Constants.abfahrt2 - mindestreichweite_sofort_dauer_drawn
                            self.geladene_kilometer2 = round(self.mindestreichweite_sofort + (
                                        restliche_zeit * gewichtungsfaktor_zaehler), 2)
                    else:
                        # Der Gewichtungsfaktor ist > 1, also würde die urpsrüngliche Zeit nicht ausreichen um die Mindestreichweite später zu laden
                        # Hier würde auch normalerweise die gesamte Standdauer über mit der maximalen Laderate aufgeladen werden. Also muss nicht erst noch überprüft werden ob die Standdauer ausreicht um die Mindestreichweite sofort aufzuladen
                        self.geladene_kilometer2 = round(Constants.aktuell_kilometer + (
                                    Constants.abfahrt2 * Constants.max_laderate), 2)


    def charge_up3(self):
        # Erst muss ausgerechnet werden wie lange es dauert die gewünschte Mindestreichweite sofort aufzuladen. Sollte die Zeit nicht ausreichen wird die gewünschte Abfahrt genommen
        mindestreichweite_sofort_dauer = min(self.gewuenschte_abfahrt, (
                    self.mindestreichweite_sofort - Constants.aktuell_kilometer) / Constants.max_laderate)
        # dieser Block ist neu:
        if Constants.abfahrt3 >= self.gewuenschte_abfahrt:
            # Die gewünschte Abfahrt ist kleiner gleich der gezogenen Abfahrt, der Ladevorgang kann also wie geplant vorgenommen werden
            if mindestreichweite_sofort_dauer == self.gewuenschte_abfahrt:
                # Die gewünschte Mindestreichweite sofort aufzuladen dauert länger oder genauso lange wie das Auto steht. Es wird daher die gesamte Standzeit mit maximaler Laderate geladen. Die Ladeflexibilität sollte bei diesem Fall bei 0 liegen.
                self.geladene_kilometer3 = round(Constants.aktuell_kilometer + (
                            self.gewuenschte_abfahrt * Constants.max_laderate), 2)
            else:
                # Die gewünschte Mindestreichweite sofort aufzuladen nimmt nicht die gesamte Standdauer in Anspruch
                if self.mindestreichweite_sofort >= self.mindestreichweite_spaeter:
                    # Erst der einfache Fall: die geforderte Mindestreichweite sofort ist größer als die geforderte Mindestreichweite später. Es werden also einfach so viele Kilometer geladen wie in der Mindestreichweite sofort gefordert
                    self.geladene_kilometer3 = self.mindestreichweite_sofort
                else:
                    # Jetzt der etwas kompliziertere Fall: Die Mindestreichweite sofort wird aufgeladen, aber die geforderte Mindestreichweite später ist größer. Nach Erreichen der Mindestreichweite sofort wird also noch mit einer verringerten Laderate geladen.
                    gewichtungsfaktor_zaehler = (self.mindestreichweite_spaeter - self.mindestreichweite_sofort) / (
                                self.gewuenschte_abfahrt - mindestreichweite_sofort_dauer)  # wir wissen, dass die mindestreichweite später größer ist als die mindestreichweite sofort, muss daher größer 0 sein
                    # Nenner kann nicht 0 werden, da bereits festgestellt wurde, dass die Mindestreichweite sofort aufzuladen nicht die gesamte Standdauer benötigt
                    # Insgesamt (die Variable die hier mit gewichtungsfaktor_zaehler bezeichnet wird) wird hier also berechnet wie viele Kilometer pro Stunde geladen werden müssen um die Mindestreichweite später vor Ende der Standzeit zu erreichen
                    gewichtungsfaktor = gewichtungsfaktor_zaehler / Constants.max_laderate
                    # Der Gewichtungsfaktor überprüft ob die maximale Laderate ausreicht um die noch zu ladenden Kilometer aufzuladen. Ist er > 1 reicht die Zeit nicht aus. Es muss also die gesamte restliche Zeit mit maximaler Laderate geladen werden
                    if gewichtungsfaktor <= 1:
                        # Erst der einfache Fall: der gewichtungsfaktor ist kleiner oder gleich 1: damit reicht die Zeit aus um das Autoa auf die geforderte Mindestreichweite später zu laden (auch wenn es sein kann, dass der Gewichtungsfaktor genau 1 ist und somit die gesamte Zeit mit maximaler Laderate aufgeladen werden muss - die Ladeflexibilität also 0 ist)
                        self.geladene_kilometer3 = self.mindestreichweite_spaeter
                    else:
                        # Hier reicht die restliche Zeit nicht aus. Es wird daher erst berechnet wie viel Zeit nach erreichen der Mindestreichweite sofort noch übrig ist
                        restliche_zeit = self.gewuenschte_abfahrt - mindestreichweite_sofort_dauer
                        # Diese verbleibende Zeit wird mit maximaler Laderate geladen
                        self.geladene_kilometer3 = round(self.mindestreichweite_sofort + (
                                    restliche_zeit * Constants.max_laderate), 2)
        else:
            # Die gewünschte Abfahrt ist liegt nach der tatsächlichen Abfahrtszeit. Es kann also vorkommen, dass der Ladevorgang unterbrochen werden muss
            # Erst muss ausgerechnet werden wie lange es dauert die gewünschte Mindestreichweite sofort aufzuladen. Falls die Mindestreichweite sofort nicht in der tatsächlichen (hier: gezogenen) Standdauer erreicht werden kann wird dies signalisiert indem die dauer auf die (hier:gezogene) Standdauer gesetzt wird.
            mindestreichweite_sofort_dauer_drawn = min(Constants.abfahrt3, (
                        self.mindestreichweite_sofort - Constants.aktuell_kilometer) / Constants.max_laderate)
            if mindestreichweite_sofort_dauer == self.gewuenschte_abfahrt:
                # Die gewünschte Mindestreichweite kann nicht erreicht werden. Allerdings muss das Auto jetzt sogar noch früher los. Deswegen wird hier die restliche Zeit nicht über die gewünschte Abfahrtszeit bestimmt sondern über die tatsächliche, gezogene Abfahrtszeit
                self.geladene_kilometer3 = round(Constants.aktuell_kilometer + (Constants.abfahrt3 * Constants.max_laderate), 2)
            else:
                # Die Mindestreichweite sofort aufzuladen würde nicht die gesamte Standdauer in Anspruch nehmen.
                if self.mindestreichweite_sofort >= self.mindestreichweite_spaeter:
                    # Erst der einfache Fall: die gewünschte Mindestreichweite sofort ist größer als die Mindestreichweite später. Die Mindestreichweite später kann also ignoriert werden.
                    if mindestreichweite_sofort_dauer > mindestreichweite_sofort_dauer_drawn:
                        # Dauert es länger die Mindestreichweite sofort zu laden als Zeit bis zur tatsächlichen Abfahrt zur Verfügung steht, wird der Ladeprozess unterbrochen sobald die tatsächliche Abfahrtszeit erreicht ist
                        self.geladene_kilometer3 = round(Constants.aktuell_kilometer + (
                                    Constants.abfahrt3 * Constants.max_laderate), 2)
                    else:
                        # Die Mindesterichweite sofort dauer und die Mindestreichweite sofort dauer drawn sollten jetzt gleich sein
                        # Die Zeit sollte auch mit dem früheren Abfahrtstermin ausreichen die geforderte Mindestreichweite sofort zu erreichen. Zusätzlich muss nicht weiter geladen werden.
                        self.geladene_kilometer3 = self.mindestreichweite_sofort
                else:
                    # Die Mindestreichweite später kann nicht einfach ignoriert werden
                    gewichtungsfaktor_zaehler = (self.mindestreichweite_spaeter - self.mindestreichweite_sofort) / (
                                self.gewuenschte_abfahrt - mindestreichweite_sofort_dauer)
                    gewichtungsfaktor = gewichtungsfaktor_zaehler / Constants.max_laderate
                    if gewichtungsfaktor <= 1:
                        # Erst der einfachere Fall: Der Gewichtungsfaktor ist kleiner gleich 1, die restliche Zeit (gemessen an der gewünschten Abfahrtszeit) reicht also aus um die Mindestreichweite später zu laden
                        if mindestreichweite_sofort_dauer_drawn == Constants.abfahrt3:
                            # Die gezogene Abfahrtszeit liegt so, dass noch nicht einmal die Mindestreichweite sofort aufgelden werden kann. Das Auto denkt aber es hat Zeit erst die Mindestreichweite sofort zu laden und dann noch die Mindestreichweite später
                            self.geladene_kilometer3 = round(Constants.aktuell_kilometer + (
                                        Constants.abfahrt3 * Constants.max_laderate), 2)
                        else:
                            # Die gezogene Abfahrtszeit reicht aus um die gewünschte Mindestreichweite sofort aufzuladen
                            # Reicht die Zeit auch um die Mindestreichweite später aufzuladen (Gewichtungfaktor <= 1) wird angenommen, dass die gesamte Restzeit mit einer verringerten Laderate geladen wird. D.h. hier wird erst die Mindestreichweite sofort aufgeladen um dann mit verringerter Laderate die restlich Zeit aufzuladen
                            restliche_zeit = Constants.abfahrt3 - mindestreichweite_sofort_dauer_drawn
                            self.geladene_kilometer3 = round(self.mindestreichweite_sofort + (
                                        restliche_zeit * gewichtungsfaktor_zaehler), 2)
                    else:
                        # Der Gewichtungsfaktor ist > 1, also würde die urpsrüngliche Zeit nicht ausreichen um die Mindestreichweite später zu laden
                        # Hier würde auch normalerweise die gesamte Standdauer über mit der maximalen Laderate aufgeladen werden. Also muss nicht erst noch überprüft werden ob die Standdauer ausreicht um die Mindestreichweite sofort aufzuladen
                        self.geladene_kilometer3 = round(Constants.aktuell_kilometer + (
                                    Constants.abfahrt3 * Constants.max_laderate), 2)


    def set_ladeflexibilitaet(self):
        ladedauer_maximal = min(self.gewuenschte_abfahrt,
                                (Constants.max_kilometer - Constants.aktuell_kilometer) / Constants.max_laderate)
        mindestreichweite_sofort_dauer = min(self.gewuenschte_abfahrt, (
                self.mindestreichweite_sofort - Constants.aktuell_kilometer) / Constants.max_laderate)

        if mindestreichweite_sofort_dauer == self.gewuenschte_abfahrt:
            self.ladeflexibilitaet = 0
        else:
            gewichtungsfaktor_zaehler = max(0, max(0, self.mindestreichweite_spaeter - self.mindestreichweite_sofort) /
                                            (self.gewuenschte_abfahrt - mindestreichweite_sofort_dauer))
            gewichtungsfaktor = gewichtungsfaktor_zaehler / Constants.max_laderate
            if gewichtungsfaktor >= 1:
                self.ladeflexibilitaet = 0
            else:
                mindestreichweite_spaeter_dauer = max(0, (
                            self.mindestreichweite_spaeter - self.mindestreichweite_sofort) / Constants.max_laderate)
                self.ladeflexibilitaet = round(
                    (1 - (mindestreichweite_sofort_dauer + gewichtungsfaktor * mindestreichweite_spaeter_dauer) /
                     ladedauer_maximal) * 100, 0)


    def set_payoff1(self):
        if Constants.to_drive1 <= self.geladene_kilometer1:
            self.punkte1 = int(0 + self.ladeflexibilitaet)
        else:
            self.punkte1 = int(0 - self.ladeflexibilitaet)

    def set_payoff2(self):
        if Constants.to_drive2 <= self.geladene_kilometer2:
            self.punkte2 = int(0 + self.ladeflexibilitaet)
        else:
            self.punkte2 = int(0 - self.ladeflexibilitaet)

    def set_payoff3(self):
        if Constants.to_drive3 <= self.geladene_kilometer3:
            self.punkte3 = int(0 + self.ladeflexibilitaet)
        else:
            self.punkte3 = int(0 - self.ladeflexibilitaet)

    def reset_payoff(self):
        self.participant.payoff = 0


    def calculate_minutes1(self):
        self.minutes1 = int((Constants.abfahrt1 % 1)*60)

    def calculate_hours1(self):
        self.hours1 = int(Constants.abfahrt1)


    def calculate_minutes2(self):
        self.minutes2 = int((Constants.abfahrt2 % 1)*60)

    def calculate_hours2(self):
        self.hours2 = int(Constants.abfahrt2)


    def calculate_minutes3(self):
        self.minutes3 = int((Constants.abfahrt3 % 1)*60)

    def calculate_hours3(self):
        self.hours3 = int(Constants.abfahrt3)

    def calculate_gewuenscht_abfahrt_minutes(self):
        self.gewuenschte_abfahrt_minutes = int((self.gewuenschte_abfahrt % 1)*60)

    def calculate_gewuenschte_abfahrt_hours(self):
        self.gewuenschte_abfahrt_hours = int(self.gewuenschte_abfahrt)