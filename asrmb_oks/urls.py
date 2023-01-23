from .oks_views.view_p1 import *
from .views import *
from django.urls import path

urlpatterns = [
    path('', oks_base, name='oks_base'),

    path('p1/', oks_p1, name='oks_p1')
]