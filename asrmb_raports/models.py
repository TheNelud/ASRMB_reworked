from django.db import models

# Create your models here.
class Ser_per_day(models.Model):
    id = models.SmallAutoField(primary_key=True)
    ser_1 = models.CharField(max_length=255)
    ser_2 = models.CharField(max_length=255)
    ser_3 = models.CharField(max_length=255)
    ser_4 = models.CharField(max_length=255)
    ser_5 = models.CharField(max_length=255)
    ser_6 = models.CharField(max_length=255)
    ser_7 = models.CharField(max_length=255)
    ser_8 = models.CharField(max_length=255)
    ser_9 = models.CharField(max_length=255)
    ser_10 = models.CharField(max_length=255)
    ser_11 = models.CharField(max_length=255)
    ser_12 = models.CharField(max_length=255)
    ser_13 = models.CharField(max_length=255)
    ser_14 = models.CharField(max_length=255)
    ser_15 = models.CharField(max_length=255)
    ser_16 = models.CharField(max_length=255)
    ser_17 = models.CharField(max_length=255)
    ser_18 = models.CharField(max_length=255)
    ser_19 = models.CharField(max_length=255)
    ser_20 = models.CharField(max_length=255) 
    date_update = models.DateField()


    class Meta:
        # ordering = ['-date_update']
        managed = False
        db_table = 'ser_per_day'

class Ser_per_month(models.Model):
    id = models.SmallAutoField(primary_key=True)
    ser_101 = models.CharField(max_length=255)
    ser_102 = models.CharField(max_length=255)
    ser_103 = models.CharField(max_length=255)
    ser_104 = models.CharField(max_length=255)
    ser_105 = models.CharField(max_length=255)
    ser_106 = models.CharField(max_length=255)
    ser_107 = models.CharField(max_length=255)
    ser_108 = models.CharField(max_length=255)
    ser_109 = models.CharField(max_length=255)
    ser_110 = models.CharField(max_length=255)
    ser_111 = models.CharField(max_length=255)
    ser_112 = models.CharField(max_length=255)
    ser_113 = models.CharField(max_length=255)
    ser_114 = models.CharField(max_length=255)
    ser_115 = models.CharField(max_length=255)
    ser_116 = models.CharField(max_length=255)
    ser_117 = models.CharField(max_length=255)
    ser_118 = models.CharField(max_length=255)
    ser_119 = models.CharField(max_length=255)
    ser_120 = models.CharField(max_length=255)
    date_update = models.DateTimeField()


    class Meta:
        ordering = ['date_update']
        managed = False
        db_table = 'ser_per_month'