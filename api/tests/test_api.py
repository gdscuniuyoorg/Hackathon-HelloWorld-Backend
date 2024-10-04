from django.test import TestCase
from django.urls import reverse
from api.models import Venue
from .utils import Utils


class GetDistanceAPITestCase(TestCase):
    url = reverse('get_distance')
    #populate tue database
    def setUp(self):
        self.venue = Venue.objects.create(**Utils.fill_db())
    # Testing Near
    def test_get_distance_near(self):
        response = self.client.get(self.url,Utils.params_near())
        Utils.custom_assert(response,200,'distance', 'Am I Near', 'You are far')
        
    #Testing Far
    def test_get_distance_far(self):
        response = self.client.get(self.url,Utils.params_far())
        Utils.custom_assert(response,200,'distance', 'Am I Near', 'You are far')
        
    #Testing missing params
    #Api rejects bad request
    
    #Test remaining APIs