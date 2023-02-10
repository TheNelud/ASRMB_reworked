from .rtp_views.view_rtp_1 import *

from . import views
from django.urls import path

urlpatterns = [

    path('rtp_1/', rtp_1, name='rtp_1'),
    path('rtp_1/create/', rtp_1_create, name='rtp_1_create'),
    path('rtp_1/edit/<slug:date_rtp_1>', rtp_1_edit, name='rtp_1_edit'),
    path('rtp_1/delete/<slug:date_rtp_1>', rtp_1_delete, name='rtp_1_delete'),
]
