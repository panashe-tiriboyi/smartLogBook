from django.urls import path, include
from .views import HomeAttendance
from . import views

urlpatterns = [
    path('', views.HomeAttendance, name='homeAttendance'),
    path('login/', views.login, name='login')
]
