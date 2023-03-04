from django.shortcuts import render


# Create your views here.
def base(request):
    return render(request, "asrmb_main/base_tasks.html")
