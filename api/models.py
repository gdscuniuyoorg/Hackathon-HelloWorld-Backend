from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Venue(models.Model):
    short_name = models.CharField(max_length=10)
    full_name = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.FloatField(blank=True)

    @property
    def coords(self):
        return [self.latitude, self.longitude]

    def __str__(self):
        return self.full_name
