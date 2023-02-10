from .models import *

from django.forms import ModelForm
from django import forms


class TeclossesOneForm(ModelForm):
    name = forms.CharField(label="Оборудование", max_length=255, required=False,
                           widget=forms.TextInput(attrs={'class': 'table_content_rd_rtp_input',
                                                         'style': 'width: 118px'}))
    v = forms.FloatField(label="V - геометрический объем аппарата", required=False,
                         widget=forms.NumberInput(attrs={'class': 'js-claculated table_content_rd_rtp_input'}))
    pn = forms.FloatField(label="Рн - абсолютное давление природного газа перед началом ремонтной работы",
                          required=False,
                          widget=forms.NumberInput(attrs={'class': 'js-claculated table_content_rd_rtp_input'}))
    tn = forms.FloatField(label="Тн - температура природного газа перед началом работы", required=False,
                          widget=forms.NumberInput(attrs={'class': 'js-claculated table_content_rd_rtp_input'}))
    zn = forms.FloatField(label="Zн - коэффициенты сверхсжимаемости природного газа", required=False,
                          widget=forms.NumberInput(attrs={'class': 'js-claculated table_content_rd_rtp_input'}))
    press_pk = forms.FloatField(label="Рк - абсолютное давление природного газа после опорожнения", required=False,
                                widget=forms.NumberInput(attrs={'class': 'js-claculated table_content_rd_rtp_input'}))
    tk = forms.FloatField(label="Тк - температура природного газа после опорожнения", required=False,
                          widget=forms.NumberInput(attrs={'class': 'js-claculated table_content_rd_rtp_input'}))
    zk = forms.FloatField(label="Zк - коэффициенты сверхсжимаемости природного газа", required=False,
                          widget=forms.NumberInput(attrs={'class': 'js-claculated table_content_rd_rtp_input'}))
    v_op = forms.FloatField(label='Vop', required=False,
                            widget=forms.NumberInput(attrs={'class': 'js-claculated table_content_rd_rtp_input'}))
    ng_prod = forms.FloatField(label='nг.прод', required=False,
                               widget=forms.NumberInput(attrs={'class': 'js-claculated table_content_rd_rtp_input'}))
    ng_nl = forms.FloatField(label="nг.пл - соответственно число молей в газе", required=False,
                             widget=forms.NumberInput(attrs={'class': 'js-claculated table_content_rd_rtp_input'}))
    xg_prod = forms.FloatField(label='', required=False,
                               widget=forms.NumberInput(attrs={'class': 'js-claculated table_content_rd_rtp_input'}))
    n = forms.FloatField(label="N - количество операций в расчетный период", required=False
                         , widget=forms.NumberInput(attrs={'class': 'js-claculated table_content_rd_rtp_input'}))
    pn_op = forms.FloatField(label="соответственно число молей в газе", required=False,
                             widget=forms.NumberInput(attrs={'class': 'js-claculated table_content_rd_rtp_input'}))
    mol = forms.FloatField(label="Мольная доля С1-С4", required=False,
                           widget=forms.NumberInput(attrs={'class': 'js-claculated table_content_rd_rtp_input',
                                                           'style': 'width: 200px'}))
    date_create = forms.DateTimeField(label='Дата создания', required=False,
                                      widget=forms.NumberInput(attrs={'style': 'display: None'}))
    date_update = forms.DateTimeField(label='Дата обновления', required=False,
                                      widget=forms.NumberInput(attrs={'style': 'display: None'}))

    class Meta:
        model = TeclossesOne
        fields = ['name', 'v', 'pn', 'tn', 'zn', 'press_pk', 'tk', 'zk', 'v_op',
                  'ng_prod', 'ng_nl', 'xg_prod', 'n', 'pn_op', 'mol']


class TeclossesTwoForm(ModelForm):
    name = forms.CharField(label="Оборудование", max_length=255, required=False)
    qgr_sh = forms.FloatField(label="Qг.р.ж. - расход природного газа при регенерации технических жидкостей",
                              required=False)
    ng_prod = forms.FloatField(label="nг.пл - соответственно число молей в газе", required=False)
    ng_pl = forms.FloatField(label='nг.прод - соответственно число молей в газе', required=False)
    xg_prod = forms.FloatField(label='Xг.прод - мольная доля добываемой продукции в газе', required=False)
    pgr_sh = forms.FloatField(label="Пг.р.ж. - потери природного газа при регенерации технических жидкостей",
                              required=False)
    date_create = forms.DateTimeField(label='Дата создания', required=False)
    date_update = forms.DateTimeField(label='Дата обновления', required=False)

    class Meta:
        model = TeclossesTwo
        fields = ['name', 'qgr_sh', 'ng_prod', 'ng_pl']


class TeclossesTreeForm(ModelForm):
    name = forms.CharField(label="Вид анализа", max_length=255, required=False)
    v_pr = forms.FloatField(label="Vпр - геометрический объем пробоотборника для анализа i-го вида", required=False)
    p_pr = forms.FloatField(label="Рпр - давление в пробоотборнике для анализа i-го вида", required=False)
    t_pr = forms.FloatField(label="Tпр - температура в пробоотборнике для анализа i-го вида", required=False)
    z_pr = forms.FloatField(label="Zпр - коэффициент сжимаемости газа", required=False)
    b = forms.FloatField(label="b -кратность продувки, т.е. отношение объема (при условии отбора) газа,",
                         required=False)
    ni = forms.FloatField(label="ni", required=False)
    xr_prod = forms.FloatField(label="Xг.прод - мольная доля добываемой продукции в газе", required=False)
    pr_op = forms.FloatField(label="Пг.оп - потери природного газа при периодическом отборе проб для разовых",
                             required=False)
    device = forms.CharField(label="Приборы", max_length=255, required=False)
    v_p = forms.FloatField(label="Vр.- расход газа на i-й прибор", required=False)
    tau = forms.FloatField(label="τр - время работы i-го прибора в расчетный период", required=False)
    xrr_prod = forms.FloatField(label="Xг.прод - мольная доля добываемой продукции в газе", required=False)
    n = forms.FloatField(label="n - число видов анализов", required=False)
    pr_pot = forms.FloatField(label="Пг.пот.i - потери природного газа при работе i-го прибора на потоке",
                              required=False)
    pr_pr = forms.FloatField(label="Пг.пр - соответственно число молей пластового газа и газа", required=False)
    date_create = forms.DateTimeField(label='Дата создания', required=False)
    date_update = forms.DateTimeField(label='Дата обновления', required=False)

    class Meta:
        model = TeclossesTree
        fields = ['name', 'v_pr', 'p_pr', 't_pr', 'z_pr', 'b', 'ni',
                  'xr_prod', 'device', 'tau', 'xrr_prod', 'n']
