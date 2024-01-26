"""
api views for weather app
"""
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response

from .utils import get_weather_data


class CoolestDistrictAPIView(APIView):
    """
    api view for 10 coolest districts
        url: api/v1/coolest_districts/
        return:
    {
      "data": [
            {
              "name": "Dinajpur",
              "temp": 10
            },
            {
              "name": "Panchagarh",
              "temp": 10
            },
            {
              "name": "Thakurgaon",
              "temp": 10
            },
            {
              "name": "Bandarban",
              "temp": 10
            },
            {
              "name": "Khagrachari",
              "temp": 10
            },
            {
              "name": "Jamalpur",
              "temp": 11
            },
            {
              "name": "Munshiganj",
              "temp": 11
            },
            {
              "name": "Mymensingh",
              "temp": 11
            },
            {
              "name": "Netrokona",
              "temp": 11
            },
            {
              "name": "Sherpur",
              "temp": 11
            }
          ]
        }
    """
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        weather_data = get_weather_data()
        if weather_data:
            return Response({"data": weather_data}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Sorry an error occurred. Please try again."}, status=status)

