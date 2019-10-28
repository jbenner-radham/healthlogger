# Generated by Django 2.2.6 on 2019-10-27 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloodpressures', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bloodpressure',
            old_name='blood_pressure_diastolic',
            new_name='diastolic',
        ),
        migrations.RenameField(
            model_name='bloodpressure',
            old_name='blood_pressure_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='bloodpressure',
            old_name='blood_pressure_systolic',
            new_name='systolic',
        ),
        migrations.AlterField(
            model_name='bloodpressure',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]