from .oks_views.view_p1 import *
from .views import *
from django.urls import path

urlpatterns = [


    path('p1/', oks_p1, name='oks_p1'),
    path('p1/create/', oks_p1_create, name='oks_p1_create'),
    path('p1/edit/', oks_p1_edit, name='oks_p1_edit'),
]