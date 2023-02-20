from datetime import datetime

from asrmb_rtp.models import *
from asrmb_rtp.forms import *

from asrmb_oks.models import *
from asrmb_oks.forms import *


def calculated_meter_reading():
    max_date_now = datetime.now().strftime("%Y-%m-%d")
    oks_p3_items = P3DeterminationOfTheComponentOfGas.objects.filter(date_create__contains=max_date_now).order_by(
        'date_update')[:5]
    oks_p4_items = P4GasCompositionToTheProtocol.objects.filter(date_create__contains=max_date_now).order_by(
        'date_update')[:5]
    oks_p2_items = P2ComponentCompositionOfGas.objects.filter(date_create__contains=max_date_now).order_by(
        'date_update')[:5]
    oks_p6_items = P6CompositionOfGasOutput.objects.filter(date_create__contains=max_date_now).order_by('date_update')[
                   :5]

    if not MeterReadingAll.objects.filter(date_create__contains=max_date_now):
        MeterReadingAll.objects.create(
            meter_p34=sum(oks_p3_items.values_list('molar_content_of_components', flat=True)),
            meter_30p1=sum(oks_p4_items.values_list('molar_content_of_components', flat=True)),
            meter_10c1=sum(oks_p2_items.values_list('molar_content_of_components', flat=True)),
            meter_10c4=sum(oks_p6_items.values_list('molar_content_of_components', flat=True))
            )


