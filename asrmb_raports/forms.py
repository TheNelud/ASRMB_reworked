from django import forms
from .models import *
from django.forms import ModelForm

class Ser_per_day_form(ModelForm):
    ser_1 = forms.CharField(max_length=255)
    ser_2 = forms.CharField(max_length=255)
    ser_3 = forms.CharField(max_length=255)
    ser_4 = forms.CharField(max_length=255)
    ser_5 = forms.CharField(max_length=255)
    ser_6 = forms.CharField(max_length=255)
    ser_7 = forms.CharField(max_length=255)
    ser_8 = forms.CharField(max_length=255)
    ser_9 = forms.CharField(max_length=255)
    ser_10 = forms.CharField(max_length=255)
    ser_11 = forms.CharField(max_length=255)
    ser_12 = forms.CharField(max_length=255)
    ser_13 = forms.CharField(max_length=255)
    ser_14 = forms.CharField(max_length=255)
    ser_15 = forms.CharField(max_length=255)
    ser_16 = forms.CharField(max_length=255)
    ser_17 = forms.CharField(max_length=255)
    ser_18 = forms.CharField(max_length=255)
    ser_19 = forms.CharField(max_length=255)
    ser_20 = forms.CharField(max_length=255) 
    date_update = forms.DateField()
   
    class Meta:
        model = Ser_per_day
        fields = '__all__'

class Ser_per_month_form(ModelForm):
    ser_101 = forms.CharField(max_length=255)
    ser_102 = forms.CharField(max_length=255)
    ser_103 = forms.CharField(max_length=255)
    ser_104 = forms.CharField(max_length=255)
    ser_105 = forms.CharField(max_length=255)
    ser_106 = forms.CharField(max_length=255)
    ser_107 = forms.CharField(max_length=255)
    ser_108 = forms.CharField(max_length=255)
    ser_109 = forms.CharField(max_length=255)
    ser_110 = forms.CharField(max_length=255)
    ser_111 = forms.CharField(max_length=255)
    ser_112 = forms.CharField(max_length=255)
    ser_113 = forms.CharField(max_length=255)
    ser_114 = forms.CharField(max_length=255)
    ser_115 = forms.CharField(max_length=255)
    ser_116 = forms.CharField(max_length=255)
    ser_117 = forms.CharField(max_length=255)
    ser_118 = forms.CharField(max_length=255)
    ser_119 = forms.CharField(max_length=255)
    ser_120 = forms.CharField(max_length=255) 
    date_update = forms.DateField()
    class Meta:
        model = Ser_per_month
        fields = '__all__'