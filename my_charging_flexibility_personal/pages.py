from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    form_model = 'player'
    form_fields = ['crt_epkw',
                   'crt_bev_exp',
                   'crt_conv_exp',
                   'crt_zweitwagen',
                   'crt_flex_nutzung',
                   'crt_flex_anzahl',
                   'crt_flex_absicht',
                   'crt_attention',
                   'crt_age',
                   'crt_gender',
                   'crt_bildung',
                   'crt_wohnort',
                   'crt_einkommen',
                   'crt_risiko']


class TPB(Page):
    form_model = 'player'
    form_fields = ['crt_tpb_einstellung1',
                   'crt_tpb_einstellung2',
                   'crt_tpb_einstellung3',
                   'crt_tpb_einstellung4',
                   'crt_tpb_einstellung5',
                   'crt_tpb_normen1',
                   'crt_tpb_normen2',
                   'crt_tpb_normen3',
                   'crt_tpb_normen4',
                   'crt_tpb_normen5',
                   'crt_tpb_kontrolle1',
                   'crt_tpb_kontrolle2',
                   'crt_tpb_kontrolle3',
                   'crt_tpb_kontrolle4',
                   'crt_tpb_kontrolle5',
                   'crt_tpb_absicht1',
                   'crt_tpb_absicht2',
                   'crt_tpb_absicht3',
                   'crt_kommentar']

page_sequence = [
    MyPage,
    TPB
]
