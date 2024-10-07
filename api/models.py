from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


# Create your models here.

class Venue(models.Model):
    short_name = models.CharField(max_length=10, unique=True)
    full_name = models.CharField(max_length=255, unique=True)
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
    reg_no = models.CharField(max_length=15, blank=True, null=True, unique=True)
    role = models.CharField(max_length=10,
                            choices=ROLE_CHOICES, default='student')

    def save(self, *args, **kwargs):
        # Ensure only students have a reg no
        if self.role != 'student' and self.reg_no:
            raise ValidationError('Only student can have reg_no')
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Username = {self.username} : Role = {self.get_role_display()}'


class Course(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    teachers = models.ForeignKey(CustomUser, on_delete=models.SET_NULL,
                                 null=True, related_name='courses_taught')

    def __str__(self):
        return self.name


class Attendance(models.Model):
    STATUS_CHOICES = [
        ('present', 'Present'),
        ('absent', 'Absent')
    ]


    reg_no = models.ForeignKey(CustomUser, to_field='reg_no', on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(default=timezone.now)
    course = models.ForeignKey(Course, to_field='name', on_delete=models.CASCADE, null=True)
    time = models.TimeField(default=timezone.now)

    venue = models.ForeignKey(Venue, to_field='short_name', on_delete=models.SET_NULL, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['reg_no', 'date', 'course'],
                                    name='unique_attendance',)
        ]

    def clean(self):
        # Prevent attendance for future dates
        if self.date > timezone.now().date():
            raise ValidationError('Cannot add attendance for future date')

        if self.reg_no.role != 'student':
            raise ValidationError('Only student can add attendance')

    def __str__(self):
        return f'{self.reg_no.reg_no} || {self.date} || {self.course} || {self.time}'
