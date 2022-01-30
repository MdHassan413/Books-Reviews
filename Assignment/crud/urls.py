from django.urls import path
from .views import *

urlpatterns = [
    path('', PathUrls, name='path_urls'),
    path('user/list/', UserdataList.as_view()),
    path('user/detail/<str:pk>/',UserdataDetail.as_view()),
    path('error/list/', ErrorcodeList.as_view()),
    path('error/detail/<str:pk>/',ErrorcodeDetail.as_view()),
]