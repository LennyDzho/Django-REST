from django.db import models

# Create your models here.

class Sensor(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

class TemperatureMeasurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name="measurements")
    temperature = models.FloatField()
    measured_at = models.DateTimeField(auto_now_add=True)
