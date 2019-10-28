from django.db import models


class Medication(models.Model):
    NAMES = ['Adderall', 'Cyclobenzaprine', 'D3', 'Guanfacine HCL ER', 'Lisinopril', 'Memantine HCL', 'Vyvanse']
    NAME_CHOICES = [(name, name) for name in NAMES]
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256, choices=NAME_CHOICES)
    dosage = models.CharField(max_length=256)
    time = models.DateTimeField()

    def __str__(self):
        return f'{self.name} {self.dosage}'
