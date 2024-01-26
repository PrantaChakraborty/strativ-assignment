"""
Tests for the weather api views
"""
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient


class CoolestDistrictAPIViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_coolest_districts_view(self):
        response = self.client.get('/api/v1/weather/coolest_districts/')

        # Check if the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check the response structure
        self.assertIn('data', response.data)
        self.assertIsInstance(response.data['data'], list)

        # Check the content of the first item in the list
        first_item = response.data['data'][0]
        self.assertIn('name', first_item)
        self.assertIn('temp', first_item)


class SuggestionAPIViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_suggestion_view(self):
        # Mock data for the test
        request_data = {
            "location": {"lat": 23.7115, "long": 90.4079},
            "destination": {"lat": 22.5726, "long": 88.3639},
            "date": "2024-01-26"
        }
        response = self.client.post('/api/v1/weather/suggestions/', request_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check the response structure
        self.assertIn('data', response.data)
        self.assertIn('source_temp', response.data['data'])
        self.assertIn('destination_temp', response.data['data'])
        self.assertIn('message', response.data['data'])
