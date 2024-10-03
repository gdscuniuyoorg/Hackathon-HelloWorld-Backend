from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


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


class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    teachers = models.ForeignKey(CustomUser, on_delete=models.SET_NULL,
                                 null=True, related_name='courses_taught')

    def __str__(self):
        return self.name


class Attendance(models.Model):
    STATUS_CHOICES = [
        ('present', 'Present'),
        ('absent', 'Absent'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    date = models.DateField(default=timezone.now)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    time = models.TimeField(default=timezone.now)
    venue = models.ForeignKey(Venue, on_delete=models.SET_NULL, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'date', 'course'],
                                    name='unique_user_date')
        ]
