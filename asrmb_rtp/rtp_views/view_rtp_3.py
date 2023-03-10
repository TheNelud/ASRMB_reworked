from datetime import datetime

from django.forms import modelformset_factory
from django.http import Http404
from django.shortcuts import render, redirect

from asrmb_rtp.rtp_views.triggers.add_meter_reading import calculated_meter_reading

from asrmb_rtp.models import *
from asrmb_rtp.forms import *


def rtp_3(request):
    max_date_now = datetime.now().strftime("%Y-%m-%d")
    rtp_3_items = TeclossesTree.objects.filter(
        date_create__contains=max_date_now).order_by('date_update')

    url_rtp_3 = max_date_now
    if request.method == "POST":
        rtp_3_items = TeclossesTree.objects.filter(
            date_create__contains=request.POST.get('date_create', '')).order_by('date_update')
        url_rtp_3 = request.POST.get('date_create', '')
    if rtp_3_items.values():
        just_day = rtp_3_items.values()[0]['date_create']
    else:
        just_day = request.POST.get('date_create', '')

    context = {
        'max_date_now': max_date_now,
        'rtp_3_items': rtp_3_items,
        'just_day': just_day,
        'url_rtp_3': url_rtp_3,
    }
    return render(request, 'asrmb_rtp/forms/rtp_3/rtp_3.html', context)


def rtp_3_create(request):
    max_date_now = datetime.now().strftime("%Y-%m-%d")
    calculated_meter_reading()

    TeclossesTreeModelFormSet = modelformset_factory(model=TeclossesTree,
                                                     form=TeclossesTreeForm,
                                                     fields=(
                                                         'type_of_analysis', 'v_pr', 'p_pr', 't_pr', 'z_pr', 'b', 'ni',
                                                         'xr_prod', 'pr_op', 'device', 'v_p', 'tau', 'xrr_prod', 'n',
                                                         'pr_pot', 'pr_pr'),
                                                     extra=4)
    MeterReadingAllModelFormSet = modelformset_factory(model=MeterReadingAll,
                                                       form=MeterReadingAllForm,
                                                       fields=('meter_p34', 'meter_30p1', 'meter_10c1', 'meter_10c4'),
                                                       extra=2)
    form_meter = MeterReadingAllModelFormSet()
    form_set = TeclossesTreeModelFormSet(queryset=TeclossesTree.objects.none())

    if request.method == 'POST':
        form_meter = MeterReadingAllModelFormSet(data=request.POST)
        form_set = TeclossesTreeModelFormSet(data=request.POST)
        print('?????????? ??????????????: ' + str(form_set.is_valid()))
        if form_set.is_valid() and form_meter.is_valid():
            form_set.save()
            form_meter.save()
            return redirect('rtp_3')
    context = {
        'max_date_now': max_date_now,
        'form_set': form_set,
        'form_meter': form_meter,
    }
    return render(request, 'asrmb_rtp/forms/rtp_3/form_create.html', context)


def rtp_3_edit(request, date_rtp_3):
    rtp_3_items = TeclossesTree.objects.filter(
        date_create__contains=date_rtp_3).order_by('date_update')

    meter_reading_items = MeterReadingAll.objects.filter(date_create__contains=date_rtp_3).order_by('date_update')[:3]
    TeclossesTreeModelFormSet = modelformset_factory(model=TeclossesTree,
                                                     form=TeclossesTreeForm,
                                                     fields=(
                                                         'type_of_analysis', 'v_pr', 'p_pr', 't_pr', 'z_pr', 'b', 'ni',
                                                         'xr_prod', 'pr_op', 'device', 'v_p', 'tau', 'xrr_prod', 'n',
                                                         'pr_pot', 'pr_pr'),
                                                     extra=0)
    MeterReadingAllModelFormSet = modelformset_factory(model=MeterReadingAll,
                                                       form=MeterReadingAllForm,
                                                       fields=('meter_p34', 'meter_30p1', 'meter_10c1', 'meter_10c4'),
                                                       extra=0)
    if not rtp_3_items:
        raise Http404("?????? ????????????")

    if request.method == "POST":
        form_set = TeclossesTreeModelFormSet(request.POST)
        meter_reading_form = MeterReadingAllModelFormSet(request.POST)
        if form_set.is_valid() and meter_reading_form.is_valid():
            meter_reading_form.save()
            form_set.save()
            return redirect('rtp_3')
    else:
        form_set = TeclossesTreeModelFormSet(queryset=rtp_3_items)
        meter_reading_form = MeterReadingAllModelFormSet(queryset=meter_reading_items)

    context = {
        'form_set': form_set,
        'meter_reading_form': meter_reading_form,
    }
    return render(request, 'asrmb_rtp/forms/rtp_3/form_edit.html', context)


def rtp_3_delete(request, date_rtp_3):
    meter_items = MeterReadingAll.objects.filter(
        date_create__contains=date_rtp_3).order_by('date_update').values_list('id', flat=True)
    rtp_3_items = TeclossesTree.objects.filter(
        date_create__contains=date_rtp_3).order_by('date_update').values_list('id', flat=True)

    if not rtp_3_items:
        raise Http404("?????? ????????????")

    if request.method == 'POST':
        MeterReadingAll.objects.filter(pk__in=list(meter_items)).delete()
        TeclossesTree.objects.filter(pk__in=list(rtp_3_items)).delete()
        return redirect('rtp_3')
