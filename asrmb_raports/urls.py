from . import views
from django.conf.urls import url
from .views import *
from django.urls import path




urlpatterns = [
        
    url(r'^sar/$', views.sar, name='sar'),
    url(r'^sar/filter/$', views.filter_date_sar, name="filter_date_sar"),
    url(r'^sar/edit/$', views.sar_edit, name="sar_edit"),

]