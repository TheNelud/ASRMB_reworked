from .models import *
from django import forms
from django.forms import ModelForm, TextInput, inlineformset_factory
from django.forms import formset_factory, modelformset_factory


class P1ComponentCompositionOfUnstableCondensateForm(ModelForm):
    name = forms.CharField(label="Наименование", max_length=255, required=False)
    molar_content_of_components = forms.FloatField(label="Мольное содержание компонентов, %", required=False,
                                                   widget=forms.NumberInput(attrs={'class': 'js-mcc'}))
    molar_mass_of_the_component = forms.FloatField(label='Молярная масса компонента', required=False,
                                                   widget=forms.NumberInput(attrs={'class': 'js-mmc'}))
    total_molar_mass = forms.FloatField(label='Молярная масса общая, гр/моль', required=False,
                                        widget=forms.NumberInput(attrs={'class': 'js-tmm'}))
    chromatograph_mass = forms.FloatField(label='Молярная масса, % (хроматограф)', required=False,
                                          widget=forms.NumberInput(attrs={'class': 'js-cm'}))
    calculated_mass = forms.FloatField(label='Масс, % (расчетная)', required=False,
                                       widget=forms.NumberInput(attrs={'class': 'js-calcm'}))
    date_create = forms.DateTimeField(label='Дата создания', required=False)
    date_update = forms.DateTimeField(label='Дата обновления', required=False)

    class Meta:
        model = P1ComponentCompositionOfUnstableCondensate
        fields = ['name', 'molar_content_of_components', 'molar_mass_of_the_component',
                  'total_molar_mass', 'chromatograph_mass', 'calculated_mass']


P1ComponentCompositionOfUnstableCondensateFormSet = formset_factory(P1ComponentCompositionOfUnstableCondensateForm,
                                                                    extra=0)
P1ModelFormSet = modelformset_factory(model=P1ComponentCompositionOfUnstableCondensate,
                                      form=P1ComponentCompositionOfUnstableCondensateForm)


class P2ComponentCompositionOfGasForm(ModelForm):
    name = forms.CharField(label="Наименование", max_length=255, required=False)
    molar_content_of_components = forms.FloatField(label="Мольное содержание компонентов, %", required=False,
                                                   widget=forms.NumberInput(attrs={'class': 'js-mcc'}))
    molar_mass_of_the_component = forms.FloatField(label='Молярная масса компонента', required=False,
                                                   widget=forms.NumberInput(attrs={'class': 'js-mmc'}))
    total_molar_mass = forms.FloatField(label='Молярная масса общая, гр/моль', required=False,
                                        widget=forms.NumberInput(attrs={'class': 'js-tmm'}))
    chromatograph_mass = forms.FloatField(label='Молярная масса, % (хроматограф)', required=False,
                                          widget=forms.NumberInput(attrs={'class': 'js-cm'}))
    calculated_mass = forms.FloatField(label='Масс, % (расчетная)', required=False,
                                       widget=forms.NumberInput(attrs={'class': 'js-calcm'}))
    date_create = forms.DateTimeField(label='Дата создания', required=False)
    date_update = forms.DateTimeField(label='Дата обновления', required=False)

    class Meta:
        model = P2ComponentCompositionOfGas
        fields = ['name', 'molar_content_of_components', 'molar_mass_of_the_component',
                  'total_molar_mass', 'chromatograph_mass', 'calculated_mass']


P2ComponentCompositionOfGasFormSet = formset_factory(P2ComponentCompositionOfGasForm,
                                                     extra=1)


class P3DeterminationOfTheComponentOfGasForm(ModelForm):
    name = forms.CharField(label="Наименование", max_length=255, required=False)
    molar_content_of_components = forms.FloatField(label="Мольное содержание компонентов, %", required=False,
                                                   widget=forms.NumberInput(attrs={'class': 'js-mcc'}))
    molar_mass_of_the_component = forms.FloatField(label='Молярная масса компонента', required=False,
                                                   widget=forms.NumberInput(attrs={'class': 'js-mmc'}))
    total_molar_mass = forms.FloatField(label='Молярная масса общая, гр/моль', required=False,
                                        widget=forms.NumberInput(attrs={'class': 'js-tmm'}))
    chromatograph_mass = forms.FloatField(label='Молярная масса, % (хроматограф)', required=False,
                                          widget=forms.NumberInput(attrs={'class': 'js-cm'}))
    calculated_mass = forms.FloatField(label='Масс, % (расчетная)', required=False,
                                       widget=forms.NumberInput(attrs={'class': 'js-calcm'}))
    date_create = forms.DateTimeField(label='Дата создания', required=False)
    date_update = forms.DateTimeField(label='Дата обновления', required=False)

    class Meta:
        model = P3DeterminationOfTheComponentOfGas
        fields = ['name', 'molar_content_of_components', 'molar_mass_of_the_component',
                  'total_molar_mass', 'chromatograph_mass', 'calculated_mass']


P3DeterminationOfTheComponentOfGasFormSet = formset_factory(P3DeterminationOfTheComponentOfGasForm,
                                                            extra=1)


class P4GasCompositionToTheProtocolForm(ModelForm):
    name = forms.CharField(label="Наименование", max_length=255, required=False)
    molar_content_of_components = forms.FloatField(label="Мольное содержание компонентов, %", required=False,
                                                   widget=forms.NumberInput(attrs={'class': 'js-mcc'}))
    molar_mass_of_the_component = forms.FloatField(label='Молярная масса компонента', required=False,
                                                   widget=forms.NumberInput(attrs={'class': 'js-mmc'}))
    total_molar_mass = forms.FloatField(label='Молярная масса общая, гр/моль', required=False,
                                        widget=forms.NumberInput(attrs={'class': 'js-tmm'}))
    chromatograph_mass = forms.FloatField(label='Молярная масса, % (хроматограф)', required=False,
                                          widget=forms.NumberInput(attrs={'class': 'js-cm'}))
    calculated_mass = forms.FloatField(label='Масс, % (расчетная)', required=False,
                                       widget=forms.NumberInput(attrs={'class': 'js-calcm'}))
    content_of_the_component = forms.FloatField(label='', required=False,
                                                widget=forms.NumberInput(attrs={'class': 'js-coc'}))
    proportion_of_the_component = forms.FloatField(label='', required=False,
                                                   widget=forms.NumberInput(attrs={'class': 'js-poc'}))
    date_create = forms.DateTimeField(label='Дата создания', required=False)
    date_update = forms.DateTimeField(label='Дата обновления', required=False)

    class Meta:
        model = P4GasCompositionToTheProtocol
        fields = ['name', 'molar_content_of_components', 'molar_mass_of_the_component',
                  'total_molar_mass', 'chromatograph_mass', 'calculated_mass', 'content_of_the_component',
                  'proportion_of_the_component']


P4GasCompositionToTheProtocolFormSet = formset_factory(P4GasCompositionToTheProtocolForm,
                                                       extra=1)


class P5DeterminationOfTheComponentCompositionForm(ModelForm):
    name = forms.CharField(label="Наименование", max_length=255, required=False)
    molar_content_of_components = forms.FloatField(label="Мольное содержание компонентов, %", required=False,
                                                   widget=forms.NumberInput(attrs={'class': 'js-mcc'}))
    molar_mass_of_the_component = forms.FloatField(label='Молярная масса компонента', required=False,
                                                   widget=forms.NumberInput(attrs={'class': 'js-mmc'}))
    total_molar_mass = forms.FloatField(label='Молярная масса общая, гр/моль', required=False,
                                        widget=forms.NumberInput(attrs={'class': 'js-tmm'}))
    chromatograph_mass = forms.FloatField(label='Молярная масса, % (хроматограф)', required=False,
                                          widget=forms.NumberInput(attrs={'class': 'js-cm'}))
    calculated_mass = forms.FloatField(label='Масс, % (расчетная)', required=False,
                                       widget=forms.NumberInput(attrs={'class': 'js-calcm'}))
    date_create = forms.DateTimeField(label='Дата создания', required=False)
    date_update = forms.DateTimeField(label='Дата обновления', required=False)

    class Meta:
        model = P5DeterminationOfTheComponentComposition
        fields = ['name', 'molar_content_of_components', 'molar_mass_of_the_component',
                  'total_molar_mass', 'chromatograph_mass', 'calculated_mass']


P5DeterminationOfTheComponentCompositionFormSet = formset_factory(P5DeterminationOfTheComponentCompositionForm,
                                                                  extra=1)


class P6CompositionOfGasOutputForm(ModelForm):
    name = forms.CharField(label="Наименование", max_length=255, required=False)
    molar_content_of_components = forms.FloatField(label="Мольное содержание компонентов, %", required=False,
                                                   widget=forms.NumberInput(attrs={'class': 'js-mcc'}))
    molar_mass_of_the_component = forms.FloatField(label='Молярная масса компонента', required=False,
                                                   widget=forms.NumberInput(attrs={'class': 'js-mmc'}))
    total_molar_mass = forms.FloatField(label='Молярная масса общая, гр/моль', required=False,
                                        widget=forms.NumberInput(attrs={'class': 'js-tmm'}))
    chromatograph_mass = forms.FloatField(label='Молярная масса, % (хроматограф)', required=False,
                                          widget=forms.NumberInput(attrs={'class': 'js-cm'}))
    calculated_mass = forms.FloatField(label='Масс, % (расчетная)', required=False,
                                       widget=forms.NumberInput(attrs={'class': 'js-calcm'}))
    date_create = forms.DateTimeField(label='Дата создания', required=False)
    date_update = forms.DateTimeField(label='Дата обновления', required=False)

    class Meta:
        model = P6CompositionOfGasOutput
        fields = ['name', 'molar_content_of_components', 'molar_mass_of_the_component',
                  'total_molar_mass', 'chromatograph_mass', 'calculated_mass']


P6CompositionOfGasOutputFormSet = formset_factory(P6CompositionOfGasOutputForm,
                                                  extra=1)


class P7CompositionOfGas10cForm(ModelForm):
    name = forms.CharField(label="Наименование", max_length=255, required=False)
    molar_content_of_components = forms.FloatField(label="Мольное содержание компонентов, %", required=False,
                                                   widget=forms.NumberInput(attrs={'class': 'js-mcc'}))
    molar_mass_of_the_component = forms.FloatField(label='Молярная масса компонента', required=False,
                                                   widget=forms.NumberInput(attrs={'class': 'js-mmc'}))
    total_molar_mass = forms.FloatField(label='Молярная масса общая, гр/моль', required=False,
                                        widget=forms.NumberInput(attrs={'class': 'js-tmm'}))
    chromatograph_mass = forms.FloatField(label='Молярная масса, % (хроматограф)', required=False,
                                          widget=forms.NumberInput(attrs={'class': 'js-cm'}))
    calculated_mass = forms.FloatField(label='Масс, % (расчетная)', required=False,
                                       widget=forms.NumberInput(attrs={'class': 'js-calcm'}))
    date_create = forms.DateTimeField(label='Дата создания', required=False)
    date_update = forms.DateTimeField(label='Дата обновления', required=False)

    class Meta:
        model = P7CompositionOfGas10c
        fields = ['name', 'molar_content_of_components', 'molar_mass_of_the_component',
                  'total_molar_mass', 'chromatograph_mass', 'calculated_mass']


P7CompositionOfGas10cFormSet = formset_factory(P7CompositionOfGas10cForm,
                                               extra=1)


class P8CompositionOfTheCondensateForm(ModelForm):
    name = forms.CharField(label="Наименование", max_length=255, required=False)
    cylinder_1506 = forms.FloatField(label="Резервуар 1506", required=False,
                                     widget=forms.NumberInput(attrs={'class': 'js-sum-c1506'}))
    cylinder_1641 = forms.FloatField(label='Резервуар 1641', required=False,
                                     widget=forms.NumberInput(attrs={'class': 'js-sum-c1641'}))
    average_value = forms.FloatField(label='Среднее значение', required=False,
                                     widget=forms.NumberInput(attrs={'class': 'js-average_value'}))
    date_create = forms.DateTimeField(label='Дата создания', required=False)
    date_update = forms.DateTimeField(label='Дата обновления', required=False)

    class Meta:
        model = P8CompositionOfTheCondensate
        fields = ['name', 'cylinder_1506', 'cylinder_1641',
                  'average_value']


P8CompositionOfTheCondensateFormSet = formset_factory(P8CompositionOfTheCondensateForm,
                                                      extra=1)


class P9ComponentOfTheSeparationGasForm(ModelForm):
    name = forms.CharField(label="Наименование", max_length=255, required=False)
    molar_content_of_components = forms.FloatField(label="Мольное содержание компонентов, %", required=False,
                                                   widget=forms.NumberInput(attrs={'class': 'js-mcc'}))
    molar_mass_of_the_component = forms.FloatField(label='Молярная масса компонента', required=False,
                                                   widget=forms.NumberInput(attrs={'class': 'js-mmc'}))
    total_molar_mass = forms.FloatField(label='Молярная масса общая, гр/моль', required=False,
                                        widget=forms.NumberInput(attrs={'class': 'js-tmm'}))
    chromatograph_mass = forms.FloatField(label='Молярная масса, % (хроматограф)', required=False,
                                          widget=forms.NumberInput(attrs={'class': 'js-cm'}))
    calculated_mass = forms.FloatField(label='Масс, % (расчетная)', required=False,
                                       widget=forms.NumberInput(attrs={'class': 'js-calcm'}))
    date_create = forms.DateTimeField(label='Дата создания', required=False)
    date_update = forms.DateTimeField(label='Дата обновления', required=False)

    class Meta:
        model = P9ComponentOfTheSeparationGas
        fields = ['name', 'molar_content_of_components', 'molar_mass_of_the_component',
                  'total_molar_mass', 'chromatograph_mass', 'calculated_mass']


P9ComponentOfTheSeparationGasFormSet = formset_factory(P9ComponentOfTheSeparationGasForm,
                                                       extra=1)


class P10ProtokolKGNForm(ModelForm):
    name = forms.CharField(label="Наименование", max_length=255, required=False)
    structure = forms.CharField(label='Состав', required=False,
                                widget=forms.NumberInput(attrs={'class': 'js-structure'}))
    molar_mass_of_the_component = forms.FloatField(label='Молярная масса компонента', required=False,
                                                   widget=forms.NumberInput(attrs={'class': 'js-mmc'}))
    chromatograph_mass = forms.FloatField(label='Молярная масса, % (хроматограф)', required=False,
                                          widget=forms.NumberInput(attrs={'class': 'js-cm'}))
    difference = forms.FloatField(label='Молярная масса общая, гр/моль', required=False,
                                  widget=forms.NumberInput(attrs={'class': 'js-diff'}))
    date_create = forms.DateTimeField(label='Дата создания', required=False)
    date_update = forms.DateTimeField(label='Дата обновления', required=False)

    class Meta:
        model = P10ProtokolKGN
        fields = ['name', 'structure', 'molar_mass_of_the_component', 'chromatograph_mass',
                  'difference']


P10ProtokolKGNFormSet = formset_factory(P10ProtokolKGNForm,
                                        extra=42)
