from django.db import models
# from django.http import request
from django.urls import reverse
from django.contrib.auth.models import User

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
    date_create = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now=True)
    # user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('sar_edit', kwargs={'date_sar': self.date_update})


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
    date_create = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now=True)
    # user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('sar_edit', kwargs={'date_sar': self.date_create})
    class Meta:
        # ordering = ['date_update']
        managed = False
        db_table = 'ser_per_month'


class Mer_per_month(models.Model):
    id = models.SmallAutoField(primary_key=True)
    mer_1 = models.CharField(max_length=255)
    mer_2 = models.CharField(max_length=255)
    mer_3 = models.CharField(max_length=255)
    mer_4 = models.CharField(max_length=255)
    mer_5 = models.CharField(max_length=255)
    mer_6 = models.CharField(max_length=255)
    mer_7 = models.CharField(max_length=255)
    mer_8 = models.CharField(max_length=255)
    mer_9 = models.CharField(max_length=255)
    mer_10 = models.CharField(max_length=255)
    mer_11 = models.CharField(max_length=255)
    mer_12 = models.CharField(max_length=255)
    mer_13 = models.CharField(max_length=255)
    mer_14 = models.CharField(max_length=255)
    mer_15 = models.CharField(max_length=255)
    mer_16 = models.CharField(max_length=255)
    mer_17 = models.CharField(max_length=255)
    mer_18 = models.CharField(max_length=255)
    mer_19 = models.CharField(max_length=255)
    mer_20 = models.CharField(max_length=255)
    mer_21 = models.CharField(max_length=255)
    mer_22 = models.CharField(max_length=255)
    mer_23 = models.CharField(max_length=255)
    mer_24 = models.CharField(max_length=255)
    mer_25 = models.CharField(max_length=255)
    mer_26 = models.CharField(max_length=255)
    mer_27 = models.CharField(max_length=255)
    mer_28 = models.CharField(max_length=255)
    mer_29 = models.CharField(max_length=255)
    mer_30 = models.CharField(max_length=255)
    mer_31 = models.CharField(max_length=255)
    mer_32 = models.CharField(max_length=255)
    # mer_33 = models.CharField(max_length=255)
    # mer_34 = models.CharField(max_length=255)
    # mer_35 = models.CharField(max_length=255)
    # mer_36 = models.CharField(max_length=255)
    # mer_37 = models.CharField(max_length=255)
    date_create = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now=True)

    def get_absolute_url(self):
        return reverse('mar_edit', kwargs={'date_sar': self.date_create})

    class Meta:
        ordering = ['date_update']
        managed = False
        db_table = 'mer_per_month'


class Sen_equip(models.Model):
    id = models.SmallAutoField(primary_key=True)
    r1 = models.CharField(max_length=255)
    r2 = models.CharField(max_length=255)
    r3 = models.CharField(max_length=255)
    r4 = models.CharField(max_length=255)
    r5 = models.CharField(max_length=255)
    r6 = models.CharField(max_length=255)
    r7 = models.CharField(max_length=255)
    r8 = models.CharField(max_length=255)
    r9 = models.CharField(max_length=255)
    r10 = models.CharField(max_length=255)
    r11 = models.CharField(max_length=255)
    r12 = models.CharField(max_length=255)
    dy13 = models.CharField(max_length=255)
    rt13 = models.CharField(max_length=255)
    dy14 = models.CharField(max_length=255)
    rt14 = models.CharField(max_length=255)
    dy15 = models.CharField(max_length=255)
    rt15 = models.CharField(max_length=255)
    dy16 = models.CharField(max_length=255)
    rt16 = models.CharField(max_length=255)
    r17 = models.CharField(max_length=255)
    r18 = models.CharField(max_length=255)
    r19 = models.CharField(max_length=255)
    # r20 = models.CharField(max_length=255)
    # r21 = models.CharField(max_length=255)
    r22 = models.CharField(max_length=255)
    r23 = models.CharField(max_length=255)
    r24 = models.CharField(max_length=255)
    r25 = models.CharField(max_length=255)
    r26 = models.CharField(max_length=255)
    r27 = models.CharField(max_length=255)
    date_create = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now=True)

    def get_absolute_url(self):
        return reverse('mar_edit', kwargs={'date_mag': self.date_create})
    class Meta:
        ordering = ['date_update']
        managed = False
        db_table = 'sen_equip'


class Balance(models.Model):
    id = models.SmallAutoField(primary_key=True)
    par_a = models.CharField(max_length=255)
    par_b = models.CharField(max_length=255)
    par_c = models.CharField(max_length=255)
    par_d = models.CharField(max_length=255)
    par_e = models.CharField(max_length=255)
    par_f = models.CharField(max_length=255)

    par_g_nmag = models.CharField(max_length=255)
    par_g_rmag_30i_1 = models.CharField(max_length=255)
    par_g_rmag_60e_1 = models.CharField(max_length=255)

    par_h = models.CharField(max_length=255)
    par_i = models.CharField(max_length=255)
    par_j = models.CharField(max_length=255)
    par_k = models.CharField(max_length=255)
    par_l = models.CharField(max_length=255)
    par_m = models.CharField(max_length=255)
    par_n = models.CharField(max_length=255)
    par_o = models.CharField(max_length=255)
    par_p = models.CharField(max_length=255)

    par_q = models.CharField(max_length=255)
    par_r = models.CharField(max_length=255)
    par_s = models.CharField(max_length=255)
    par_t = models.CharField(max_length=255)
    par_u = models.CharField(max_length=255)
    par_v = models.CharField(max_length=255)
    par_w = models.CharField(max_length=255)
    par_x = models.CharField(max_length=255)
    par_aa = models.CharField(max_length=255)
    par_bb = models.CharField(max_length=255)
    par_cc = models.CharField(max_length=255)
    date_create = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now=True)

    def get_absolute_url(self):
        return reverse('mar_edit', kwargs={'date_mag': self.date_create})

    class Meta:
        ordering = ['date_update']
        managed = False
        db_table = 'balance'