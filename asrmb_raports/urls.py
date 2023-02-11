from . import views
from django.urls import path



urlpatterns = [

    path('sar/', views.sar, name='sar'),
    path('sar/edit/<slug:date_sar>', views.sar_edit, name='sar_edit'),

    path('mar/', views.mar, name='mar'),
    path('mar/edit/<slug:date_mar>', views.mar_edit, name='mar_edit'),

    path('mag/', views.mag, name='mag'),
    path('mag/edit/<slug:date_mag>', views.mag_edit, name='mag_edit'),




]