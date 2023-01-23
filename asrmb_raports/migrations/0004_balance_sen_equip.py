# Generated by Django 3.2.16 on 2023-01-23 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asrmb_raports', '0003_alter_ser_per_month_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('par_a', models.CharField(max_length=255)),
                ('par_b', models.CharField(max_length=255)),
                ('par_c', models.CharField(max_length=255)),
                ('par_d', models.CharField(max_length=255)),
                ('par_e', models.CharField(max_length=255)),
                ('par_f', models.CharField(max_length=255)),
                ('par_g_nmag', models.CharField(max_length=255)),
                ('par_g_rmag_30i_1', models.CharField(max_length=255)),
                ('par_g_rmag_60e_1', models.CharField(max_length=255)),
                ('par_h', models.CharField(max_length=255)),
                ('par_i', models.CharField(max_length=255)),
                ('par_j', models.CharField(max_length=255)),
                ('par_k', models.CharField(max_length=255)),
                ('par_l', models.CharField(max_length=255)),
                ('par_m', models.CharField(max_length=255)),
                ('par_n', models.CharField(max_length=255)),
                ('par_o', models.CharField(max_length=255)),
                ('par_p', models.CharField(max_length=255)),
                ('par_q', models.CharField(max_length=255)),
                ('par_r', models.CharField(max_length=255)),
                ('par_s', models.CharField(max_length=255)),
                ('par_t', models.CharField(max_length=255)),
                ('par_u', models.CharField(max_length=255)),
                ('par_v', models.CharField(max_length=255)),
                ('par_w', models.CharField(max_length=255)),
                ('par_x', models.CharField(max_length=255)),
                ('par_aa', models.CharField(max_length=255)),
                ('par_bb', models.CharField(max_length=255)),
                ('par_cc', models.CharField(max_length=255)),
                ('date_create', models.DateField(auto_now_add=True)),
                ('date_update', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'balance',
                'ordering': ['date_update'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sen_equip',
            fields=[
                ('id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('r1', models.CharField(max_length=255)),
                ('r2', models.CharField(max_length=255)),
                ('r3', models.CharField(max_length=255)),
                ('r4', models.CharField(max_length=255)),
                ('r5', models.CharField(max_length=255)),
                ('r6', models.CharField(max_length=255)),
                ('r7', models.CharField(max_length=255)),
                ('r8', models.CharField(max_length=255)),
                ('r9', models.CharField(max_length=255)),
                ('r10', models.CharField(max_length=255)),
                ('r11', models.CharField(max_length=255)),
                ('r12', models.CharField(max_length=255)),
                ('dy13', models.CharField(max_length=255)),
                ('rt13', models.CharField(max_length=255)),
                ('dy14', models.CharField(max_length=255)),
                ('rt14', models.CharField(max_length=255)),
                ('dy15', models.CharField(max_length=255)),
                ('rt15', models.CharField(max_length=255)),
                ('dy16', models.CharField(max_length=255)),
                ('rt16', models.CharField(max_length=255)),
                ('r17', models.CharField(max_length=255)),
                ('r18', models.CharField(max_length=255)),
                ('r19', models.CharField(max_length=255)),
                ('r22', models.CharField(max_length=255)),
                ('r23', models.CharField(max_length=255)),
                ('r24', models.CharField(max_length=255)),
                ('r25', models.CharField(max_length=255)),
                ('r26', models.CharField(max_length=255)),
                ('r27', models.CharField(max_length=255)),
                ('date_create', models.DateField(auto_now_add=True)),
                ('date_update', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'sen_equip',
                'ordering': ['date_update'],
                'managed': False,
            },
        ),
    ]