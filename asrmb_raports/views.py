from django.shortcuts import render
from .models import *
from .forms import *

from datetime import datetime, timedelta


# Create your views here.
"""Для СЭР"""
def sar(request):

    max_date_now = datetime.now().strftime("%Y-%m-%d")
    print(max_date_now)
    items_day = Ser_per_day.objects.all().order_by('-id')[:1]
    items_month =Ser_per_month.objects.all().order_by('-id')[:1]
    return render(request, 'sar.html', context={'items_day' : items_day,
                                                'items_month' : items_month,
                                                'max_date_now':max_date_now}
                                            )

def filter_date_sar(request):
    print (request.path)
    max_date_now = datetime.now().strftime("%Y-%m-%d")
    items_day = Ser_per_day.objects.filter(date_update__contains=request.POST.get('date_update','')).order_by('-id')[:1]
    items_month =Ser_per_month.objects.filter(date_update__contains=request.POST.get('date_update','')).order_by('-id')[:1]
    print(items_day.values())
    print(items_month.values())
    if items_day.values():
        just_day = items_day.values()[0]['date_update']
        delta_day = (just_day - timedelta(days=1)).strftime("%d.%m.%Y")
    else:
        delta_day = "-"
    return render(request, 'sar.html', context={'items_ser_day' : items_day,
                                                    'items_ser_month' : items_month,
                                                    'max_date_now':max_date_now,
                                                    'delta_day': delta_day
                                                    })
    


def sar_edit(request):
    items_ser_day = Ser_per_day.objects.filter(date_update__contains=request.POST.get('date_update','')).order_by('-id')[:1]
    items_ser_month =Ser_per_month.objects.filter(date_update__contains=request.POST.get('date_update','')).order_by('-id')[:1]
    max_date_now = datetime.now().strftime("%Y-%m-%d")
    if request.method == "POST":
        form_day = Ser_per_day_form(request.POST)
        form_month = Ser_per_month_form(request.POST)
        print(form_day,'________', form_month)
        if form_day.is_valid() and form_month.is_valid():
            form_day.save()
            form_month.save()
            print('SAVE')
            # return render(request, 'sar.html', context={'items_ser_day':items_ser_day})
    else:
        form_day = Ser_per_day_form()
        form_month = Ser_per_month_form()
    context = { 'form_day': form_day,
                'form_month':form_month,
                'items_ser_day':items_ser_day,
                'items_ser_month':items_ser_month,
                'max_date_now':max_date_now
                }
    return render(request,'sar_edit.html', context)


def filter_date_sar_edit(request):
    print (request.path)
    max_date_now = datetime.now().strftime("%Y-%m-%d")
    items_day = Ser_per_day.objects.filter(date_update__contains=request.POST.get('date_update','')).order_by('-id')[:1]
    items_month =Ser_per_month.objects.filter(date_update__contains=request.POST.get('date_update','')).order_by('-id')[:1]
    print(items_day.values())
    print(items_month.values())
    if items_day.values():
        just_day = items_day.values()[0]['date_update']
        delta_day = (just_day - timedelta(days=1)).strftime("%d.%m.%Y")
    else:
        delta_day = "-"
    return render(request, 'sar_edit.html', context={'items_ser_day' : items_day,
                                                    'items_ser_month' : items_month,
                                                    'max_date_now':max_date_now,
                                                    'delta_day': delta_day
                                                    })