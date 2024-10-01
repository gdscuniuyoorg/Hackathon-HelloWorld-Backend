from django.urls import path
from .views import get_distance


urlpatterns = [
    path('get_distance/', get_distance, name='get_distance'),
]
