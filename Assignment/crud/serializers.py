from rest_framework import serializers
from .models import *
from django.core.exceptions import ValidationError


class UserdataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userdata
        fields = '__all__'

class ErrorcodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Errorcode
        fields = '__all__'

