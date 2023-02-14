from datetime import datetime

from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404

from ..models import *
from ..forms import *
from asrmb_oks.models import NrProd
from asrmb_oks.forms import NrProdForm


def rtp_2(request):
    max_date_now = datetime.now().strftime("%Y-%m-%d")
    rtp_2_items = TeclossesTwo.objects.filter(
        date_create__contains=max_date_now).order_by('date_update')

    url_rtp_2 = max_date_now
    if request.method == "POST":
        rtp_2_items = TeclossesTwo.objects.filter(
            date_create__contains=request.POST.get('date_create', '')).order_by('date_update')
        url_rtp_2 = request.POST.get('date_create', '')
    if rtp_2_items.values():
        just_day = rtp_2_items.values()[0]['date_create']
    else:
        just_day = request.POST.get('date_create', '')

    context = {
        'max_date_now': max_date_now,
        'rtp_2_items': rtp_2_items,
        'just_day': just_day,
        'url_rtp_2': url_rtp_2,
    }
    return render(request, 'asrmb_rtp/forms/rtp_2/rtp_2.html', context)


def rtp_2_create(request, date_rtp_2):
    max_date_now = datetime.now().strftime("%Y-%m-%d")
    meter_reading_form = MeterReading30P1ModelFormSet(queryset=MeterReading30P1.objects.none())
    TeclossesTwoModelFormSet = modelformset_factory(model=TeclossesTwo,
                                                    form=TeclossesTwoForm,
                                                    fields=('name', 'qgr_sh', 'ng_prod', 'ng_pl', 'xg_prod', 'pgr_sh'),
                                                    extra=2)
    form_set = TeclossesTwoModelFormSet(queryset=TeclossesTwo.objects.none())
    items_nr_prod = NrProd.objects.filter(date_create__contains=date_rtp_2)

    print(items_nr_prod.values())


    if request.method == 'POST':

        meter_reading_form = MeterReading30P1ModelFormSet(request.POST)
        form_set = TeclossesTwoModelFormSet(data=request.POST)

        print('Форма валидна: ' + str(form_set.is_valid()) + str(meter_reading_form.is_valid()))
        if form_set.is_valid() and meter_reading_form.is_valid():
            meter_reading_form.save()
            form_set.save()
            return redirect('rtp_2')

    context = {
        'max_date_now': max_date_now,
        'form_set': form_set,
        'meter_reading_form': meter_reading_form,
        'items_nr_prod':items_nr_prod,
    }
    return render(request, 'asrmb_rtp/forms/rtp_2/form_create.html', context)


def rtp_2_edit(request, date_rtp_2):
    rtp_2_items = TeclossesTwo.objects.filter(
        date_create__contains=date_rtp_2).order_by('date_update')

    if not rtp_2_items:
        raise Http404("Нет данных")

    if request.method == 'POST':
        form_set = TeclossesTwoModelFormSet(request.POST)

        print('Форма валидна: ' + str(form_set.is_valid()))
        print(form_set.as_table())
        if form_set.is_valid():
            form_set.save()
            return redirect('rtp_2')

    else:
        form_set = TeclossesTwoModelFormSet(queryset=rtp_2_items)

        print(form_set.as_table())

    context = {
        'just_day': date_rtp_2,
        'form_set': form_set,
    }
    return render(request, 'asrmb_rtp/forms/rtp_2/form_edit.html', context)


def rtp_2_delete(request, date_rtp_2):
    rtp_2_items = TeclossesTwo.objects.filter(
        date_create__contains=date_rtp_2).order_by('date_update').values_list('id', flat=True)
    print(rtp_2_items)

    if not rtp_2_items:
        raise Http404("Нет данных")

    if request.method == 'POST':
        TeclossesTwo.objects.filter(pk__in=list(rtp_2_items)).delete()
        return redirect('rtp_2')
