from datetime import datetime

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string

from ..models import *

from ..forms import *


def oks_p3(request):
    max_date_now = datetime.now().strftime("%Y-%m-%d")
    oks_p3_items = P3DeterminationOfTheComponentOfGas.objects.filter(date_create__contains=max_date_now).order_by('id')[:12]

    form_set = P3DeterminationOfTheComponentOfGasFormSet()
    if request.method == "POST":
        oks_p3_items = P3DeterminationOfTheComponentOfGas.objects.filter(
            date_create__contains=request.POST.get('date_create', ''))[:12]

    if oks_p3_items.values():
        just_day = oks_p3_items.values()[0]['date_create']
    else:
        just_day = request.POST.get('date_create', '')

    context = {
        'max_date_now': max_date_now,
        'oks_p3_items': oks_p3_items,
        'just_day': just_day,
        'form_set': form_set,
    }
    return render(request, 'asrmb_oks/forms/oks_p3/oks_p3.html', context)


def save_oks_p3_form(request, form_set):
    if request.method == 'POST':
        print('Форма валидна: ' + str(form_set.is_valid()))
        if form_set.is_valid():
            for form in form_set:
                form.save()
            return redirect('oks_p3')
    return redirect('oks_p3')


def oks_p3_create(request):
    if request.method == 'POST':
        form_set = P3DeterminationOfTheComponentOfGasFormSet(request.POST)
    else:
        form_set = P3DeterminationOfTheComponentOfGasFormSet()
    return save_oks_p3_form(request, form_set)

