from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.decorators import api_view, schema
from rest_framework.parsers import JSONParser

# Create your views here.

#loginView
#LogoutView
#AddEmployeeView
#RemoveEmployeeView
#VerifyEmployeeView

@api_view(['GET', 'POST'])
def HomeAttendance(request):

    data = JSONParser().parse(request)

    id = data['id']
    print(type(data))

    if request.method == 'POST':
       
        return Response(data)
    
    return Response({"message": "Will not appear in schema!"})


@api_view(['GET', 'POST'])
def login(request):
    return Response({"message": "Will not appear in schema!"})

