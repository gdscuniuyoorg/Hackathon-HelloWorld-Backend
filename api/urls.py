from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import (get_distance, register_user, AttendanceList,
                    AttendanceCreate, StudentDetailView)


urlpatterns = [
    path('token/', obtain_auth_token, name='api-token-auth'),
    path('getdistance/', get_distance, name='get_distance'),
    path('register/', register_user, name='register'),
    path('student/<slug:reg_no>/', StudentDetailView.as_view(),
         name='student-detail'),
    path('attendancelist/', AttendanceList.as_view(), name='attendance_list'),
    path('attendanceadd/', AttendanceCreate.as_view(), name='attendance_add'),
]
