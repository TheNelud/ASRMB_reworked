from datetime import datetime

from django.http import JsonResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from django.template.loader import render_to_string

from ..models import *

from ..forms import *


def oks_p10(request):
    max_date_now = datetime.now().strftime("%Y-%m-%d")
    oks_p10_items = P10ProtokolKGN.objects.filter(
        date_create__contains=max_date_now).order_by('date_update')

    oks_p10_items = P10ProtokolKGN.objects.all()

    # for i in oks_p10_items.values():
    #     print(i)


    url_oks_p10 = max_date_now
    if request.method == "POST":
        oks_p10_items = P10ProtokolKGN.objects.filter(
            date_create__contains=request.POST.get('date_create', '')).order_by('date_update')[:42]
        url_oks_p10 = request.POST.get('date_create', '')
    if oks_p10_items.values():
        just_day = oks_p10_items.values()[0]['date_create']
    else:
        just_day = request.POST.get('date_create', '')

    context = {
        'max_date_now': max_date_now,
        'oks_p10_items': oks_p10_items,
        'just_day': just_day,
        'url_oks_p10': url_oks_p10,
    }
    return render(request, 'asrmb_oks/forms/oks_p10/oks_p10.html', context)


def oks_p10_create(request):
    max_date_now = datetime.now().strftime("%Y-%m-%d")
    form_set = P10ProtokolKGNFormSet()

    if request.method == 'POST':
        form_set = P10ProtokolKGNFormSet(request.POST)

        print('Форма валидна: ' + str(form_set.is_valid()))
        print(form_set.cleaned_data)
        if form_set.is_valid():

            for form in form_set:
                form.save()
            return redirect('oks_p10')

    context = {
        'max_date_now': max_date_now,
        'form_set': form_set,
    }
    return render(request, 'asrmb_oks/forms/oks_p10/form_create.html', context)


def oks_p10_edit(request, date_oks_p10):
    oks_p10_items = P10ProtokolKGN.objects.filter(
        date_create__contains=date_oks_p10).order_by('date_update')[:42]

    if not oks_p10_items:
        raise Http404("Нет данных")

    if request.method == 'POST':
        form_set = P10ModelFormSet(request.POST)
        print('Форма валидна: ' + str(form_set.is_valid()))
        if form_set.is_valid():
            for form in form_set:

                form.save()
            return redirect('oks_p10')

    else:
        form_set = P10ModelFormSet(queryset=oks_p10_items)
        for f in form_set:
            print(f.as_table())

    context = {
        'just_day': date_oks_p10,
        'form_set': form_set,
    }
    return render(request, 'asrmb_oks/forms/oks_p10/form_edit.html', context)


def oks_p10_delete(request, date_oks_p10):
    oks_p10_items = P10ProtokolKGN.objects.filter(
        date_create__contains=date_oks_p10).order_by('date_update')[:42].values_list('id', flat=True)
    print(oks_p10_items)

    if not oks_p10_items:
        raise Http404("Нет данных")

    if request.method == 'POST':
        P10ProtokolKGN.objects.filter(pk__in=list(oks_p10_items)).delete()
        return redirect('oks_p10')
