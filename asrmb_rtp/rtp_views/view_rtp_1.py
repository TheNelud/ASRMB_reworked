from datetime import datetime

from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404

from ..models import *
from ..forms import *


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
    form_set = TeclossesOneForm()
    if request.method == 'POST':
        form_set = TeclossesOneForm(request.POST)
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


    if not rtp_1_items:
        raise Http404("Нет данных")

    if request.method == 'POST':
        form_set = TeclossesOneModelFormSet(request.POST)

        print('Форма валидна: ' + str(form_set.is_valid()))
        print(form_set.as_table())
        if form_set.is_valid():
            form_set.save()
            return redirect('rtp_1')

    else:
        form_set = TeclossesOneModelFormSet(queryset=rtp_1_items)

        print(form_set.as_table())

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
