# Generated by Django 2.2.6 on 2019-10-28 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medications', '0003_auto_20191027_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medication',
            name='name',
            field=models.CharField(choices=[('Adderall', 'Adderall'), ('Cyclobenzaprine', 'Cyclobenzaprine'), ('D3', 'D3'), ('Guanfacine HCL ER', 'Guanfacine HCL ER'), ('Lisinopril', 'Lisinopril'), ('Memantine HCL', 'Memantine HCL'), ('Vyvanse', 'Vyvanse')], max_length=256),
        ),
        migrations.AlterField(
            model_name='medication',
            name='time',
            field=models.DateTimeField(auto_created=True),
        ),
    ]