from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.base, name='base'),

    path('raports/', include('asrmb_raports.urls')),
    path('oks/', include('asrmb_oks.urls')),
    path('rtp/', include('asrmb_rtp.urls')),
]
