from datetime import datetime

from django.shortcuts import render, get_object_or_404, redirect
from ..models import *

from ..forms import *



def oks_p1(request):
    max_date_now = datetime.now().strftime("%Y-%m-%d")
    oks_p1_items = P1ComponentCompositionOfUnstableCondensate.objects.all().order_by('id')[:12]
    url_oks_p1 = oks_p1_items[0].date_create


    # form_one = P1ComponentCompositionOfUnstableCondensateForm()
    # for form in form_one:
    #     print(form.as_text())

    form_set = P1ComponentCompositionOfUnstableCondensateFormSet()
    # model_form_set = P1ComponentCompositionOfUnstableCondensateModelFormSet(queryset=oks_p1_items)
    for form in form_set:
        print(form.as_table())

    if request.method == "POST":
        oks_p1_items = P1ComponentCompositionOfUnstableCondensate.objects.filter(
            date_create__contains=request.POST.get('date_create', ''))[:12]
        model_form_set = P1ComponentCompositionOfUnstableCondensateModelFormSet(queryset=oks_p1_items)
        url_oks_p1 = oks_p1_items[0].date_create

    if oks_p1_items.values():
        just_day = oks_p1_items.values()[0]['date_create']
    else:
        just_day = request.POST.get('date_create', '')

    context = {
        'max_date_now': max_date_now,
        'oks_p1_items': oks_p1_items,
        'url_oks_p1': url_oks_p1,
        'just_day': just_day,
        'form_set':form_set,
    }
    return render(request, 'asrmb_oks/forms/oks_p1/oks_p1.html', context)

def oks_p1_create(request):
    if request.method == 'POST':
        form_set = P1ComponentCompositionOfUnstableCondensateFormSet(request.POST)
        print(form_set.cleaned_data)
        # if form.is_valid():
        #     form.save()
        #     return redirect('oks_p1')



