from datetime import datetime

from django.forms import modelformset_factory
from django.http import Http404
from django.shortcuts import render, redirect

from asrmb_rtp.models import *
from asrmb_rtp.forms import *


def rtp_3(request):
    max_date_now = datetime.now().strftime("%Y-%m-%d")
    rtp_3_items = TeclossesTree.objects.filter(
        date_create__contains=max_date_now).order_by('date_update')

    url_rtp_3 = max_date_now
    if request.method == "POST":
        rtp_3_items = TeclossesTree.objects.filter(
            date_create__contains=request.POST.get('date_create', '')).order_by('date_update')
        url_rtp_3 = request.POST.get('date_create', '')
    if rtp_3_items.values():
        just_day = rtp_3_items.values()[0]['date_create']
    else:
        just_day = request.POST.get('date_create', '')

    context = {
        'max_date_now': max_date_now,
        'rtp_3_items': rtp_3_items,
        'just_day': just_day,
        'url_rtp_3': url_rtp_3,
    }
    return render(request, 'asrmb_rtp/forms/rtp_3/rtp_3.html', context)


def rtp_3_create(request):
    max_date_now = datetime.now().strftime("%Y-%m-%d")

    TeclossesTreeModelFormSet = modelformset_factory(model=TeclossesTree,
                                                     form=TeclossesTreeForm,
                                                     fields=(
                                                         'type_of_analysis', 'v_pr', 'p_pr', 't_pr', 'z_pr', 'b', 'ni',
                                                         'xr_prod', 'device', 'tau', 'xrr_prod', 'n'),
                                                     extra=2)
    form_set = TeclossesTreeModelFormSet(queryset=TeclossesTree.objects.none())

    if request.method == 'POST':
        form_set = TeclossesTreeModelFormSet(data=request.POST)
        print('Форма валидна: ' + str(form_set.is_valid()))
        if form_set.is_valid():
            form_set.save()
            return redirect('rtp_3')
    context = {
        'max_date_now': max_date_now,
        'form_set': form_set,
    }
    return render(request, 'asrmb_rtp/forms/rtp_3/form_create.html', context)
