from django.test import TestCase
from django.urls import include, path, reverse
from rest_framework.test import APITestCase
from rest_framework import status


# Create your tests here.
class TestL3Proccess(APITestCase):

    def test_save_data(self):
        """Ensure we can do a request and add new data."""
        response = self.client.put("/blockchain/save_orders/ETH-USD/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_specific_statistics(self):
        """Check if the data of specific_statistics is correct"""
        self.client.put("/blockchain/save_orders/ETH-USD/")
        response = self.client.get("/blockchain/specific_statistics/bids/ETH-USD/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_general_statistics(self):
        """Check if the data of general_statistics is correct"""
        self.client.put("/blockchain/save_orders/ETH-USD/")
        response = self.client.get("/blockchain/general_statistics/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

