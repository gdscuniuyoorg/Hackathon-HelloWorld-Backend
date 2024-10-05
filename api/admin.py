from django.contrib import admin
from .models import Venue, CustomUser, Course, Attendance

# Register your models here.
admin.site.register(Venue)
admin.site.register(CustomUser)
admin.site.register(Course)
admin.site.register(Attendance)