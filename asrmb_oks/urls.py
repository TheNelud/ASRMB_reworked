from .oks_views.view_p1 import *
from .oks_views.view_p2 import *
from .oks_views.view_p3 import *
from .oks_views.view_p4 import *
from .oks_views.view_p5 import *
from .oks_views.view_p6 import *
from .oks_views.view_p7 import *
from .oks_views.view_p8 import *
from .views import *
from django.urls import path

urlpatterns = [

    path('p1/', oks_p1, name='oks_p1'),
    path('p1/create/', oks_p1_create, name='oks_p1_create'),
    # path('p1/edit/', oks_p1_edit, name='oks_p1_edit'),

    path('p2/', oks_p2, name='oks_p2'),
    path('p2/create/', oks_p2_create, name='oks_p2_create'),

    path('p3/', oks_p3, name='oks_p3'),
    path('p3/create/', oks_p3_create, name='oks_p3_create'),

    path('p4/', oks_p4, name='oks_p4'),
    path('p4/create/', oks_p4_create, name='oks_p4_create'),

    path('p5/', oks_p5, name='oks_p5'),
    path('p5/create/', oks_p5_create, name='oks_p5_create'),

    path('p6/', oks_p6, name='oks_p6'),
    path('p6/create/', oks_p6_create, name='oks_p6_create'),

    path('p7/', oks_p7, name='oks_p7'),
    path('p7/create/', oks_p7_create, name='oks_p7_create'),

    path('p8/', oks_p8, name='oks_p8'),
    path('p8/create/', oks_p8_create, name='oks_p8_create'),

]
