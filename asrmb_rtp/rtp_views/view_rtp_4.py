from datetime import datetime

from asrmb_rtp.models import *
from asrmb_rtp.forms import *
from django.shortcuts import render


def rtp_4(request):
    max_date_now = datetime.now().strftime("%Y-%m-%d")
    rtp_4_items = RecyclingcalcOne.objects.filter(
        date_create__contains=max_date_now).order_by('date_update')
    url_rtp_4 = max_date_now

    if request.method == 'POST':
        rtp_4_items = RecyclingcalcOne.objects.filter(
            date_create__contains=request.POST.get('date_create', '')).order_by('date_update')
        url_rtp_4 = request.POST.get('date_create', '')

    if rtp_4_items.values():
        just_day = rtp_4_items.values()[0]['date_create']
    else:
        just_day = request.POST.get('date_create', '')
    context = {
        'max_date_now': max_date_now,
        'rtp_4_items': rtp_4_items,
        'just_day': just_day,
        'url_rtp_4': url_rtp_4,
    }
    return render(request, 'asrmb_rtp/forms/rtp_4/rtp_4.html', context)