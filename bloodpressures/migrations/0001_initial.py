# Generated by Django 2.2.6 on 2019-10-26 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BloodPressure',
            fields=[
                ('blood_pressure_id', models.AutoField(primary_key=True, serialize=False)),
                ('blood_pressure_systolic', models.PositiveSmallIntegerField()),
                ('blood_pressure_diastolic', models.PositiveSmallIntegerField()),
                ('time', models.DateTimeField()),
            ],
        ),
    ]
