from django.urls import path
from .views import get_distance, register_user


urlpatterns = [
    path('get_distance/', get_distance, name='get_distance'),
    path('register/', register_user, name='register'),
]
