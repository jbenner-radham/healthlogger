# Generated by Django 2.2.6 on 2019-10-28 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medications', '0004_auto_20191028_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medication',
            name='time',
            field=models.DateTimeField(),
        ),
    ]
