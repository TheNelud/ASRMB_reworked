# Generated by Django 3.2.16 on 2023-01-10 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asrmb_raports', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mer_per_month',
            fields=[
                ('id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('mer_1', models.CharField(max_length=255)),
                ('mer_2', models.CharField(max_length=255)),
                ('mer_3', models.CharField(max_length=255)),
                ('mer_4', models.CharField(max_length=255)),
                ('mer_5', models.CharField(max_length=255)),
                ('mer_6', models.CharField(max_length=255)),
                ('mer_7', models.CharField(max_length=255)),
                ('mer_8', models.CharField(max_length=255)),
                ('mer_9', models.CharField(max_length=255)),
                ('mer_10', models.CharField(max_length=255)),
                ('mer_11', models.CharField(max_length=255)),
                ('mer_12', models.CharField(max_length=255)),
                ('mer_13', models.CharField(max_length=255)),
                ('mer_14', models.CharField(max_length=255)),
                ('mer_15', models.CharField(max_length=255)),
                ('mer_16', models.CharField(max_length=255)),
                ('mer_17', models.CharField(max_length=255)),
                ('mer_18', models.CharField(max_length=255)),
                ('mer_19', models.CharField(max_length=255)),
                ('mer_20', models.CharField(max_length=255)),
                ('mer_21', models.CharField(max_length=255)),
                ('mer_22', models.CharField(max_length=255)),
                ('mer_23', models.CharField(max_length=255)),
                ('mer_24', models.CharField(max_length=255)),
                ('mer_25', models.CharField(max_length=255)),
                ('mer_26', models.CharField(max_length=255)),
                ('mer_27', models.CharField(max_length=255)),
                ('mer_28', models.CharField(max_length=255)),
                ('mer_29', models.CharField(max_length=255)),
                ('mer_30', models.CharField(max_length=255)),
                ('mer_31', models.CharField(max_length=255)),
                ('mer_32', models.CharField(max_length=255)),
                ('date_update', models.DateTimeField()),
            ],
            options={
                'db_table': 'mer_per_month',
                'ordering': ['date_update'],
                'managed': False,
            },
        ),
    ]
