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