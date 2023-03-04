from datetime import datetime

from asrmb_rtp.models import *
from asrmb_rtp.forms import *
from django.forms import modelformset_factory
from django.shortcuts import render, redirect


def rtp_4(request):
    max_date_now = datetime.now().strftime("%Y-%m-%d")
    rtp_4_items = RecyclingcalcOne.objects.filter(
        date_create__contains=max_date_now).order_by('date_update')
    rtp_4_time_items = RecyclingcalcOneTime.objects.filter(
        date_create__contains=max_date_now).order_by('date_update')

    url_rtp_4 = max_date_now

    if request.method == 'POST':
        rtp_4_items = RecyclingcalcOne.objects.filter(
            date_create__contains=request.POST.get('date_create', '')).order_by('date_update')
        rtp_4_time_items = RecyclingcalcOneTime.objects.filter(
            date_create__contains=request.POST.get('date_create', '')).order_by('date_update')
        url_rtp_4 = request.POST.get('date_create', '')

    if rtp_4_items.values():
        just_day = rtp_4_items.values()[0]['date_create']
    else:
        just_day = request.POST.get('date_create', '')
    context = {
        'max_date_now': max_date_now,
        'rtp_4_items': rtp_4_items,
        'rtp_4_time_items': rtp_4_time_items,
        'just_day': just_day,
        'url_rtp_4': url_rtp_4,
    }
    return render(request, 'asrmb_rtp/forms/rtp_4/rtp_4.html', context)


def rtp_4_create(request):
    max_date_now = datetime.now().strftime("%Y-%m-%d")

    RecyclingcalcOneModelFormSet = modelformset_factory(model=RecyclingcalcOne,
                                                        form=RecyclingcalcOneForm,
                                                        fields=(
                                                            'type', 'aij', 'bij', 'tauij',
                                                            'a_ij', 'mi', 'q_yp', 't_type',
                                                            't_aij', 't_bij', 't_tauij',
                                                            't_a_ij', 't_mi', 't_q_yp')
                                                        , extra=4)
    RecyclingcalcOneTimeModelFormSet = modelformset_factory(model=RecyclingcalcOneTime,
                                                            form=RecyclingcalcOneTimeForm,
                                                            fields=('type', 'time'),
                                                            extra=5)
    form_set_ro = RecyclingcalcOneModelFormSet(queryset=RecyclingcalcOne.objects.none())
    form_set_ro_time = RecyclingcalcOneTimeModelFormSet(queryset=RecyclingcalcOneTime.objects.none())

    if request.method == "POST":
        form_set_ro = RecyclingcalcOneModelFormSet(data=request.POST)
        form_set_ro_time = RecyclingcalcOneTimeModelFormSet(data=request.POST)
        if form_set_ro.is_valid() and form_set_ro_time.is_valid():
            form_set_ro.save()
            form_set_ro_time.save()
            return redirect('rtp_4')
    context = {
        'max_date_now': max_date_now,
        'form_set_ro': form_set_ro,
        'form_set_ro_time': form_set_ro_time
    }

    return render(request, 'asrmb_rtp/forms/rtp_4/form_create.html', context)
