from rest_framework.decorators import api_view
from rest_framework.response import Response
from vincenty import vincenty
from .models import Venue


@api_view(['GET'])
def get_distance(request):
    # get request params
    name = request.query_params.get('name', None)
    latitude = request.query_params.get('latitude', None)
    longitude = request.query_params.get('longitude', None)

    # get specific venue and calculate distance from current location
    venue = Venue.objects.get(short_name=name).coords
    location = (float(latitude), float(longitude))
    distance = vincenty(venue, location)

    def is_near(length):
        if length > 50:
            return f'Your are far'
        else:
            return f'You are near'

    # generate result
    result = {'distance': distance, 'Am I Near': is_near(distance)}

    return Response(result)


