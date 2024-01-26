"""
api views for weather app
"""
from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response

from .utils import (
    get_weather_data,
    get_temperature
)

from .serializers import (
    SuggestionSerializer,
    CoolestDistrictsSerializer
)


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


class SuggestionAPIView(GenericAPIView):
    """
    api view for travel suggestion
        url: api/v1/weather/suggestions/
        :return:
            "data": {
            "source_temp": 22.504499435424805,
            "destination_temp": 22.98699951171875,
            "message": "Your destination temperature is greater than your current temperature."
    }
    """
    permission_classes = [permissions.AllowAny]
    http_method_names = ['post']
    serializer_class = SuggestionSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            source_location = serializer.validated_data['location']
            destination = serializer.validated_data['destination']
            date = serializer.validated_data['date']
            lat_list = [source_location['lat'], destination['lat']]
            long_list = [source_location['long'], destination['long']]
            temp_data = get_temperature(lat_list, long_list, date)
            if temp_data is not None:
                source_temp = temp_data[0]
                destination_temp = temp_data[1]
                if source_temp >= destination_temp:
                    data = {
                        "source_temp": source_temp,
                        "destination_temp": destination_temp,
                        "message": "Your current temperature is greater than or equal to your destination temperature."
                    }
                else:
                    data = {
                        "source_temp": source_temp,
                        "destination_temp": destination_temp,
                        "message": "Your destination temperature is greater than your current temperature."
                    }
                return Response({"data": data}, status=status.HTTP_200_OK)

