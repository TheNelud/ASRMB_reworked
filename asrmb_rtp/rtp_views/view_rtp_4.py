from datetime import datetime

from asrmb_rtp.models import *
from asrmb_rtp.forms import *
from django.forms import modelformset_factory
from django.http import Http404
from django.shortcuts import render, redirect

from asrmb_oks.models import P5DeterminationOfTheComponentComposition


def rtp_4(request):
    max_date_now = datetime.now().strftime("%Y-%m-%d")
    rtp_4_items = RecyclingcalcOne.objects.filter(
        date_create__contains=max_date_now).order_by('date_update')
    rtp_4_time_items = RecyclingcalcOneTime.objects.filter(
        date_create__contains=max_date_now).order_by('date_update')

    url_rtp_4 = max_date_now

    if request.method == 'POST':
        rtp_4_items = RecyclingcalcOne.objects.filter(
            date_create__contains=request.POST.get('date_create', '')).order_by('date_update')
        rtp_4_time_items = RecyclingcalcOneTime.objects.filter(
            date_create__contains=request.POST.get('date_create', '')).order_by('date_update')
        url_rtp_4 = request.POST.get('date_create', '')

    if rtp_4_items.values():
        just_day = rtp_4_items.values()[0]['date_create']
    else:
        just_day = request.POST.get('date_create', '')
    context = {
        'max_date_now': max_date_now,
        'rtp_4_items': rtp_4_items,
        'rtp_4_time_items': rtp_4_time_items,
        'just_day': just_day,
        'url_rtp_4': url_rtp_4,
    }
    return render(request, 'asrmb_rtp/forms/rtp_4/rtp_4.html', context)


def rtp_4_create(request):
    max_date_now = datetime.now().strftime("%Y-%m-%d")

    mj_items = P5DeterminationOfTheComponentComposition.objects.filter(date_create__contains=max_date_now)

    RecyclingcalcOneModelFormSet = modelformset_factory(model=RecyclingcalcOne,
                                                        form=RecyclingcalcOneForm,
                                                        fields=(
                                                            'type', 'aij', 'bij', 'tauij',
                                                            'a_ij', 'mi', 'q_yp', 't_type',
                                                            't_aij', 't_bij', 't_tauij',
                                                            't_a_ij', 't_mi', 't_q_yp')
                                                        , extra=4)
    RecyclingcalcOneTimeModelFormSet = modelformset_factory(model=RecyclingcalcOneTime,
                                                            form=RecyclingcalcOneTimeForm,
                                                            fields=('type', 'time'),
                                                            extra=5)

    form_set_ro = RecyclingcalcOneModelFormSet(queryset=RecyclingcalcOne.objects.none(),
                                               initial=[{'type': 'Фланц.соед.КУ-1', 't_type': 'Предохр. Клапан КУ-1'},
                                                        {'type': 'Фланц.соед.КУ-2', 't_type': 'Предохр. Клапан КУ-2'},
                                                        {'type': 'ЗРА КУ-1', 't_type': 'Уплотнения валов КУ-1'},
                                                        {'type': 'ЗРА КУ-2', 't_type': 'Уплотнения валов КУ-2'}])

    form_set_ro_time = RecyclingcalcOneTimeModelFormSet(queryset=RecyclingcalcOneTime.objects.none(),
                                                        initial=[{'type': 'КУ-1'},
                                                                 {'type': 'КУ-2'},
                                                                 {'type': '1 т.н. УСК'},
                                                                 {'type': '2 т.н. УСК'},
                                                                 {'type': '3 т.н. УСК'}])

    if request.method == "POST":
        form_set_ro = RecyclingcalcOneModelFormSet(data=request.POST)
        form_set_ro_time = RecyclingcalcOneTimeModelFormSet(data=request.POST)
        if form_set_ro.is_valid() and form_set_ro_time.is_valid():
            form_set_ro.save()
            form_set_ro_time.save()
            return redirect('rtp_4')

    context = {
        'max_date_now': max_date_now,
        'form_set_ro': form_set_ro,
        'form_set_ro_time': form_set_ro_time,
        'mj_items': mj_items.values()[11]['total_molar_mass'],
    }

    return render(request, 'asrmb_rtp/forms/rtp_4/form_create.html', context)


def rtp_4_edit(request, date_rtp_4):
    rtp_4_items = RecyclingcalcOne.objects.filter(
        date_create__contains=date_rtp_4).order_by('date_update')

    rtp_4_time_items = RecyclingcalcOneTime.objects.filter(
        date_create__contains=date_rtp_4).order_by('date_update')

    mj_items = P5DeterminationOfTheComponentComposition.objects.filter(date_create__contains=date_rtp_4)

    RecyclingcalcOneModelFormSet = modelformset_factory(model=RecyclingcalcOne,
                                                        form=RecyclingcalcOneForm,
                                                        fields=(
                                                            'type', 'aij', 'bij', 'tauij',
                                                            'a_ij', 'mi', 'q_yp', 't_type',
                                                            't_aij', 't_bij', 't_tauij',
                                                            't_a_ij', 't_mi', 't_q_yp'),
                                                        extra=0)
    RecyclingcalcOneTimeModelFormSet = modelformset_factory(model=RecyclingcalcOneTime,
                                                            form=RecyclingcalcOneTimeForm,
                                                            fields=('type', 'time'),
                                                            extra=0
                                                            )

    if not rtp_4_items:
        raise Http404('Нет данных')

    if request.method == "POST":
        form_set_ro = RecyclingcalcOneModelFormSet(data=request.POST)
        form_set_ro_time = RecyclingcalcOneTimeModelFormSet(data=request.POST)
        if form_set_ro.is_valid() and form_set_ro_time.is_valid():
            form_set_ro.save()
            form_set_ro_time.save()
            return redirect('rtp_4')
    else:
        form_set_ro = RecyclingcalcOneModelFormSet(queryset=rtp_4_items)
        form_set_ro_time = RecyclingcalcOneTimeModelFormSet(queryset=rtp_4_time_items)

    context = {
        'form_set_ro': form_set_ro,
        'form_set_ro_time': form_set_ro_time,
        'mj_items': mj_items.values()[11]['total_molar_mass'],
    }

    return render(request, 'asrmb_rtp/forms/rtp_4/form_edit.html', context)


def rtp_4_delete(request, date_rtp_4):
    rtp_4_items = RecyclingcalcOne.objects.filter(
        date_create__contains=date_rtp_4).order_by('date_update').values_list('id', flat=True)

    rtp_4_time_items = RecyclingcalcOneTime.objects.filter(
        date_create__contains=date_rtp_4).order_by('date_update').values_list('id', flat=True)

    if not rtp_4_items:
        raise Http404("Нет данных")

    if request.method == "POST":
        RecyclingcalcOne.objects.filter(pk__in=list(rtp_4_items)).delete()
        RecyclingcalcOneTime.objects.filter(pk__in=list(rtp_4_time_items)).delete()
        return redirect('rtp_4')
