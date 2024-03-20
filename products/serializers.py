from rest_framework import serializers
from .models import *

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Registration
        fields=["companyName","ownerName","rollNo","ownerEmail","accessCode"]

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'