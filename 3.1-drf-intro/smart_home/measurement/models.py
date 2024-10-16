from django.db import models


# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(default='')


class Measurement(models.Model):
    sensor = models.ForeignKey(
        Sensor, on_delete=models.CASCADE, related_name='measurements',
    )
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(
        null=True,
        blank=True,
        upload_to='measurement/photos',
        max_length=150,
    )
