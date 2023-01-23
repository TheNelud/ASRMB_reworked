from .models import *
from datetime import datetime, timedelta


class SarRaportMixin:

    def get_content(self, **kwargs):
        context = kwargs
        max_date_now = datetime.now().strftime("%Y-%m-%d")
        items_day = Ser_per_day.objects.all().order_by('-id')[:1]
        items_month = Ser_per_month.objects.all().order_by('-id')[:1]

        if items_day.values():
            just_day = items_day.values()[0]['date_update']
            delta_day = (just_day - timedelta(days=1)).strftime("%d.%m.%Y")
        else:
            delta_day = "-"

        context['max_date_now'] = max_date_now
        context['items_ser_day'] = items_day
        context['items_ser_month'] = items_month
        context['delta_day'] = delta_day

        return context

    def get_filter_content(self, request, **kwargs):
        context = kwargs
        max_date_now = datetime.now().strftime("%Y-%m-%d")
        items_day = Ser_per_day.objects.filter(date_update__contains=request.POST.get('date_update', '')).order_by(
            '-id')[
                    :1]
        items_month = Ser_per_month.objects.filter(date_update__contains=request.POST.get('date_update', '')).order_by(
            '-id')[:1]

        if items_day.values():
            just_day = items_day.values()[0]['date_update']
            delta_day = (just_day - timedelta(days=1)).strftime("%d.%m.%Y")
        else:
            delta_day = "-"

        context['max_date_now'] = max_date_now
        context['items_ser_day'] = items_day
        context['items_ser_month'] = items_month
        context['delta_day'] = delta_day

        return context
