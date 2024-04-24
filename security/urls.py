from django.urls import path, include
from .views import HomeSecurity

urlpatterns = [

    path(HomeSecurity, include('security.urls')),
]
