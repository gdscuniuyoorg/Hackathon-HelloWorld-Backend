from django.test import TestCase
from django.urls import reverse
from .models import Venue
from rest_framework.decorators import api_view
from rest_framework.response import Response


#Filling the Database
class GetDistanceAPITestCase(TestCase):
    url = reverse('get_distance')
    #populate_db
    def setup(self):
        self.venue = Venue.objects.create(
            short_name = '1kCap',
            full_name = '100 Capacity',
            latitude = 5.0492068,
            longitude = 7.9363032
        )
        
    # Testing Near
    def test_get_distance_near(self):
        params = {
            'name' :'1kCap',
            'latitude': 5.0492068,
            'longitude': 7.9363032
        }
        response = self.client.get(self.url,params)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertIn('distance',response.data)
        self.assertIn('Am I Near',response.data)
        self.assertEqual(response.data['Am I Near'], 'You are near')
    
