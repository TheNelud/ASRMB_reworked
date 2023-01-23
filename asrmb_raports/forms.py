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
    date_update = forms.DateField(required=False)

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
    ser_117 = forms.CharField(max_length=255, required=False)
    ser_118 = forms.CharField(max_length=255, required=False)
    ser_119 = forms.CharField(max_length=255)
    ser_120 = forms.CharField(max_length=255)
    date_update = forms.DateField(required=False)

    class Meta:
        model = Ser_per_month
        fields = '__all__'


class Mer_per_month_form(ModelForm):
    mer_1 = forms.CharField(max_length=255)
    mer_2 = forms.CharField(max_length=255)
    mer_3 = forms.CharField(max_length=255)
    mer_4 = forms.CharField(max_length=255)
    mer_5 = forms.CharField(max_length=255)
    mer_6 = forms.CharField(max_length=255)
    mer_7 = forms.CharField(max_length=255)
    mer_8 = forms.CharField(max_length=255)
    mer_9 = forms.CharField(max_length=255)
    mer_10 = forms.CharField(max_length=255)
    mer_11 = forms.CharField(max_length=255)
    mer_12 = forms.CharField(max_length=255)
    mer_13 = forms.CharField(max_length=255)
    mer_14 = forms.CharField(max_length=255)
    mer_15 = forms.CharField(max_length=255)
    mer_16 = forms.CharField(max_length=255)
    mer_17 = forms.CharField(max_length=255)
    mer_18 = forms.CharField(max_length=255)
    mer_19 = forms.CharField(max_length=255)
    mer_20 = forms.CharField(max_length=255)
    mer_21 = forms.CharField(max_length=255)
    mer_22 = forms.CharField(max_length=255)
    mer_23 = forms.CharField(max_length=255)
    mer_24 = forms.CharField(max_length=255)
    mer_25 = forms.CharField(max_length=255)
    mer_26 = forms.CharField(max_length=255)
    mer_27 = forms.CharField(max_length=255)
    mer_28 = forms.CharField(max_length=255)
    mer_29 = forms.CharField(max_length=255)
    mer_30 = forms.CharField(max_length=255)
    mer_31 = forms.CharField(max_length=255)
    mer_32 = forms.CharField(max_length=255)
    mer_33 = forms.CharField(max_length=255, required=False)
    mer_34 = forms.CharField(max_length=255, required=False)
    mer_35 = forms.CharField(max_length=255, required=False)
    mer_36 = forms.CharField(max_length=255, required=False)
    mer_37 = forms.CharField(max_length=255, required=False)
    date_update = forms.DateTimeField()

    class Meta:
        model = Mer_per_month
        fields = '__all__'
