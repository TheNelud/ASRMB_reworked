from .models import *
from django import forms
from django.forms import ModelForm
from django.forms import formset_factory, modelformset_factory


class P1ComponentCompositionOfUnstableCondensateForm(ModelForm):
    name = forms.CharField(label="Наименование", max_length=255, required=False)
    molar_content_of_components = forms.FloatField(label="Мольное содержание компонентов, %", required=False)
    molar_mass_of_the_component = forms.FloatField(label='Молярная масса компонента', required=False)
    total_molar_mass = forms.FloatField(label='Молярная масса общая, гр/моль', required=False)
    chromatograph_mass = forms.FloatField(label='Молярная масса, % (хроматограф)', required=False)
    calculated_mass = forms.FloatField(label='Масс, % (расчетная)', required=False)
    date_create = forms.DateTimeField(label='Дата создания', required=False)
    date_update = forms.DateTimeField(label='Дата обновления', required=False)

    class Meta:
        model = P1ComponentCompositionOfUnstableCondensate
        fields = ['name', 'molar_content_of_components', 'molar_mass_of_the_component',
                  'total_molar_mass', 'chromatograph_mass', 'calculated_mass']


P1ComponentCompositionOfUnstableCondensateFormSet = formset_factory(P1ComponentCompositionOfUnstableCondensateForm,
                                                                    extra=12)
P1ComponentCompositionOfUnstableCondensateModelFormSet = modelformset_factory(
    P1ComponentCompositionOfUnstableCondensate,
    fields=('name',
            'molar_content_of_components',
            'molar_mass_of_the_component',
            'total_molar_mass',
            'chromatograph_mass',
            'calculated_mass'))
