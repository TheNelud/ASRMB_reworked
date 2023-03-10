from datetime import datetime

from django.forms import modelformset_factory
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404

from asrmb_rtp.models import *
from asrmb_rtp.forms import *


def rtp_1(request):
    max_date_now = datetime.now().strftime("%Y-%m-%d")
    rtp_1_items = TeclossesOne.objects.filter(
        date_create__contains=max_date_now).order_by('date_update')

    url_rtp_1 = max_date_now
    if request.method == "POST":
        rtp_1_items = TeclossesOne.objects.filter(
            date_create__contains=request.POST.get('date_create', '')).order_by('date_update')
        url_rtp_1 = request.POST.get('date_create', '')
    if rtp_1_items.values():
        just_day = rtp_1_items.values()[0]['date_create']
    else:
        just_day = request.POST.get('date_create', '')

    context = {
        'max_date_now': max_date_now,
        'rtp_1_items': rtp_1_items,
        'just_day': just_day,
        'url_rtp_1': url_rtp_1,
    }
    return render(request, 'asrmb_rtp/forms/rtp_1/rtp_1.html', context)


def rtp_1_create(request):
    max_date_now = datetime.now().strftime("%Y-%m-%d")
    TeclossesOneModelFormSet = modelformset_factory(model=TeclossesOne,
                                                    form=TeclossesOneForm,
                                                    fields=(
                                                        'name', 'v', 'pn', 'tn', 'zn', 'press_pk', 'tk', 'zk', 'v_op',
                                                        'ng_prod', 'ng_nl', 'xg_prod', 'n', 'pn_op', 'mol'),
                                                    extra=1)

    form_set = TeclossesOneModelFormSet(queryset=TeclossesOne.objects.none())
    if request.method == 'POST':
        form_set = TeclossesOneModelFormSet(data=request.POST)
        print('Форма валидна: ' + str(form_set.is_valid()))
        if form_set.is_valid():
            form_set.save()
            return redirect('rtp_1')

    context = {
        'max_date_now': max_date_now,
        'form_set': form_set,
    }
    return render(request, 'asrmb_rtp/forms/rtp_1/form_create.html', context)


def rtp_1_edit(request, date_rtp_1):
    rtp_1_items = TeclossesOne.objects.filter(
        date_create__contains=date_rtp_1).order_by('date_update')
    TeclossesOneModelFormSet = modelformset_factory(model=TeclossesOne,
                                                    form=TeclossesOneForm,
                                                    fields=(
                                                        'name', 'v', 'pn', 'tn', 'zn', 'press_pk', 'tk', 'zk', 'v_op',
                                                        'ng_prod', 'ng_nl', 'xg_prod', 'n', 'pn_op', 'mol'),
                                                    extra=0)

    if not rtp_1_items:
        raise Http404("Нет данных")

    if request.method == 'POST':
        form_set = TeclossesOneModelFormSet(request.POST)
        print('Форма валидна: ' + str(form_set.is_valid()))
        if form_set.is_valid():
            form_set.save()
            return redirect('rtp_1')
    else:
        form_set = TeclossesOneModelFormSet(queryset=rtp_1_items)

    context = {
        'just_day': date_rtp_1,
        'form_set': form_set,
    }
    return render(request, 'asrmb_rtp/forms/rtp_1/form_edit.html', context)


def rtp_1_delete(request, date_rtp_1):
    rtp_1_items = TeclossesOne.objects.filter(
        date_create__contains=date_rtp_1).order_by('date_update').values_list('id', flat=True)
    print(rtp_1_items)

    if not rtp_1_items:
        raise Http404("Нет данных")

    if request.method == 'POST':
        TeclossesOne.objects.filter(pk__in=list(rtp_1_items)).delete()
        return redirect('rtp_1')
