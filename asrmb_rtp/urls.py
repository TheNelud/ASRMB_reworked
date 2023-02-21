from .rtp_views.view_rtp_1 import *
from .rtp_views.view_rtp_2 import *
from .rtp_views.view_rtp_3 import *
from .rtp_views.view_rtp_4 import *

from . import views
from django.urls import path

urlpatterns = [

    path('rtp_1/', rtp_1, name='rtp_1'),
    path('rtp_1/create/', rtp_1_create, name='rtp_1_create'),
    path('rtp_1/edit/<slug:date_rtp_1>', rtp_1_edit, name='rtp_1_edit'),
    path('rtp_1/delete/<slug:date_rtp_1>', rtp_1_delete, name='rtp_1_delete'),

    path('rtp_2/', rtp_2, name='rtp_2'),
    path('rtp_2/create/<slug:date_rtp_2>', rtp_2_create, name='rtp_2_create'),
    path('rtp_2/edit/<slug:date_rtp_2>', rtp_2_edit, name='rtp_2_edit'),
    path('rtp_2/delete/<slug:date_rtp_2>', rtp_2_delete, name='rtp_2_delete'),

    path('rtp_3/', rtp_3, name='rtp_3'),
    path('rtp_3/create/', rtp_3_create, name='rtp_3_create'),
    path('rtp_3/edit/<slug:date_rtp_3>', rtp_3_edit, name='rtp_3_edit'),
    path('rtp_3/delete/<slug:date_rtp_3>', rtp_3_delete, name='rtp_3_delete'),

    path('rtp_4/', rtp_4, name='rtp_4'),
]
