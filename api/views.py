from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from vincenty import vincenty
from .models import Venue, Attendance, CustomUser
from .serializers import (CustomUserSerializer, AttendanceSerializer,
                          StudentDetailSerializer)



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
            return f'You are far'
        else:
            return f'You are near'

    # generate result
    result = {'distance': distance, 'Am I Near': is_near(distance)}

    return Response(result)


@api_view(['POST'])
def register_user(request):
    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class StudentDetailView(generics.RetrieveAPIView):
    """
    API endpoint to retrieve a student's details
    """
    queryset = CustomUser.objects.filter(role='student')
    serializer_class = StudentDetailSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        student_id = self.kwargs.get('reg_no')
        return CustomUser.objects.get(reg_no=student_id)


@login_required
def teacher_dashboard(request):
    if request.user.role == 'teacher':
        pass
    else:
        return HttpResponse("Access Denied", status=403)


class AttendanceCreate(generics.CreateAPIView):
    """
    API endpoint that allows Attendance to be created.
    """
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save()


class AttendanceList(generics.ListAPIView):
    """
        View to get attendance within a time frame
    """
    serializer_class = AttendanceSerializer

    def get_queryset(self):
        course = self.request.query_params.get('course', None)
        date = self.request.query_params.get('date', None)
        start_time = self.request.query_params.get('start_time', None)
        stop_time = self.request.query_params.get('stop_time', None)

        queryset = Attendance.objects.all()

        queryset = queryset.filter(
            course__name=course, date=date,
            time__range=(start_time, stop_time))

        return queryset

