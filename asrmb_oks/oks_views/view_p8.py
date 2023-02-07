from datetime import datetime

from django.http import JsonResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from django.template.loader import render_to_string

from ..models import *

from ..forms import *


def oks_p8(request):
    max_date_now = datetime.now().strftime("%Y-%m-%d")
    oks_p8_items = P8CompositionOfTheCondensate.objects.filter(
        date_create__contains=max_date_now).order_by('date_update')[:12]

    url_oks_p8 = max_date_now
    if request.method == "POST":
        oks_p8_items = P8CompositionOfTheCondensate.objects.filter(
            date_create__contains=request.POST.get('date_create', '')).order_by('date_update')[:12]
        url_oks_p8 = request.POST.get('date_create', '')
    if oks_p8_items.values():
        just_day = oks_p8_items.values()[0]['date_create']
    else:
        just_day = request.POST.get('date_create', '')

    context = {
        'max_date_now': max_date_now,
        'oks_p8_items': oks_p8_items,
        'just_day': just_day,
        'url_oks_p8': url_oks_p8,
    }
    return render(request, 'asrmb_oks/forms/oks_p8/oks_p8.html', context)


def oks_p8_create(request):
    max_date_now = datetime.now().strftime("%Y-%m-%d")
    form_set = P8CompositionOfTheCondensateFormSet()
    if request.method == 'POST':
        form_set = P8CompositionOfTheCondensateFormSet(request.POST)
        print('Форма валидна: ' + str(form_set.is_valid()))
        if form_set.is_valid():
            for form in form_set:
                form.save()
            return redirect('oks_p8')

    context = {
        'max_date_now': max_date_now,
        'form_set': form_set,
    }
    return render(request, 'asrmb_oks/forms/oks_p8/form_create.html', context)


def oks_p8_edit(request, date_oks_p8):
    oks_p8_items = P8CompositionOfTheCondensate.objects.filter(
        date_create__contains=date_oks_p8).order_by('date_update')[:12]

    if not oks_p8_items:
        raise Http404("Нет данных")

    if request.method == 'POST':
        form_set = P8ModelFormSet(request.POST)
        print('Форма валидна: ' + str(form_set.is_valid()))
        if form_set.is_valid():
            for form in form_set:
                form.save()
            return redirect('oks_p8')

    else:
        form_set = P8ModelFormSet(queryset=oks_p8_items)
        for f in form_set:
            print(f.as_table())

    context = {
        'just_day': date_oks_p8,
        'form_set': form_set,
    }
    return render(request, 'asrmb_oks/forms/oks_p8/form_edit.html', context)


def oks_p8_delete(request, date_oks_p8):
    oks_p8_items = P8CompositionOfTheCondensate.objects.filter(
        date_create__contains=date_oks_p8).order_by('date_update')[:12].values_list('id', flat=True)
    print(oks_p8_items)

    if not oks_p8_items:
        raise Http404("Нет данных")

    if request.method == 'POST':
        P8CompositionOfTheCondensate.objects.filter(pk__in=list(oks_p8_items)).delete()
        return redirect('oks_p8')
