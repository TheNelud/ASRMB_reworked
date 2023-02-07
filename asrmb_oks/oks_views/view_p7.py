from datetime import datetime

from django.http import JsonResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from django.template.loader import render_to_string

from ..models import *

from ..forms import *


def oks_p7(request):
    max_date_now = datetime.now().strftime("%Y-%m-%d")
    oks_p7_items = P7CompositionOfGas10c.objects.filter(
        date_create__contains=max_date_now).order_by('date_update')[:12]

    url_oks_p7 = max_date_now
    if request.method == "POST":
        oks_p7_items = P7CompositionOfGas10c.objects.filter(
            date_create__contains=request.POST.get('date_create', '')).order_by('date_update')[:12]
        url_oks_p7 = request.POST.get('date_create', '')
    if oks_p7_items.values():
        just_day = oks_p7_items.values()[0]['date_create']
    else:
        just_day = request.POST.get('date_create', '')

    context = {
        'max_date_now': max_date_now,
        'oks_p7_items': oks_p7_items,
        'just_day': just_day,
        'url_oks_p7': url_oks_p7,
    }
    return render(request, 'asrmb_oks/forms/oks_p7/oks_p7.html', context)


def oks_p7_create(request):
    max_date_now = datetime.now().strftime("%Y-%m-%d")
    form_set = P7CompositionOfGas10cFormSet()
    if request.method == 'POST':
        form_set = P7CompositionOfGas10cFormSet(request.POST)
        print('Форма валидна: ' + str(form_set.is_valid()))
        if form_set.is_valid():
            for form in form_set:
                form.save()
            return redirect('oks_p7')

    context = {
        'max_date_now': max_date_now,
        'form_set': form_set,
    }
    return render(request, 'asrmb_oks/forms/oks_p7/form_create.html', context)


def oks_p7_edit(request, date_oks_p7):
    oks_p7_items = P7CompositionOfGas10c.objects.filter(
        date_create__contains=date_oks_p7).order_by('date_update')[:12]

    if not oks_p7_items:
        raise Http404("Нет данных")

    if request.method == 'POST':
        form_set = P7ModelFormSet(request.POST)
        print('Форма валидна: ' + str(form_set.is_valid()))
        if form_set.is_valid():
            for form in form_set:
                form.save()
            return redirect('oks_p7')

    else:
        form_set = P7ModelFormSet(queryset=oks_p7_items)
        for f in form_set:
            print(f.as_table())

    context = {
        'just_day': date_oks_p7,
        'form_set': form_set,
    }
    return render(request, 'asrmb_oks/forms/oks_p7/form_edit.html', context)


def oks_p7_delete(request, date_oks_p7):
    oks_p7_items = P7CompositionOfGas10c.objects.filter(
        date_create__contains=date_oks_p7).order_by('date_update')[:12].values_list('id', flat=True)
    print(oks_p7_items)

    if not oks_p7_items:
        raise Http404("Нет данных")

    if request.method == 'POST':
        P7CompositionOfGas10c.objects.filter(pk__in=list(oks_p7_items)).delete()
        return redirect('oks_p7')
