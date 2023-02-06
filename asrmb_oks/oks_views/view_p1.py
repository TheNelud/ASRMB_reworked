from datetime import datetime

from django.http import JsonResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from django.template.loader import render_to_string

from ..models import *

from ..forms import *


def oks_p1(request):
    max_date_now = datetime.now().strftime("%Y-%m-%d")
    oks_p1_items = P1ComponentCompositionOfUnstableCondensate.objects.filter(
        date_create__contains=max_date_now).order_by('date_update')[:12]

    url_oks_p1 = max_date_now
    if request.method == "POST":
        oks_p1_items = P1ComponentCompositionOfUnstableCondensate.objects.filter(
            date_create__contains=request.POST.get('date_create', '')).order_by('date_update')[:12]
        url_oks_p1 = request.POST.get('date_create', '')
    if oks_p1_items.values():
        just_day = oks_p1_items.values()[0]['date_create']
    else:
        just_day = request.POST.get('date_create', '')

    context = {
        'max_date_now': max_date_now,
        'oks_p1_items': oks_p1_items,
        'just_day': just_day,
        'url_oks_p1': url_oks_p1,
    }
    return render(request, 'asrmb_oks/forms/oks_p1/oks_p1.html', context)


def oks_p1_create(request):
    max_date_now = datetime.now().strftime("%Y-%m-%d")
    form_set = P1ComponentCompositionOfUnstableCondensateFormSet()
    if request.method == 'POST':
        form_set = P1ComponentCompositionOfUnstableCondensateFormSet(request.POST)
        print('Форма валидна: ' + str(form_set.is_valid()))
        if form_set.is_valid():
            for form in form_set:
                form.save()
            return redirect('oks_p1')

    context = {
        'max_date_now': max_date_now,
        'form_set': form_set,
    }
    return render(request, 'asrmb_oks/forms/oks_p1/form_create.html', context)


def oks_p1_edit(request, date_oks_p1):
    oks_p1_items = P1ComponentCompositionOfUnstableCondensate.objects.filter(
        date_create__contains=date_oks_p1).order_by('date_update')[:12]

    if not oks_p1_items:
        raise Http404("Нет данных")

    if request.method == 'POST':
        form_set = P1ModelFormSet(request.POST)
        print('Форма валидна: ' + str(form_set.is_valid()))
        if form_set.is_valid():
            for form in form_set:
                form.save()
            return redirect('oks_p1')

    else:
        form_set = P1ModelFormSet(queryset=oks_p1_items)

    context = {
        'just_day': date_oks_p1,
        'form_set': form_set,
    }
    return render(request, 'asrmb_oks/forms/oks_p1/form_edit.html', context)


def oks_p1_delete(request, date_oks_p1):
    oks_p1_items = P1ComponentCompositionOfUnstableCondensate.objects.filter(
        date_create__contains=date_oks_p1).order_by('date_update')[:12]
    if not oks_p1_items:
        raise Http404("Нет данных")

    if request.method == 'POST':
        oks_p1_items.delete()
        return redirect('oks_p1')
