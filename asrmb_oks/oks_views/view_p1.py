from datetime import datetime

from django.shortcuts import render, get_object_or_404, redirect
from ..models import *


# from ..forms import *

def oks_p1(request):
    max_date_now = datetime.now().strftime("%Y-%m-%d")
    oks_p1_items = P1ComponentCompositionOfUnstableCondensate.objects.filter(date_create__contains=max_date_now)[:12]
    url_oks_p1 = oks_p1_items[0].date_create

    if request.method == "POST":
        oks_p1_items = P1ComponentCompositionOfUnstableCondensate.objects.filter(
            date_create__contains=request.POST.get('date_create', ''))[:12]
        url_oks_p1 = oks_p1_items[0].date_create

    if oks_p1_items.values():
        just_day = oks_p1_items.values()[0]['date_create']
    else:
        just_day = request.POST.get('date_create', '')

    context = {
        'max_date_now': max_date_now,
        'oks_p1_items': oks_p1_items,
        'url_oks_p1': url_oks_p1,
        'just_day': just_day
    }
    return render(request, 'asrmb_oks/oks_p1.html', context)


