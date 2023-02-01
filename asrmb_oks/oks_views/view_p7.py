from datetime import datetime

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string

from ..models import *

from ..forms import *


def oks_p7(request):
    max_date_now = datetime.now().strftime("%Y-%m-%d")
    oks_p7_items = P7CompositionOfGas10c.objects.filter(date_create__contains=max_date_now).order_by('id')[:12]

    form_set = P7CompositionOfGas10cFormSet()
    if request.method == "POST":
        oks_p7_items = P7CompositionOfGas10c.objects.filter(
            date_create__contains=request.POST.get('date_create', ''))[:12]

    if oks_p7_items.values():
        just_day = oks_p7_items.values()[0]['date_create']
    else:
        just_day = request.POST.get('date_create', '')

    context = {
        'max_date_now': max_date_now,
        'oks_p7_items': oks_p7_items,
        'just_day': just_day,
        'form_set': form_set,
    }
    return render(request, 'asrmb_oks/forms/oks_p7/oks_p7.html', context)


def save_oks_p7_form(request, form_set):
    if request.method == 'POST':
        print('Форма валидна: ' + str(form_set.is_valid()))
        if form_set.is_valid():
            for form in form_set:
                form.save()
            return redirect('oks_p7')
    return redirect('oks_p7')


def oks_p7_create(request):
    if request.method == 'POST':
        form_set = P7CompositionOfGas10cFormSet(request.POST)
    else:
        form_set = P7CompositionOfGas10cFormSet()
    return save_oks_p7_form(request, form_set)

