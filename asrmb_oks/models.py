from django.db import models
from django.urls import reverse


# Create your models here.
class P1ComponentCompositionOfUnstableCondensate(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    molar_content_of_components = models.FloatField()
    molar_mass_of_the_component = models.FloatField()
    total_molar_mass = models.FloatField()
    chromatograph_mass = models.FloatField()
    calculated_mass = models.FloatField()
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('p1_edit', kwargs={'date_oks_p1': self.date_update})

    class Meta:
        managed = False
        db_table = 'p1_component_composition_of_unstable_condensate'


class P2ComponentCompositionOfGas(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    molar_content_of_components = models.FloatField()
    molar_mass_of_the_component = models.FloatField()
    total_molar_mass = models.FloatField()
    chromatograph_mass = models.FloatField()
    calculated_mass = models.FloatField()
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'p2_component_composition_of_gas'


class P3DeterminationOfTheComponentOfGas(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    molar_content_of_components = models.FloatField()
    molar_mass_of_the_component = models.FloatField()
    total_molar_mass = models.FloatField()
    chromatograph_mass = models.FloatField()
    calculated_mass = models.FloatField()
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'p3_determination_of_the_component_of_gas'


class P4GasCompositionToTheProtocol(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    molar_content_of_components = models.FloatField()
    molar_mass_of_the_component = models.FloatField()
    total_molar_mass = models.FloatField()
    chromatograph_mass = models.FloatField()
    calculated_mass = models.FloatField()
    content_of_the_component = models.FloatField()
    proportion_of_the_component = models.FloatField()
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'p4_gas_composition_to_the_protocol'


class P5DeterminationOfTheComponentComposition(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    molar_content_of_components = models.FloatField()
    molar_mass_of_the_component = models.FloatField()
    total_molar_mass = models.FloatField()
    chromatograph_mass = models.FloatField()
    calculated_mass = models.FloatField()
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'p5_determination_of_the_component_composition'


class P6CompositionOfGasOutput(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    molar_content_of_components = models.FloatField()
    molar_mass_of_the_component = models.FloatField()
    total_molar_mass = models.FloatField()
    chromatograph_mass = models.FloatField()
    calculated_mass = models.FloatField()
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'p6_composition_of_gas_output'


class P7CompositionOfGas10c(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    molar_content_of_components = models.FloatField()
    molar_mass_of_the_component = models.FloatField()
    total_molar_mass = models.FloatField()
    chromatograph_mass = models.FloatField()
    calculated_mass = models.FloatField()
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'p7_composition_of_gas_10c'


class P8CompositionOfTheCondensate(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    cylinder_1506 = models.FloatField()
    cylinder_1641 = models.FloatField()
    average_value = models.FloatField()
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'p8_composition_of_the_condensate'


class P9ComponentOfTheSeparationGas(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    molar_content_of_components = models.FloatField()
    molar_mass_of_the_component = models.FloatField()
    total_molar_mass = models.FloatField()
    chromatograph_mass = models.FloatField()
    calculated_mass = models.FloatField()
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'p9_component_of_the_separation_gas'


class P10ProtokolKGN(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    structure = models.CharField(max_length=255)
    molar_mass_of_the_component = models.FloatField()
    chromatograph_mass = models.FloatField()
    difference = models.FloatField()
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'p10_protokol_kng'
