"""
api views for weather app
"""
from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response

from .utils import get_weather_data

from .serializers import CoolestDistrictsSerializer


class CoolestDistrictAPIView(GenericAPIView):
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
    serializer_class = CoolestDistrictsSerializer

    def get(self, request, *args, **kwargs):
        weather_data = get_weather_data()
        if weather_data is not None:
            serializer = self.serializer_class(weather_data, many=True)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Sorry an error occurred. Please try again."},
                            status=status.HTTP_400_BAD_REQUEST)

