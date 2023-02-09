from .oks_views.view_p1 import *
from .oks_views.view_p2 import *
from .oks_views.view_p3 import *
from .oks_views.view_p4 import *
from .oks_views.view_p5 import *
from .oks_views.view_p6 import *
from .oks_views.view_p7 import *
from .oks_views.view_p8 import *
from .oks_views.view_p9 import *
from .oks_views.view_p10 import *
from .views import *
from django.urls import path

urlpatterns = [

    path('p1/', oks_p1, name='oks_p1'),
    path('p1/create/', oks_p1_create, name='oks_p1_create'),
    path('p1/edit/<slug:date_oks_p1>', oks_p1_edit, name='oks_p1_edit'),
    path('p1/delete/<slug:date_oks_p1>', oks_p1_delete, name='oks_p1_delete'),

    path('p2/', oks_p2, name='oks_p2'),
    path('p2/create/', oks_p2_create, name='oks_p2_create'),
    path('p2/edit/<slug:date_oks_p2>', oks_p2_edit, name='oks_p2_edit'),
    path('p2/delete/<slug:date_oks_p2>', oks_p2_delete, name='oks_p2_delete'),

    path('p3/', oks_p3, name='oks_p3'),
    path('p3/create/', oks_p3_create, name='oks_p3_create'),
    path('p3/edit/<slug:date_oks_p3>', oks_p3_edit, name='oks_p3_edit'),
    path('p3/delete/<slug:date_oks_p3>', oks_p3_delete, name='oks_p3_delete'),

    path('p4/', oks_p4, name='oks_p4'),
    path('p4/create/', oks_p4_create, name='oks_p4_create'),
    path('p4/edit/<slug:date_oks_p4>', oks_p4_edit, name='oks_p4_edit'),
    path('p4/delete/<slug:date_oks_p4>', oks_p4_delete, name='oks_p4_delete'),

    path('p5/', oks_p5, name='oks_p5'),
    path('p5/create/', oks_p5_create, name='oks_p5_create'),
    path('p5/edit/<slug:date_oks_p5>', oks_p5_edit, name='oks_p5_edit'),
    path('p5/delete/<slug:date_oks_p5>', oks_p5_delete, name='oks_p5_delete'),

    path('p6/', oks_p6, name='oks_p6'),
    path('p6/create/', oks_p6_create, name='oks_p6_create'),
    path('p6/edit/<slug:date_oks_p6>', oks_p6_edit, name='oks_p6_edit'),
    path('p6/delete/<slug:date_oks_p6>', oks_p6_delete, name='oks_p6_delete'),

    path('p7/', oks_p7, name='oks_p7'),
    path('p7/create/', oks_p7_create, name='oks_p7_create'),
    path('p7/edit/<slug:date_oks_p7>', oks_p7_edit, name='oks_p7_edit'),
    path('p7/delete/<slug:date_oks_p7>', oks_p7_delete, name='oks_p7_delete'),

    path('p8/', oks_p8, name='oks_p8'),
    path('p8/create/', oks_p8_create, name='oks_p8_create'),
    path('p8/edit/<slug:date_oks_p8>', oks_p8_edit, name='oks_p8_edit'),
    path('p8/delete/<slug:date_oks_p8>', oks_p8_delete, name='oks_p8_delete'),

    path('p9/', oks_p9, name='oks_p9'),
    path('p9/create/', oks_p9_create, name='oks_p9_create'),
    path('p9/edit/<slug:date_oks_p9>', oks_p9_edit, name='oks_p9_edit'),
    path('p9/delete/<slug:date_oks_p9>', oks_p9_delete, name='oks_p9_delete'),

    path('p10/', oks_p10, name='oks_p10'),
    path('p10/create/', oks_p10_create, name='oks_p10_create'),
    path('p10/edit/<slug:date_oks_p10>', oks_p10_edit, name='oks_p10_edit'),
    path('p10/delete/<slug:date_oks_p10>', oks_p10_delete, name='oks_p10_delete'),

]
