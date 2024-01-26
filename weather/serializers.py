"""
serializer for weather app
"""
from rest_framework import serializers


class CoolestDistrictsSerializer(serializers.Serializer):
    """
    serializer for coolest districts
    """
    name = serializers.CharField(max_length=200)
    temp = serializers.FloatField()


class LocationSerializer(serializers.Serializer):
    """
    serializer for location
    """
    lat = serializers.FloatField(required=True)
    long = serializers.FloatField(required=True)


class SuggestionSerializer(serializers.Serializer):
    """
    serializer for suggestion to travel
    """
    location = LocationSerializer(required=True, help_text="Your current location")
    destination = LocationSerializer(required=True, help_text='Your destination location')
    date = serializers.DateField(required=True, format="%Y-%m-%d", help_text="Format: YYYY-MM-DD")


