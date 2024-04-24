from django.shortcuts import render
from django.http.request import HttpRequest

# Create your views here.

#SecurityLoginView
#SecurityLogoutView


def HomeSecurity(self):
    return (HttpRequest('Hello World! Security'))