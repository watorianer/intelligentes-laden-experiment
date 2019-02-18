from channels.generic.websockets import JsonWebsocketConsumer
from my_charging_flex_treatment_final.models import  Constants, Player

class IndexTracker(JsonWebsocketConsumer):
    url_pattern = (r'^/indextracker/(?P<player_pk>[0-9]+)$')

    def clean_kwargs(self):
        self.player_pk = self.kwargs['player_pk']

    def get_player(self):
        self.clean_kwargs()
        return Player.objects.get(pk=self.player_pk)

    # def connect(self, message, **kwargs):
    #     print('connected', message)


    def receive(self, text=None, bytes=None, **kwargs):
        self.clean_kwargs()
        player = self.get_player()
        value = Constants.monte_carlo.iat[text, 1]
        player.aktuelle_gewinnchance = value
        player.save()
        response = player.aktuelle_gewinnchance
        self.send(response)
