# Generated by Django 2.2.6 on 2019-10-27 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(choices=[('adderall', 'Adderall'), ('vyvanse', 'Vyvanse')], max_length=256)),
                ('blood_pressure_diastolic', models.PositiveSmallIntegerField()),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
