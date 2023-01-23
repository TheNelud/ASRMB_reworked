from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from .utils import *

# Create your views here.
"""Для СЭР"""


def sar(request):
    max_date_now = datetime.now().strftime("%Y-%m-%d")

    """Формирование отчета последних принятых данных"""

    items_day = Ser_per_day.objects.order_by('-id')[:1]
    items_month = Ser_per_month.objects.all().order_by('-id')[:1]
    url_ser_day = items_day[0].date_create

    if request.method == "POST":
        items_day = Ser_per_day.objects.filter(date_create__contains=request.POST.get('date_create', '')).order_by(
            '-id')[
                    :1]
        items_month = Ser_per_month.objects.filter(date_create__contains=request.POST.get('date_create', '')).order_by(
            '-id')[:1]
        url_ser_day = items_day[0].date_create

    if items_day.values():
        just_day = items_day.values()[0]['date_create']
        delta_day = (just_day - timedelta(days=1)).strftime("%d.%m.%Y")
    else:
        just_day = request.POST.get('date_create', '')
        delta_day = "-"

    context = {'items_ser_day': items_day,
               'items_ser_month': items_month,
               'max_date_now': max_date_now,
               'just_day': just_day,
               'delta_day': delta_day,
               'url_ser_day': url_ser_day,

               }

    return render(request, 'asrmb_raports/sar.html', context)


def sar_edit(request, date_sar):
    items_ser_day = Ser_per_day.objects.filter(date_create=date_sar).order_by(
        '-id')[:1]
    items_ser_month = Ser_per_month.objects.filter(date_create=date_sar).order_by(
        '-id')[:1]

    just_day = items_ser_day.values()[0]['date_create']
    delta_day = (just_day - timedelta(days=1)).strftime("%d.%m.%Y")
    max_date_now = datetime.now().strftime("%Y-%m-%d")

    if request.method == "POST":
        items_ser_day = get_object_or_404(Ser_per_day, pk=items_ser_day[0].pk)
        items_ser_month = get_object_or_404(Ser_per_month, pk=items_ser_month[0].pk)
        form_day = Ser_per_day_form(request.POST, instance=items_ser_day)
        form_month = Ser_per_month_form(request.POST, instance=items_ser_month)
        if form_day.is_valid() and form_month.is_valid():
            print(form_day.cleaned_data, '\n________\n', form_month.cleaned_data)
            form_day.save()
            form_month.save()
            print('UPDATE')
            return redirect('sar')
    else:
        form_day = Ser_per_day_form()
        form_month = Ser_per_month_form()

    context = {'form_day': form_day,
               'form_month': form_month,
               'items_ser_day': items_ser_day,
               'items_ser_month': items_ser_month,
               'max_date_now': max_date_now,
               'delta_day': delta_day,
               'just_day': just_day
               }
    return render(request, 'asrmb_raports/forms/sar/sar_edit.html', context)


"""Для МЭР"""


def mar(request):
    max_date_now = datetime.now().strftime("%Y-%m-%d")
    items_month = Mer_per_month.objects.all().order_by('-date_update')[:1]
    url_mer_day = items_month[0].date_create

    if request.method == "POST":
        items_month = Mer_per_month.objects.filter(date_create__contains=request.POST.get('date_create', '')).order_by(
            '-id')[:1]
        url_mer_day = items_month[0].date_create

    if items_month.values():
        just_day = items_month.values()[0]['date_create']
        delta_day = (just_day - timedelta(days=1)).strftime("%d.%m.%Y")
    else:
        just_day = request.POST.get('date_create', '')
        delta_day = "-"

    context = {
        "itemss_month": items_month,
        'max_date_now': max_date_now,
        'url_mer_day': url_mer_day,
        'just_day': just_day,
        'delta_day': delta_day
    }

    return render(request, 'asrmb_raports/mar.html', context)


def mar_edit(request, date_mar):
    items_month = Mer_per_month.objects.filter(date_create=date_mar).order_by('-id')[:1]

    just_day = items_month.values()[0]['date_create']
    delta_day = (just_day - timedelta(days=1)).strftime("%d.%m.%Y")
    max_date_now = datetime.now().strftime("%Y-%m-%d")

    if request.method == "POST":
        items_month = get_object_or_404(Mer_per_month, pk=items_month[0].pk)
        form_month = Mer_per_month_form(request.POST, instance=items_month)

        if form_month.is_valid():
            form_month.save()
            print('UPDATE')
            return redirect('mar')
    else:
        form_month = Mer_per_month_form()

    context = {
        'form_month': form_month,
        'itemss_month': items_month,
        'max_date_now': max_date_now,
        'delta_day': delta_day,
        'just_day': just_day
    }
    return render(request, 'asrmb_raports/forms/mar/mar_edit.html', context)


"""Для МЭГ"""


def mag(request):

    max_date_now = datetime.now().strftime("%Y-%m-%d")
    items_tech = Sen_equip.objects.all().order_by('-date_update')[:1]
    items_balance = Balance.objects.all().order_by('-date_update')[:1]
    url_mer_day = items_tech[0].date_create

    if request.method == "POST":
        items_tech = Sen_equip.objects.filter(date_create__contains=request.POST.get('date_create', '')).order_by(
            '-id')[:1]
        items_balance = Balance.objects.filter(date_create__contains=request.POST.get('date_create', '')).order_by(
            '-id')[:1]
        url_mer_day = items_tech[0].date_create

    if items_tech.values():
        just_day = items_tech.values()[0]['date_create']
        delta_day = (just_day - timedelta(days=1)).strftime("%d.%m.%Y")
    else:
        just_day = request.POST.get('date_create', '')
        delta_day = "-"

    context = {
        "itemss_tech":items_tech,
        "itemss_balance":items_balance,
        'max_date_now':max_date_now,
        'url_mer_day': url_mer_day,
        'just_day': just_day,
        'delta_day': delta_day
    }

    return render(request, 'asrmb_raports/mag.html', context)
