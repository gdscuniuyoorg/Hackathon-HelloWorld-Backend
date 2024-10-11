from django.urls import path, re_path
from rest_framework.authtoken.views import obtain_auth_token
from .views import (get_distance, register_user, AttendanceList,
                    AttendanceCreate, StudentDetailView, pdfgen,
                    VenueCreate, VenueList, CustomLoginView,home)


urlpatterns = [
    path('', home, name='home'),
    path('token/', obtain_auth_token, name='api-token-auth'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('getdistance/', get_distance, name='get_distance'),
    path('register/', register_user, name='register'),
    path('student/<slug:reg_no>/', StudentDetailView.as_view(),
         name='student-detail'),
    path('attendancelist/', AttendanceList.as_view(), name='attendance_list'),
    path('attendanceadd/', AttendanceCreate.as_view(), name='attendance_add'),
    path('venueadd/', VenueCreate.as_view(), name='venue_add'),
    path('venuelist/', VenueList.as_view(), name='venue_list'),
    re_path(r'^pdfgen/(?P<course>[A-Za-z0-9]+)/(?P<date>\d{4}-\d{2}-\d{2})/'
            r'(?P<start_time>\d{2}:\d{2}:\d{2})/'
            r'(?P<stop_time>\d{2}:\d{2}:\d{2})/$', pdfgen, name='pdfgen')
    
]
