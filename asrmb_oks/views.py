from django.shortcuts import render


# Create your views here.
def oks_base(request):
    return render(request, 'asrmb_oks/oks_base.html')
