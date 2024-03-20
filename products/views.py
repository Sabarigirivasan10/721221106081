from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

class RegistrationView(APIView):
    def post(self,request):
        
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            user.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ProductView(APIView):
    def post(self,request):
         serializer = RegistrationSerializer(data=request.data)
         if serializer.is_valid():
            user=serializer.save()
            user.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
    