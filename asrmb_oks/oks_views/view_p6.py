from datetime import datetime

from django.http import JsonResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from django.template.loader import render_to_string

from ..models import *

from ..forms import *


def oks_p6(request):
    max_date_now = datetime.now().strftime("%Y-%m-%d")
    oks_p6_items = P6CompositionOfGasOutput.objects.filter(
        date_create__contains=max_date_now).order_by('date_update')[:12]

    url_oks_p6 = max_date_now
    if request.method == "POST":
        oks_p6_items = P6CompositionOfGasOutput.objects.filter(
            date_create__contains=request.POST.get('date_create', '')).order_by('date_update')[:12]
        url_oks_p6 = request.POST.get('date_create', '')
    if oks_p6_items.values():
        just_day = oks_p6_items.values()[0]['date_create']
    else:
        just_day = request.POST.get('date_create', '')

    context = {
        'max_date_now': max_date_now,
        'oks_p6_items': oks_p6_items,
        'just_day': just_day,
        'url_oks_p6': url_oks_p6,
    }
    return render(request, 'asrmb_oks/forms/oks_p6/oks_p6.html', context)


def oks_p6_create(request):
    max_date_now = datetime.now().strftime("%Y-%m-%d")
    form_set = P6CompositionOfGasOutputFormSet()
    if request.method == 'POST':
        form_set = P6CompositionOfGasOutputFormSet(request.POST)
        print('Форма валидна: ' + str(form_set.is_valid()))
        if form_set.is_valid():
            for form in form_set:
                form.save()
            return redirect('oks_p6')

    context = {
        'max_date_now': max_date_now,
        'form_set': form_set,
    }
    return render(request, 'asrmb_oks/forms/oks_p6/form_create.html', context)


def oks_p6_edit(request, date_oks_p6):
    oks_p6_items = P6CompositionOfGasOutput.objects.filter(
        date_create__contains=date_oks_p6).order_by('date_update')[:12]

    if not oks_p6_items:
        raise Http404("Нет данных")

    if request.method == 'POST':
        form_set = P6ModelFormSet(request.POST)
        print('Форма валидна: ' + str(form_set.is_valid()))
        if form_set.is_valid():
            for form in form_set:
                form.save()
            return redirect('oks_p6')

    else:
        form_set = P6ModelFormSet(queryset=oks_p6_items)
        for f in form_set:
            print(f.as_table())

    context = {
        'just_day': date_oks_p6,
        'form_set': form_set,
    }
    return render(request, 'asrmb_oks/forms/oks_p6/form_edit.html', context)


def oks_p6_delete(request, date_oks_p6):
    oks_p6_items = P6CompositionOfGasOutput.objects.filter(
        date_create__contains=date_oks_p6).order_by('date_update')[:12].values_list('id', flat=True)
    print(oks_p6_items)

    if not oks_p6_items:
        raise Http404("Нет данных")

    if request.method == 'POST':
        P6CompositionOfGasOutput.objects.filter(pk__in=list(oks_p6_items)).delete()
        return redirect('oks_p6')
