"""
utility functions for weather app
"""
import logging

from django.conf import settings

from openmeteo_sdk.Variable import Variable
import requests_cache
import openmeteo_requests
from retry_requests import retry

from district_data import (
    district_list,
    lat_list,
    lon_list
)

from strativ_test.exceptions import OpenMateoException


logger = logging.getLogger(__name__)


def get_weather_data() -> list[dict[str, int]] | None:
    """
    get weather data from the district_list
    :return: [
    {
      "name": "Dinajpur",
      "temp": 10
    },
    {
      "name": "Panchagarh",
      "temp": 10
    },
  ]
    """
    try:
        cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
        retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
        om = openmeteo_requests.Client(session=retry_session)
        temp_dict = {}
        params = {
            "latitude": lat_list,
            "longitude": lon_list,
            "daily": ["temperature_2m_min"],
            "timezone": settings.WEATHER_TIME_ZONE,
            "time": "14:00"
        }
        responses = om.weather_api(settings.WEATHER_API_URL, params=params)

        response_len = len(responses)
        index = 0
        for item in range(response_len):
            t = []
            response = responses[item]
            daily = response.Daily()
            daily_variables = list(
                map(lambda i: daily.Variables(i),
                    range(0, daily.VariablesLength())))
            for i in daily_variables:
                if i.Variable() == Variable.temperature:
                    v = i.ValuesAsNumpy()
                    t.extend(v)
            avg_tem = sum(t) // len(t)
            district_name = district_list[index]['name']

            index += 1
            temp_dict[district_name] = avg_tem
        sorted_items = sorted(temp_dict.items(), key=lambda x: x[1])
        most_cold_cities = dict(sorted_items[:10])
        serialized_data = [{'name': name, 'temp': temp} for name, temp in most_cold_cities.items()]
        return serialized_data
    except OpenMateoException as e:
        logger.exception(e)
        return None
