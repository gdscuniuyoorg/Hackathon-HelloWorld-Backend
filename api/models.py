from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Venue(models.Model):
    short_name = models.CharField(max_length=10)
    full_name = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.FloatField(blank=True, null=True)

    @property
    def coords(self):
        return [self.latitude, self.longitude]

    def __str__(self):
        return self.full_name


# Custom User Model
class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('teacher', 'Teacher'),
        ('student', 'Student'),
        ('admin', 'Admin'),
    ]
    email = models.EmailField(unique=True, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    reg_no = models.CharField(max_length=15, blank=True, null=True)
    role = models.CharField(max_length=10,
                            choices=ROLE_CHOICES, default='student')

    def __str__(self):
        return f'Username = {self.username} : Role = {self.get_role_display()}'
