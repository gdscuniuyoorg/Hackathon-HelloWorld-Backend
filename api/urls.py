from django.urls import path
from .views import get_distance, register_user, attend_data


urlpatterns = [
    path('get_distance/', get_distance, name='get_distance'),
    path('register/', register_user, name='register'),
    path('attend_data/', attend_data, name='attend_data')
]
