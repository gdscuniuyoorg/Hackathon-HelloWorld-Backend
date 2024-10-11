from io import BytesIO
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import get_user_model, authenticate
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from vincenty import vincenty
from .models import Venue, Attendance, CustomUser
from .serializers import (CustomUserSerializer, AttendanceSerializer,
                          StudentDetailSerializer, VenueSerializer)
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import requests

User = get_user_model()


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


def pdfgen(request, course, date, start_time, stop_time):
    # Example: Making an API call to get JSON data (replace with your actual API call)
    api_url = (f"http://localhost:8000/api/attendancelist/"
               f"?course={course}&date={date}&"
               f"start_time={start_time}&stop_time={stop_time}")
    headers = {'Authorization': 'Token c0af34fd2f8fac7cb84595a9ca18789f465cab35'}
    response = requests.get(api_url, headers=headers)

    if response.status_code != 200:
        return JsonResponse({'error': 'API call failed'}, status=400)

    # This is our json data
    data = response.json()

    # Create bytestream buffer
    buffer = BytesIO()

    # Create a canvas
    p = canvas.Canvas(buffer, pagesize=letter)
    p.setFont("Helvetica", 12)

    p.drawString(10, 750, "Attendance Report")

    # Loop over the JSON data and add it to the PDF
    y_position = 720
    for item in data:
        # Assuming data is a list of dictionaries with keys like 'name', 'date', 'status'
        reg_no = item.get('reg_no', 'N/A')
        time = item.get('time', 'N/A')
        course = item.get('course', 'N/A')
        date = item.get('date', 'N/A')

        # Add data to the PDF
        p.drawString(10, y_position, f"Reg No: {reg_no} | Time: {time} | Course: {course} | Date: {date}  |")
        y_position -= 20  # Move to the next line

    # Close the PDF object
    p.showPage()
    p.save()

    # Get the value of the BytesIO buffer and write it to the response
    pdf = buffer.getvalue()
    buffer.close()

    # Return a response as a PDF file
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="generated_pdf.pdf"'

    return response


class VenueCreate(generics.CreateAPIView):
    """
    API to create venue
    """
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer


class VenueList(generics.ListAPIView):
    """
    API to get all venues
    """
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer


class CustomLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        # Extract username and password from the request
        username = request.data.get('username')
        password = request.data.get('password')

        # Authenticate the user
        user = authenticate(username=username, password=password)

        if user is not None:
            # If authentication was successful, get or create a token for the user
            token, created = Token.objects.get_or_create(user=user)
            # Return the token in the response
            return Response({
                'token': token.key,
                'user_id': user.id,
                'username': user.username
            }, status=status.HTTP_200_OK)
        else:
            # If authentication failed, return an error message
            return Response({
                'error': 'Invalid credentials, please try again.'
            }, status=status.HTTP_400_BAD_REQUEST)

    # If any method other than POST is used, return 405 Method Not Allowed
    def get(self, request, *args, **kwargs):
        return Response({
            'error': 'Method not allowed.'
        }, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def put(self, request, *args, **kwargs):
        return Response({
            'error': 'Method not allowed.'
        }, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def delete(self, request, *args, **kwargs):
        return Response({
            'error': 'Method not allowed.'
        }, status=status.HTTP_405_METHOD_NOT_ALLOWED)
