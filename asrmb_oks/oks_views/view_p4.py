from datetime import datetime

from django.http import JsonResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from django.template.loader import render_to_string

from ..models import *

from ..forms import *



def oks_p4(request):
    max_date_now = datetime.now().strftime("%Y-%m-%d")
    oks_p4_items = P4GasCompositionToTheProtocol.objects.filter(
        date_create__contains=max_date_now).order_by('date_update')[:12]
    ng_prod_items = NrProd.objects.filter(date_create__contains=max_date_now).order_by('date_update')[:1]

    url_oks_p4 = max_date_now
    if request.method == "POST":
        oks_p4_items = P4GasCompositionToTheProtocol.objects.filter(
            date_create__contains=request.POST.get('date_create', '')).order_by('date_update')[:12]
        ng_prod_items = NrProd.objects.filter(
            date_create__contains=request.POST.get('date_create', '')).order_by('date_update')[:1]
        url_oks_p4 = request.POST.get('date_create', '')
    if oks_p4_items.values():
        just_day = oks_p4_items.values()[0]['date_create']
    else:
        just_day = request.POST.get('date_create', '')

    context = {
        'max_date_now': max_date_now,
        'oks_p4_items': oks_p4_items,
        'ng_prod_items': ng_prod_items,
        'just_day': just_day,
        'url_oks_p4': url_oks_p4,
    }
    return render(request, 'asrmb_oks/forms/oks_p4/oks_p4.html', context)


def oks_p4_create(request):
    max_date_now = datetime.now().strftime("%Y-%m-%d")
    form_set = P4GasCompositionToTheProtocolFormSet()
    form_ng_prod = NrProdForm()
    print(form_ng_prod.as_p())
    if request.method == 'POST':
        form_set = P4GasCompositionToTheProtocolFormSet(request.POST)
        form_ng_prod = NrProdForm(request.POST)
        print('Форма валидна: ' + str(form_set.is_valid()) + str(form_ng_prod.is_valid()))
        if form_set.is_valid() and form_ng_prod.is_valid():
            form_ng_prod.save()
            for form in form_set:
                form.save()
            return redirect('oks_p4')

    context = {
        'max_date_now': max_date_now,
        'form_set': form_set,
        'form_ng_prod': form_ng_prod
    }
    return render(request, 'asrmb_oks/forms/oks_p4/form_create.html', context)


def oks_p4_edit(request, date_oks_p4):
    oks_p4_items = P4GasCompositionToTheProtocol.objects.filter(
        date_create__contains=date_oks_p4).order_by('date_update')[:12]

    if not oks_p4_items:
        raise Http404("Нет данных")

    if request.method == 'POST':
        form_set = P4ModelFormSet(request.POST)
        print('Форма валидна: ' + str(form_set.is_valid()))
        if form_set.is_valid():
            for form in form_set:
                form.save()
            return redirect('oks_p4')

    else:
        form_set = P4ModelFormSet(queryset=oks_p4_items)
        for f in form_set:
            print(f.as_table())

    context = {
        'just_day': date_oks_p4,
        'form_set': form_set,
    }
    return render(request, 'asrmb_oks/forms/oks_p4/form_edit.html', context)


def oks_p4_delete(request, date_oks_p4):
    oks_p4_items = P4GasCompositionToTheProtocol.objects.filter(
        date_create__contains=date_oks_p4).order_by('date_update')[:12].values_list('id', flat=True)
    print(oks_p4_items)

    if not oks_p4_items:
        raise Http404("Нет данных")

    if request.method == 'POST':
        P4GasCompositionToTheProtocol.objects.filter(pk__in=list(oks_p4_items)).delete()
        return redirect('oks_p4')
