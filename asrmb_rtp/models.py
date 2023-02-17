from django.db import models
from django.urls import reverse

''' 1. Технологические потери природного газа по итогам опорожнения технологического
 оборудования и трубопроводов перед проведением ремонтных работ, м3 (п.4.2.)';
 '''


class TeclossesOne(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    v = models.FloatField()
    pn = models.FloatField()
    tn = models.FloatField()
    zn = models.FloatField()
    press_pk = models.FloatField()
    tk = models.FloatField()
    zk = models.FloatField()
    v_op = models.FloatField()
    ng_prod = models.FloatField()
    ng_nl = models.FloatField()
    xg_prod = models.FloatField()
    n = models.FloatField()
    pn_op = models.FloatField()
    mol = models.FloatField()
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    # def get_absolute_url(self):
    #     return reverse('p1_edit', kwargs={'date_oks_p1': self.date_update})

    class Meta:
        managed = False
        db_table = 'teclosses_one'


''' 
2. Технологические потери природного газа при регенерации технических жидкостей (МЭГа), м3 (п. 4.3.2)';
'''


class TeclossesTwo(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    qgr_sh = models.FloatField()
    ng_prod = models.FloatField()
    ng_pl = models.FloatField()
    xg_prod = models.FloatField()
    pgr_sh = models.FloatField()
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'teclosses_two'


''' 
показания счетчиков 30Р-1
'''


class MeterReading30P1(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateTimeField()
    num_one = models.FloatField()
    num_two = models.FloatField()
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'meter_readings_30P_1'


class MeterReadingAll(models.Model):
    id = models.BigAutoField(primary_key=True)
    meter_p34 = models.FloatField()
    meter_30p1 = models.FloatField()
    meter_10c1 = models.FloatField()
    meter_10c4 = models.FloatField()
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'meter_readings_all'
''' 
 3. Технологические потери природного газа при отборе проб, м3 (п. 4.5)';
'''


class TeclossesTree(models.Model):
    id = models.BigAutoField(primary_key=True)
    type_of_analysis = models.CharField(max_length=255)
    v_pr = models.FloatField()
    p_pr = models.FloatField()
    t_pr = models.FloatField()
    z_pr = models.FloatField()
    b = models.FloatField()
    ni = models.FloatField()
    xr_prod = models.FloatField()
    pr_op = models.FloatField()
    device = models.CharField(max_length=255)
    v_p = models.FloatField()
    tau = models.FloatField()
    xrr_prod = models.FloatField()
    n = models.FloatField()
    pr_pot = models.FloatField()
    pr_pr = models.FloatField()
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'teclosses_three'
