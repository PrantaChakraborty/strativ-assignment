"""
weather app URL Configuration file
"""
from django.urls import path

from weather.views import (
    CoolestDistrictAPIView
)

urlpatterns = [
    path('coolest_districts/', CoolestDistrictAPIView.as_view(), name='coolest_districts')
]