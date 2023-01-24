from .oks_views.view_p1 import *
from .views import *
from django.urls import path

urlpatterns = [


    path('p1/', oks_p1, name='oks_p1'),

]