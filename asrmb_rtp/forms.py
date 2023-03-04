from .models import *

from django.forms import ModelForm, modelformset_factory, formset_factory
from django import forms

''' 1. Технологические потери природного газа по итогам опорожнения технологического
 оборудования и трубопроводов перед проведением ремонтных работ, м3 (п.4.2.)';
 '''


class TeclossesOneForm(ModelForm):
    name = forms.CharField(label="Оборудование", max_length=255, required=False,
                           widget=forms.TextInput(attrs={'class': 'table_content_rd_rtp_input',
                                                         'style': 'width: 118px'}))
    v = forms.FloatField(label="V - геометрический объем аппарата", required=False,
                         widget=forms.NumberInput(attrs={'class': 'js-v table_content_rd_rtp_input'}))
    pn = forms.FloatField(label="Рн - абсолютное давление природного газа перед началом ремонтной работы",
                          required=False,
                          widget=forms.NumberInput(attrs={'class': 'js-pn table_content_rd_rtp_input'}))
    tn = forms.FloatField(label="Тн - температура природного газа перед началом работы", required=False,
                          widget=forms.NumberInput(attrs={'class': 'js-tn table_content_rd_rtp_input'}))
    zn = forms.FloatField(label="Zн - коэффициенты сверхсжимаемости природного газа", required=False,
                          widget=forms.NumberInput(attrs={'class': 'js-zn table_content_rd_rtp_input'}))
    press_pk = forms.FloatField(label="Рк - абсолютное давление природного газа после опорожнения", required=False,
                                widget=forms.NumberInput(attrs={'class': 'js-press_pk table_content_rd_rtp_input'}))
    tk = forms.FloatField(label="Тк - температура природного газа после опорожнения", required=False,
                          widget=forms.NumberInput(attrs={'class': 'js-tk table_content_rd_rtp_input'}))
    zk = forms.FloatField(label="Zк - коэффициенты сверхсжимаемости природного газа", required=False,
                          widget=forms.NumberInput(attrs={'class': 'js-zk table_content_rd_rtp_input'}))
    v_op = forms.FloatField(label='Vop', required=False,
                            widget=forms.NumberInput(attrs={'class': 'js-v_op table_content_rd_rtp_input'}))
    ng_prod = forms.FloatField(label='nг.прод', required=False,
                               widget=forms.NumberInput(attrs={'class': 'js-ng_prod table_content_rd_rtp_input'}))
    ng_nl = forms.FloatField(label="nг.пл - соответственно число молей в газе", required=False,
                             widget=forms.NumberInput(attrs={'class': 'js-ng_nl table_content_rd_rtp_input'}))
    xg_prod = forms.FloatField(label='', required=False,
                               widget=forms.NumberInput(attrs={'class': 'js-xg_prod table_content_rd_rtp_input'}))
    n = forms.FloatField(label="N - количество операций в расчетный период", required=False
                         , widget=forms.NumberInput(attrs={'class': 'js-n table_content_rd_rtp_input'}))
    pn_op = forms.FloatField(label="соответственно число молей в газе", required=False,
                             widget=forms.NumberInput(attrs={'class': 'js-pn_op table_content_rd_rtp_input'}))
    mol = forms.FloatField(label="Мольная доля С1-С4", required=False,
                           widget=forms.NumberInput(attrs={'class': 'js-mol table_content_rd_rtp_input',
                                                           'style': 'width: 200px'}))
    date_create = forms.DateTimeField(label='Дата создания', required=False,
                                      widget=forms.NumberInput(attrs={'style': 'display: None'}))
    date_update = forms.DateTimeField(label='Дата обновления', required=False,
                                      widget=forms.NumberInput(attrs={'style': 'display: None'}))

    class Meta:
        model = TeclossesOne
        fields = ['name', 'v', 'pn', 'tn', 'zn', 'press_pk', 'tk', 'zk', 'v_op',
                  'ng_prod', 'ng_nl', 'xg_prod', 'n', 'pn_op', 'mol']


# TeclossesOneModelFormSet = modelformset_factory(model=TeclossesOne,
#                                                 form=TeclossesOneForm,
#                                                 fields=('name', 'v', 'pn', 'tn', 'zn', 'press_pk', 'tk', 'zk', 'v_op',
#                                                         'ng_prod', 'ng_nl', 'xg_prod', 'n', 'pn_op', 'mol'),
#                                                 extra=0)

''' 
2. Технологические потери природного газа при регенерации технических жидкостей (МЭГа), м3 (п. 4.3.2)';
'''


class TeclossesTwoForm(ModelForm):
    name = forms.CharField(label="Оборудование", max_length=255, required=False)
    qgr_sh = forms.FloatField(label="Qг.р.ж. - расход природного газа при регенерации технических жидкостей",
                              required=False,
                              widget=forms.NumberInput(attrs={'class': 'js-qgr_sh table_content_rd_rtp_input'}))
    ng_prod = forms.FloatField(label="nг.пл - соответственно число молей в газе", required=False,
                               widget=forms.NumberInput(attrs={'class': 'js-ng_prod table_content_rd_rtp_input'}))
    ng_pl = forms.FloatField(label='nг.прод - соответственно число молей в газе', required=False,
                             widget=forms.NumberInput(attrs={'class': 'js-ng_pl table_content_rd_rtp_input'}))
    xg_prod = forms.FloatField(label='Xг.прод - мольная доля добываемой продукции в газе', required=False,
                               widget=forms.NumberInput(attrs={'class': 'js-xg_prod table_content_rd_rtp_input'}))
    pgr_sh = forms.FloatField(label="Пг.р.ж. - потери природного газа при регенерации технических жидкостей",
                              required=False,
                              widget=forms.NumberInput(attrs={'class': 'js-pgr_sh table_content_rd_rtp_input'}))
    date_create = forms.DateTimeField(label='Дата создания', required=False,
                                      widget=forms.NumberInput(attrs={'style': 'display: None'})
                                      )
    date_update = forms.DateTimeField(label='Дата обновления', required=False,
                                      widget=forms.NumberInput(attrs={'style': 'display: None'})
                                      )

    class Meta:
        model = TeclossesTwo
        fields = ['name', 'qgr_sh', 'ng_prod', 'ng_pl', 'xg_prod', 'pgr_sh']


# TeclossesTwoFormSet = formset_factory(form=TeclossesTwoForm,
#                                       extra=1)
# TeclossesTwoModelFormSet = modelformset_factory(model=TeclossesTwo,
#                                                 form=TeclossesTwoForm,
#                                                 fields=('name', 'qgr_sh', 'ng_prod', 'ng_pl', 'xg_prod', 'pgr_sh'),
#                                                 extra=1)

''' 
показания счетчиков 30Р-1
'''


class MeterReading30P1Form(ModelForm):
    date = forms.DateTimeField(required=False,
                               widget=forms.DateTimeInput(attrs={'class': 'js-date', 'type': 'date'}))
    num_one = forms.FloatField(required=False,
                               widget=forms.NumberInput(attrs={'class': 'js-num_one'}))
    num_two = forms.FloatField(required=False,
                               widget=forms.NumberInput(attrs={'class': 'js-num_two'}))
    date_create = forms.DateTimeField(label='Дата создания', required=False, )
    date_update = forms.DateTimeField(label='Дата обновления', required=False, )

    class Meta:
        model = MeterReading30P1
        fields = '__all__'


class MeterReadingAllForm(ModelForm):
    meter_p34 = forms.FloatField(required=False, widget=forms.NumberInput(attrs={'class': 'js-meter_p34'}))
    meter_30p1 = forms.FloatField(required=False, widget=forms.NumberInput(attrs={'class': 'js-meter_30p1'}))
    meter_10c1 = forms.FloatField(required=False, widget=forms.NumberInput(attrs={'class': 'js-meter_10c1'}))
    meter_10c4 = forms.FloatField(required=False, widget=forms.NumberInput(attrs={'class': 'js-meter_10c4'}))
    date_create = forms.DateTimeField(required=False)
    date_update = forms.DateTimeField(required=False)

    class Meta:
        model = MeterReadingAll
        fields = '__all__'


''' 
 3. Технологические потери природного газа при отборе проб, м3 (п. 4.5)';
'''


class TeclossesTreeForm(ModelForm):
    type_of_analysis = forms.CharField(label="Вид анализа", max_length=255, required=False,
                                       widget=forms.TextInput(attrs={'class': 'table_content_rd_rtp_input'}))
    v_pr = forms.FloatField(label="Vпр - геометрический объем пробоотборника для анализа i-го вида", required=False,
                            widget=forms.NumberInput(attrs={'class': 'js-v_pr table_content_rd_rtp_input'}))
    p_pr = forms.FloatField(label="Рпр - давление в пробоотборнике для анализа i-го вида", required=False,
                            widget=forms.NumberInput(attrs={'class': 'js-p_pr table_content_rd_rtp_input'}))
    t_pr = forms.FloatField(label="Tпр - температура в пробоотборнике для анализа i-го вида", required=False,
                            widget=forms.NumberInput(attrs={'class': 'js-t_pr table_content_rd_rtp_input'}))
    z_pr = forms.FloatField(label="Zпр - коэффициент сжимаемости газа", required=False,
                            widget=forms.NumberInput(attrs={'class': 'js-z_pr table_content_rd_rtp_input'}))
    b = forms.FloatField(label="b -кратность продувки, т.е. отношение объема (при условии отбора) газа,",
                         required=False, widget=forms.NumberInput(attrs={'class': 'js-b table_content_rd_rtp_input'}))
    ni = forms.FloatField(label="ni", required=False,
                          widget=forms.NumberInput(attrs={'class': 'js-ni table_content_rd_rtp_input'}))
    xr_prod = forms.FloatField(label="Xг.прод - мольная доля добываемой продукции в газе", required=False,
                               widget=forms.NumberInput(attrs={'class': 'js-xr_prod table_content_rd_rtp_input'}))
    pr_op = forms.FloatField(label="Пг.оп - потери природного газа при периодическом отборе проб для разовых",
                             required=False,
                             widget=forms.NumberInput(attrs={'class': 'js-pr_op table_content_rd_rtp_input'}))
    device = forms.CharField(label="Приборы", max_length=255, required=False,
                             widget=forms.TextInput(attrs={'class': ' table_content_rd_rtp_input'}))
    v_p = forms.FloatField(label="Vр.- расход газа на i-й прибор", required=False,
                           widget=forms.NumberInput(attrs={'class': 'js-v_p table_content_rd_rtp_input'}))
    tau = forms.FloatField(label="τр - время работы i-го прибора в расчетный период", required=False,
                           widget=forms.NumberInput(attrs={'class': 'js-tau table_content_rd_rtp_input'}))
    xrr_prod = forms.FloatField(label="Xг.прод - мольная доля добываемой продукции в газе", required=False,
                                widget=forms.NumberInput(attrs={'class': 'js-xrr_prod table_content_rd_rtp_input'}))
    n = forms.FloatField(label="n - число видов анализов", required=False,
                         widget=forms.NumberInput(attrs={'class': 'js-n table_content_rd_rtp_input'}))
    pr_pot = forms.FloatField(label="Пг.пот.i - потери природного газа при работе i-го прибора на потоке",
                              required=False,
                              widget=forms.NumberInput(attrs={'class': 'js-pr_pot table_content_rd_rtp_input'}))
    pr_pr = forms.FloatField(label="Пг.пр - соответственно число молей пластового газа и газа", required=False,
                             widget=forms.NumberInput(attrs={'class': 'js-pr_pr table_content_rd_rtp_input'}))
    date_create = forms.DateTimeField(label='Дата создания', required=False,
                                      widget=forms.NumberInput(attrs={'style': 'display: None'}))
    date_update = forms.DateTimeField(label='Дата обновления', required=False,
                                      widget=forms.NumberInput(attrs={'style': 'display: None'}))

    class Meta:
        model = TeclossesTree
        fields = ['type_of_analysis', 'v_pr', 'p_pr', 't_pr', 'z_pr', 'b', 'ni',
                  'xr_prod', 'pr_op', 'device', 'v_p', 'tau', 'xrr_prod', 'n', 'pr_pot', 'pr_pr']


# 'Расчет потерь при Переработке**
# 1. Потери природного газа через неплотности соединений и уплотнений ЗРА, м3. (п.5.1.3)';

class RecyclingcalcOneForm(ModelForm):
    type = forms.CharField(required=False, )
    aij = forms.FloatField(required=False, )
    bij = forms.FloatField(required=False, )
    tauij = forms.FloatField(required=False, )
    a_ij = forms.FloatField(required=False, )
    mi = forms.FloatField(required=False, )
    q_yp = forms.FloatField(required=False, )
    t_type = forms.CharField(required=False, )
    t_aij = forms.FloatField(required=False, )
    t_bij = forms.FloatField(required=False, )
    t_tauij = forms.FloatField(required=False, )
    t_a_ij = forms.FloatField(required=False, )
    t_mi = forms.FloatField(required=False, )
    t_q_yp = forms.FloatField(required=False, )
    date_create = forms.DateTimeField(required=False, )
    date_update = forms.DateTimeField(required=False, )

    class Meta:
        model = RecyclingcalcOne
        fields = '__all__'


class RecyclingcalcOneTimeForm(ModelForm):
    type = forms.CharField(required=False, widget=forms.Select(
        choices=(
            ('1', 'КУ-1 '),
            ('2', 'КУ-2 '),
            ('3', '1 т.н. УСК'),
            ('4', '2 т.н. УСК'),
            ('5', '3 т.н. УСК'),
        ))
                           )
    time = forms.IntegerField(required=False, )
    date_create = forms.DateTimeField(required=False, )
    date_update = forms.DateTimeField(required=False, )

    class Meta:
        model = RecyclingcalcOneTime
        fields = '__all__'
