from django.contrib import admin
from .models import Venue, CustomUser

# Register your models here.
admin.site.register(Venue)
admin.site.register(CustomUser)
