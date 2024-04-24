from django.urls import path, include
from .views import HomeAttendance

urlpatterns = [
    path(HomeAttendance, include('attendance.urls')),
]
