from datetime import datetime

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string

from ..models import *

from ..forms import *


def oks_p10(request):
    max_date_now = datetime.now().strftime("%Y-%m-%d")
    oks_p10_items = P10ProtokolKGN.objects.filter(date_create__contains=max_date_now).order_by('id')[:42]

    form_set = P10ProtokolKGNFormSet()

    if request.method == "POST":
        oks_p10_items = P10ProtokolKGN.objects.filter(
            date_create__contains=request.POST.get('date_create', ''))[:42]

    if oks_p10_items.values():
        just_day = oks_p10_items.values()[0]['date_create']
    else:
        just_day = request.POST.get('date_create', '')

    context = {
        'max_date_now': max_date_now,
        'oks_p10_items': oks_p10_items,
        'just_day': just_day,
        'form_set': form_set,
    }
    return render(request, 'asrmb_oks/forms/oks_p10/oks_p10.html', context)


def save_oks_p10_form(request, form_set):
    if request.method == 'POST':
        print('Форма валидна: ' + str(form_set.is_valid()))
        if form_set.is_valid():
            for form in form_set:
                form.save()
            return redirect('oks_p10')
    return redirect('oks_p10')


def oks_p10_create(request):
    if request.method == 'POST':
        form_set = P10ProtokolKGNFormSet(request.POST)
    else:
        form_set = P10ProtokolKGNFormSet()
    for form in form_set:
        print(form.as_table())
    return save_oks_p10_form(request, form_set)
