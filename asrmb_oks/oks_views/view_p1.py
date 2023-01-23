from django.shortcuts import render, get_object_or_404, redirect
from ..models import *
# from ..forms import *

def oks_p1(request):

    context={

    }
    return render(request, 'asrmb_oks/oks_base.html', context)