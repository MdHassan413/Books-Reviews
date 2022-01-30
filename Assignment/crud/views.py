from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .models import Errorcode, Userdata
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .serializers import ErrorcodeSerializer, UserdataSerializer
# Create your views here.

@api_view(["GET"])
def PathUrls(request):
    api_urls = {
        'User list    ': 'http://127.0.0.1:8000/user/list',
        "User C-R-U-D ": "http://127.0.0.1:8000/user/detail/<str:pk>",
        '    ----     ': '           ---------                       ',
        "Error List   ": "http://127.0.0.1:8000/error/list",
        "Error C-R-U-D": "http://127.0.0.1:8000/error/detail/<str:pk>",
    }
    return Response(api_urls)

class UserdataList(generics.ListCreateAPIView):
    queryset = Userdata.objects.all()
    serializer_class = UserdataSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields = ['id','name', 'age']

class UserdataDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Userdata
    serializer_class = UserdataSerializer

class ErrorcodeList(generics.ListCreateAPIView):
    queryset = Errorcode.objects.all()
    serializer_class = ErrorcodeSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    search_fields = ['id','message']

class ErrorcodeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Errorcode
    serializer_class = ErrorcodeSerializer