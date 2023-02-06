from datetime import datetime

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string

from ..models import *

from ..forms import *


def oks_p2(request):
    max_date_now = datetime.now().strftime("%Y-%m-%d")
    oks_p2_items = P2ComponentCompositionOfGas.objects.filter(date_create__contains=max_date_now).order_by('id')[:12]
    form_set = P2ComponentCompositionOfGasFormSet()
    if request.method == "POST":
        oks_p2_items = P2ComponentCompositionOfGas.objects.filter(
            date_create__contains=request.POST.get('date_create', ''))[:12]
        form_set = P2ComponentCompositionOfGasFormSet(initial=oks_p2_items.values())
    if oks_p2_items.values():
        just_day = oks_p2_items.values()[0]['date_create']
    else:
        just_day = request.POST.get('date_create', '')

    context = {
        'max_date_now': max_date_now,
        'oks_p2_items': oks_p2_items,
        'just_day': just_day,
        'form_set': form_set,
    }
    return render(request, 'asrmb_oks/forms/oks_p2/oks_p2.html', context)


def save_oks_p2_form(request, form_set):
    if request.method == 'POST':
        print('Форма валидна: ' + str(form_set.is_valid()))
        if form_set.is_valid():
            for form in form_set:
                form.save()
            return redirect('oks_p2')
    return redirect('oks_p2')


def oks_p2_create(request):
    if request.method == 'POST':
        form_set = P2ComponentCompositionOfGasFormSet(request.POST)
    else:
        form_set = P2ComponentCompositionOfGasFormSet()
    return save_oks_p2_form(request, form_set)


def oks_p2_edit(request):
    pass
