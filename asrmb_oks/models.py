from django.db import models
from django.urls import reverse


# Create your models here.
class P1ComponentCompositionOfUnstableCondensate(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    molar_components = models.FloatField()
    molar_mass_of_the_component = models.FloatField()
    total_molar_mass = models.FloatField()
    chromatograph_mass = models.FloatField()
    calculated_mass = models.FloatField()
    date_create = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now=True)

    def get_absolute_url(self):
        return reverse('p1_edit', kwargs={'date_p1': self.date_update})

    class Meta:
        # ordering = ['id']
        managed = False
        db_table = 'p1_component_composition_of_unstable_condensate'
