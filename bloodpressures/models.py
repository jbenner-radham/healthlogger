from django.db import models


class BloodPressure(models.Model):
    id = models.AutoField(primary_key=True)
    systolic = models.PositiveSmallIntegerField(blank=False)
    diastolic = models.PositiveSmallIntegerField(blank=False)
    time = models.DateTimeField()

    def __str__(self):
        return f'{self.systolic}/{self.diastolic} mm Hg'
