from datetime import datetime

from django.http import JsonResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from django.template.loader import render_to_string

from ..models import *

from ..forms import *


def oks_p3(request):
    max_date_now = datetime.now().strftime("%Y-%m-%d")
    oks_p3_items = P3DeterminationOfTheComponentOfGas.objects.filter(
        date_create__contains=max_date_now).order_by('date_update')[:12]

    url_oks_p3 = max_date_now
    if request.method == "POST":
        oks_p3_items = P3DeterminationOfTheComponentOfGas.objects.filter(
            date_create__contains=request.POST.get('date_create', '')).order_by('date_update')[:12]
        url_oks_p3 = request.POST.get('date_create', '')
    if oks_p3_items.values():
        just_day = oks_p3_items.values()[0]['date_create']
    else:
        just_day = request.POST.get('date_create', '')

    context = {
        'max_date_now': max_date_now,
        'oks_p3_items': oks_p3_items,
        'just_day': just_day,
        'url_oks_p3': url_oks_p3,
    }
    return render(request, 'asrmb_oks/forms/oks_p3/oks_p3.html', context)


def oks_p3_create(request):
    max_date_now = datetime.now().strftime("%Y-%m-%d")
    form_set = P3DeterminationOfTheComponentOfGasFormSet()
    if request.method == 'POST':
        form_set = P3DeterminationOfTheComponentOfGasFormSet(request.POST)
        print('Форма валидна: ' + str(form_set.is_valid()))
        if form_set.is_valid():
            for form in form_set:
                form.save()
            return redirect('oks_p3')

    context = {
        'max_date_now': max_date_now,
        'form_set': form_set,
    }
    return render(request, 'asrmb_oks/forms/oks_p3/form_create.html', context)


def oks_p3_edit(request, date_oks_p3):
    oks_p3_items = P3DeterminationOfTheComponentOfGas.objects.filter(
        date_create__contains=date_oks_p3).order_by('date_update')[:12]

    if not oks_p3_items:
        raise Http404("Нет данных")

    if request.method == 'POST':
        form_set = P3ModelFormSet(request.POST)
        print('Форма валидна: ' + str(form_set.is_valid()))
        if form_set.is_valid():
            for form in form_set:
                form.save()
            return redirect('oks_p3')

    else:
        form_set = P3ModelFormSet(queryset=oks_p3_items)
        for f in form_set:
            print(f.as_table())

    context = {
        'just_day': date_oks_p3,
        'form_set': form_set,
    }
    return render(request, 'asrmb_oks/forms/oks_p3/form_edit.html', context)


def oks_p3_delete(request, date_oks_p3):
    oks_p3_items = P3DeterminationOfTheComponentOfGas.objects.filter(
        date_create__contains=date_oks_p3).order_by('date_update')[:12].values_list('id', flat=True)
    print(oks_p3_items)

    if not oks_p3_items:
        raise Http404("Нет данных")

    if request.method == 'POST':
        P3DeterminationOfTheComponentOfGas.objects.filter(pk__in=list(oks_p3_items)).delete()
        return redirect('oks_p3')
